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
            return "To confirm, you want a {} {}".format(dialogAct.info[1], dialogAct.info[0])
        if dialogAct.DialogActType == DialogActTypes.REQUEST:
            # TODO come up with a better string
            return "{}: ".format(dialogAct.info)
        elif dialogAct.DialogActType == DialogActTypes.REVISE:
            # ask what new {info} do you want?
            return "Okay, what is your new {}?".format(dialogAct.info)
