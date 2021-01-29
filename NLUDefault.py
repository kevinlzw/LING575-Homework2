from Order import Order
from SemanticFrame import SemanticFrame
from PizzaMenu import *
import re


class NLUDefault:

    def __init__(self):
        self.SemanticFrame = SemanticFrame()

    def resetSemanticFrame(self):
        self.SemanticFrame = SemanticFrame()

    def parse(self, inputStr):
        self.SemanticFrame.Domain = "pizza"
        inputStr = inputStr.lower()
        ifFilled = True
        if 'revise' in inputStr:
            self.SemanticFrame.Intent = 'REVISE_info'
            ifFoundAttribute = False
            for attribute in Order.allAttribute():
                if attribute in inputStr:
                    # TODO: split into 2 functions. One for revise and one for make orders.
                    # TODO: self.SemnaticFrame.info = (attribute, the value of the attribute)
                    # TODO: function called markOrder(pizza, hawaiian)
                    self.SemanticFrame.info = attribute
                    ifFoundAttribute = True
                    break
            if not ifFoundAttribute:
                raise NameError('The system cannot recognize the thing you want to revise.')
        elif 'pizza' in inputStr:
            self.SemanticFrame.Intent = "INFORM_pizza"
            added = False
            for pizza in PizzaMenu.pizzas:
                if pizza in inputStr:
                    self.SemanticFrame.info = pizza
                    added = True
                    break
            ifFilled &= added
        elif 'topping' in inputStr:
            self.SemanticFrame.Intent = "INFORM_topping"
            added = False
            for topping in PizzaMenu.Toppings:
                if topping in inputStr:
                    self.SemanticFrame.info = topping
                    added = True
                    break
            ifFilled &= added
        elif 'crust' in inputStr:
            self.SemanticFrame.Intent = "INFORM_crust"
            added = False
            for crust in PizzaMenu.crusts:
                if crust in inputStr:
                    self.SemanticFrame.info = crust
                    added = True
                    break
            ifFilled &= added
        elif 'size' in inputStr:
            self.SemanticFrame.Intent = "INFORM_size"
            for size in PizzaMenu.sizes:
                if size in inputStr:
                    self.SemanticFrame.info = size
                    ifFilled = True
                    break
        elif 'pick-up' in inputStr:
            self.SemanticFrame.Intent = "INFORM_pick_up"
            self.SemanticFrame.info = 'pick-up'
            ifFilled = True
        elif 'delivery' in inputStr:
            self.SemanticFrame.Intent = "INFORM_delivery"
            self.SemanticFrame.info = 'delivery'
            ifFilled = True
        elif re.compile("^[\dA-Z]{3}-[\dA-Z]{3}-[\dA-Z]{4}$", re.IGNORECASE).match(inputStr) is not None:
            self.SemanticFrame.Intent = 'INFORM_phone'
            self.SemanticFrame.info = inputStr
            ifFilled = True
        elif 'address' in inputStr:
            self.SemanticFrame.Intent = 'INFORM_address'
            self.SemanticFrame.info = inputStr
            ifFilled = True
        elif 'yes' in inputStr:
            self.SemanticFrame.Intent = 'CONFIRM_info'
        elif 'reorder' in inputStr:
            self.SemanticFrame.Intent = 'INFORM_reorder'
        elif 'check' in inputStr:
            self.SemanticFrame.Intent = 'CHECK_order'
        elif 'no' in inputStr:
            self.SemanticFrame.Intent = 'REJECT_info'
        if not ifFilled:
            raise NameError('The system cannot recognize your input, your option is not in the menu.')
        return self.SemanticFrame
