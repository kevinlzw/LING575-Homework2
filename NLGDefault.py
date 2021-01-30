from DialogAct import DialogAct
from DialogActTypes import DialogActTypes

confirm_phrase = {
    'specialty': 'To confirm, you want a {} specialy pizza',
    'pizza': 'To confirm, you want a {} pizza',
    'topping': 'To confirm, your topping for your pizza is {}',
    'crust': 'To confirm, your crust selection is {} crust',
    'size': 'To confirm, your pizza size is {} size',
    'delivery_type': 'To confirm, you want a {} service',
    'phone': 'To confirm, your phone number is {}',
    'address': 'To confirm, your address is {}'
}

request_phrase = {
    'pizza': 'What pizza would you like?',
    'topping': 'What topping do you want to add to your pizza?',
    'crust': 'What crust for your pizza?',
    'size': 'Which size do you want? We have small, medium and large.',
    'delivery_type': 'Do you want a delivery or pick-up?',
    'phone': 'What is your phone number?',
    'address': 'Can you give me an address for your delivery?'
}


class NLGDefault:

    def __init__(self):
        # add whatever fields you want here
        self.Name = "NLGDefault"
        self.prev = None

    def generate(self, dialogAct):
        if dialogAct.DialogActType == DialogActTypes.REPEAT:
            return self.prev
        if dialogAct.DialogActType == DialogActTypes.CONFIRM:
            self.prev = confirm_phrase[dialogAct.info[0]].format(dialogAct.info[1])
            return self.prev
        if dialogAct.DialogActType == DialogActTypes.REQUEST:
            # TODO come up with a better string
            if dialogAct.info[1]:
                self.prev = dialogAct.info[1] + request_phrase[dialogAct.info[0]]
                return self.prev
            self.prev = request_phrase[dialogAct.info[0]]
            return self.prev
        elif dialogAct.DialogActType == DialogActTypes.REVISE:
            # ask what new {info} do you want?
            self.prev = "Okay, what is your new {}?".format(dialogAct.info)
            return self.prev
        elif dialogAct.DialogActType == DialogActTypes.UNDEFINED:
            self.prev = "I don't understand, can you say it again?"
            return self.prev
        elif dialogAct.DialogActType == DialogActTypes.GOODBYE:
            self.prev = "Thank you, your order for a {} pizza is on the way".format(dialogAct.info)
            return self.prev
        elif dialogAct.DialogActType == DialogActTypes.REORDER:
            self.prev = "Please type in your phone number."
            return self.prev
        elif dialogAct.DialogActType == DialogActTypes.RETURN_CHECK:
            self.prev = "Great, thank you. I see there is an order for a {} pizza currently on its way".format(dialogAct.info)
            return self.prev