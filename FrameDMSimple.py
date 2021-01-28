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
        if newSemanticFrame.Intent == 'INFORM_pizza':
            if not self.DialogFrame.cur_order.pizza:
                # self.DialogFrame.cur_order.pizza = newSemanticFrame.info
                self.status = 'CONFIRM'
                self.info = 'pizza'
                self.confirm_saved_info = newSemanticFrame.info
            else:
                self.status = 'REVISE'
                self.info = 'pizza'
        elif newSemanticFrame.Intent == 'INFORM_crust':
            if not self.DialogFrame.cur_order.crust:
                # self.DialogFrame.cur_order.crust = newSemanticFrame.info
                self.status = 'CONFIRM'
                self.info = 'crust'
                self.confirm_saved_info = newSemanticFrame.info
            else:
                self.status = 'REVISE'
                self.info = 'crust'
        elif newSemanticFrame.Intent == 'INFORM_size':
            if not self.DialogFrame.cur_order.size:
                # self.DialogFrame.cur_order.size = newSemanticFrame.info
                self.status = 'CONFIRM'
                self.info = 'size'
                self.confirm_saved_info = newSemanticFrame.info
            else:
                self.status = 'REVISE'
                self.info = 'size'
        elif newSemanticFrame.Intent == 'INFORM_topping':
            if not self.DialogFrame.cur_order.topping:
                # self.DialogFrame.cur_order.size = newSemanticFrame.info
                self.status = 'CONFIRM'
                self.info = 'topping'
                self.confirm_saved_info = newSemanticFrame.info
            else:
                self.status = 'REVISE'
                self.info = 'topping'
        elif newSemanticFrame.Intent == 'INFORM_phone':
            if not self.DialogFrame.cur_order.phone:
                # self.DialogFrame.cur_order.phone = newSemanticFrame.info
                self.status = 'CONFIRM'
                self.info = 'phone'
                self.confirm_saved_info = newSemanticFrame.info
            else:
                self.status = 'REVISE'
                self.info = 'phone'
        elif newSemanticFrame.Intent == 'INFORM_delivery':
            if not self.DialogFrame.cur_order.delivery_type:
                # self.DialogFrame.cur_order.delivery_type = newSemanticFrame.info
                self.status = 'CONFIRM'
                self.info = 'delivery'
                self.confirm_saved_info = newSemanticFrame.info
            else:
                self.status = 'REVISE'
                self.info = 'delivery'
        elif newSemanticFrame.Intent == 'INFORM_address':
            if not self.DialogFrame.cur_order.address:
                # self.DialogFrame.cur_order.address = newSemanticFrame.info
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
            if self.info == 'reorder':
                if self.DialogFrame.cur_order.ifPhoneFilled() and self.DialogFrame.ifPhoneHasArchived():
                    self.DialogFrame.cur_order = self.DialogFrame.customer_info[self.DialogFrame.cur_order.phone]
                    self.status = 'REORDER_COMPLETE'
                else:
                    self.status = 'REORDER_FAIL'
                return
            else:
                self.DialogFrame.cur_order.fillAttribute(self.info, self.confirm_saved_info)
            self.status = 'NEXT_THING_TO_ASK'
            self.info = None
            self.confirm_saved_info = None
        else:
            self.status = 'HELLO'
            self.info = None
            self.confirm_saved_info = None

    def selectDialogAct(self):
        # decide on what dialog act to execute
        # by default, return a Hello dialog act
        dialogAct = DialogAct()

        if self.status == 'CONFIRM':
            dialogAct.DialogActType = DialogActTypes.CONFIRM
            dialogAct.info = (self.info, self.confirm_saved_info)
        elif self.status == 'NEXT_THING_TO_ASK':
            if self.DialogFrame.ifCurOrderOnlyPhone():
                if self.DialogFrame.cur_order.phone in self.DialogFrame.customer_info:
                    dialogAct.DialogActType = DialogActTypes.REORDER
                    dialogAct.info = self.DialogFrame.cur_order.phone
                    return dialogAct
            next_unfilled_item = self.DialogFrame.curUnfilledItem()
            if not next_unfilled_item:
                dialogAct.DialogActType = DialogActTypes.GOODBYE
                self.DialogFrame.addCurOrderToArchive()
            else:
                dialogAct.DialogActType = DialogActTypes.REQUEST
                dialogAct.info = next_unfilled_item
        elif self.status == 'CHECK':
            dialogAct.DialogActType = DialogActTypes.CHECK
            dialogAct.info = self.DialogFrame.cur_order.asDict()
        elif self.status == 'REVISE':
            dialogAct.DialogActType = DialogActTypes.REVISE
            dialogAct.info = self.info
        elif self.status == 'REORDER_COMPLETE':
            dialogAct.DialogActType = DialogActTypes.GOODBYE
        elif self.status == 'REORDER_FAIL':
            dialogAct.DialogActType = DialogActTypes.INFORM
        return dialogAct
