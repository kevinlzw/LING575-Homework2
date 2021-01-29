from DialogAct import DialogAct
from DialogActTypes import DialogActTypes


class NLGDefault:

    def __init__(self):
        # add whatever fields you want here
        self.Name = "NLGDefault"

    def generate(self, dialogAct):
        if dialogAct.DialogActType == DialogActTypes.HELLO:
            return "Welcome to the pizza ordering system. What pizza would you like?"
        if dialogAct.DialogActType == DialogActTypes.CONFIRM:
            return "Do you want a {} {}"
        if dialogAct.DialogActType == DialogActTypes.REQUEST:
            # use dialogAct.info to return the question.
        elif dialogAct.DialogActType == DialogActTypes.REVISE:
            # ask what new {info} do you want?
            '''
            if dialogAct.semantic_intent == 'INFORM_pizza':
                return "What toppings would you like?"
            elif dialogAct.semantic_intent == 'INFORM_topping':
                return "What size would you like?"
            elif dialogAct.semantic_intent == 'INFORM_size':
                return "What crust would you like?"
            elif dialogAct.semantic_intent == 'INFORM_crust':
                return "What sides would you like?"
            elif dialogAct.semantic_intent == 'INFORM_side':
                return 'What drinks would you like?'
            elif dialogAct.semantic_intent == 'INFORM_drink':
                return 'Do you want delivery service or pick-up?'
            elif dialogAct.semantic_intent == 'INFORM_delivery':
                return 'What is your address?'
            elif dialogAct.semantic_intent == 'INFORM_pick_up' or dialogAct.semantic_intent == 'INFORM_address':
                return "What's your name?"
            elif dialogAct.semantic_intent == 'INFORM_name':
                return "What's your phone number?"
            elif dialogAct.semantic_intent == 'INFORM_phone':
                return 'I have an order for a {} {} pizza on {} crust with {} toppings, {} side, {} drink for {}.'.format(
                    dialogAct.semantic_frame.Slots['size_type'], dialogAct.semantic_frame.Slots['pizza_type'],
                    dialogAct.semantic_frame.Slots['crust_type'], dialogAct.semantic_frame.Slots['topping_type'],
                    dialogAct.semantic_frame.Slots['side_type'], dialogAct.semantic_frame.Slots['drink_type'],
                    dialogAct.semantic_frame.Slots['delivery_type']
                )
            '''