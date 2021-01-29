from DialogFrameSimple import DialogFrameSimple
from DialogAct import DialogAct
from DialogActTypes import DialogActTypes


class FrameDMSimple:

    def __init__(self, NLU, NLG):
        self.NLU = NLU
        self.NLG = NLG
        # define frame below, for example:
        self.DialogFrame = DialogFrameSimple()
        self.status = None
        self.info = None
        self.confirm_saved_info = None

    def execute(self, inputStr):
        # apply the NLU component
        currentSemanticFrame = self.NLU.parse(inputStr)

        # update the dialog frame with the new information
        self.trackState(currentSemanticFrame)

        # and decide what to do next
        newDialogAct = self.selectDialogAct()

        # then generate some meaningful response
        response = self.NLG.generate(newDialogAct)
        return response

    def trackState(self, newSemanticFrame):
        # update self.DialogFrame based on the contents of newSemanticFrame
        if newSemanticFrame.Intent == 'START_over':
            self.DialogFrame.resetCurOrder()
            print('Your order is reset.')
            self.status = 'NEXT_THING_TO_ASK'
            self.info = None
            self.confirm_saved_info = None
        elif newSemanticFrame.Intent == 'CANCEL_order':
            raise Warning('Your order is canceled.')
        elif newSemanticFrame.Intent == 'REPEAT_order':
            self.status = 'REPEAT'
            self.info = None
            self.confirm_saved_info = None
        elif newSemanticFrame.Intent == 'INFORM_pizza':
            if not self.DialogFrame.cur_order.pizza:
                self.status = 'CONFIRM'
                self.info = 'pizza'
                self.confirm_saved_info = newSemanticFrame.info
            else:
                self.DialogFrame.cur_order.pizza = None
                self.status = 'REVISE'
                self.info = 'pizza'
        elif newSemanticFrame.Intent == 'INFORM_crust':
            if not self.DialogFrame.cur_order.crust:
                self.status = 'CONFIRM'
                self.info = 'crust'
                self.confirm_saved_info = newSemanticFrame.info
            else:
                self.status = 'REVISE'
                self.info = 'crust'
        elif newSemanticFrame.Intent == 'INFORM_size':
            if not self.DialogFrame.cur_order.size:
                self.status = 'CONFIRM'
                self.info = 'size'
                self.confirm_saved_info = newSemanticFrame.info
            else:
                self.status = 'REVISE'
                self.info = 'size'
        elif newSemanticFrame.Intent == 'INFORM_topping':
            if not self.DialogFrame.cur_order.topping:
                self.status = 'CONFIRM'
                self.info = 'topping'
                self.confirm_saved_info = newSemanticFrame.info
            else:
                self.status = 'REVISE'
                self.info = 'topping'
        elif newSemanticFrame.Intent == 'INFORM_phone':
            if not self.DialogFrame.cur_order.phone:
                self.status = 'CONFIRM'
                self.info = 'phone'
                self.confirm_saved_info = newSemanticFrame.info
            else:
                self.status = 'REVISE'
                self.info = 'phone'
        elif newSemanticFrame.Intent == 'INFORM_delivery':
            if not self.DialogFrame.cur_order.delivery_type:
                self.status = 'CONFIRM'
                self.info = 'delivery_type'
                self.confirm_saved_info = newSemanticFrame.info
            else:
                self.status = 'REVISE'
                self.info = 'delivery_type'
        elif newSemanticFrame.Intent == 'INFORM_pick_up':
            if not self.DialogFrame.cur_order.delivery_type:
                self.status = 'CONFIRM'
                self.info = 'delivery_type'
                self.confirm_saved_info = newSemanticFrame.info
            else:
                self.status = 'REVISE'
                self.info = 'pick-up'
        elif newSemanticFrame.Intent == 'INFORM_address':
            if not self.DialogFrame.cur_order.address:
                self.status = 'CONFIRM'
                self.info = 'address'
                self.confirm_saved_info = newSemanticFrame.info
            else:
                self.status = 'REVISE'
                self.info = 'address'
        elif newSemanticFrame.Intent == 'INFORM_reorder':
            self.status = 'CONFIRM'
            self.info = 'reorder'
        elif newSemanticFrame.Intent == 'CHECK_order':
            self.status = 'CHECK'
            self.info = None
        elif newSemanticFrame.Intent == 'REJECT_info':
            self.status = 'NEXT_THING_TO_ASK'
            self.info = None
            self.confirm_saved_info = None
        elif newSemanticFrame.Intent == 'REVISE_info':
            self.status = 'REVISE'
            self.info = newSemanticFrame.info
        elif newSemanticFrame.Intent == 'CONFIRM_info':
            try:
                self.DialogFrame.cur_order.fillAttribute(self.info, self.confirm_saved_info)
            except:
                pass
            self.status = 'NEXT_THING_TO_ASK'
            self.info = 'ok'
            self.confirm_saved_info = None
        else:
            self.status = 'NEXT_THING_TO_ASK'
            self.info = 'confused'
            self.confirm_saved_info = None

    def selectDialogAct(self):
        # decide on what dialog act to execute
        dialogAct = DialogAct()
        if self.status == 'REPEAT':
            dialogAct.DialogActType = DialogActTypes.REPEAT
        elif self.status == 'CONFIRM':
            dialogAct.DialogActType = DialogActTypes.CONFIRM
            dialogAct.info = (self.info, self.confirm_saved_info)
        elif self.status == 'NEXT_THING_TO_ASK':
            next_unfilled_item = self.DialogFrame.curUnfilledItem()
            if not next_unfilled_item:
                dialogAct.DialogActType = DialogActTypes.GOODBYE
                dialogAct.info = str(self.DialogFrame.cur_order)
                self.DialogFrame.addCurOrderToArchive()
            else:
                dialogAct.DialogActType = DialogActTypes.REQUEST
                if self.info == 'ok':
                    dialogAct.info = (next_unfilled_item, 'Okay. ')
                    self.info = None
                elif self.info == 'confused':
                    dialogAct.info = (next_unfilled_item, 'I am confused. ')
                    self.info = None
                else:
                    dialogAct.info = (next_unfilled_item, None)
        elif self.status == 'REVISE':
            dialogAct.DialogActType = DialogActTypes.REVISE
            dialogAct.info = self.info
        elif self.status == 'UNKNOWN':
            dialogAct.DialogActType = DialogActTypes.UNDEFINED
        return dialogAct
