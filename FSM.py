from DialogAct import DialogAct
from DialogActTypes import DialogActTypes

class FSM:

    def __init__(self, NLU, NLG):
        # add whatever you want here
        self.Name = "FSM DM"
        self.curState = None
        self.NLU = NLU
        self.NLG = NLG
        self.transitions = {
            'pizza': {'INFORM_pizza': 'topping'},
            'topping': {'INFORM_topping': 'size'},
            'size': {'INFORM_size': 'crust'},
            'crust': {'INFORM_crust': 'side'},
            'side': {'INFORM_side': 'drinks'},
            'drinks': {'INFORM_drinks': 'delivery_type'},
            'delivery_type': {'INFORM_delivery': 'address', 'INFORM_pick_up': 'name'},
            'address': {'INFORM_address': 'name'},
            'name': {'INFORM_name': 'phone'},
            'phone': {'INFORM_phone': 'end'}
        }
        self.endState = 'end'

    def execute(self, inputStr):
        if not self.curState or self.curState == self.endState:
            if self.curState == self.endState:
                self.NLU.resetSemanticFrame()
            self.curState = 'pizza'
            return self.NLG.generate(DialogAct(DialogActTypes.HELLO))
        semantic_frame = self.NLU.parse(inputStr)
        if semantic_frame.Intent in self.transitions[self.curState]:
            self.curState = self.transitions[self.curState][semantic_frame.Intent]
            dialogAct = DialogAct(DialogActTypes.REQUEST, semantic_frame)
            return self.NLG.generate(dialogAct)
        else:
            return self.NLG.generate(DialogAct(DialogActTypes.CONFIRM))
