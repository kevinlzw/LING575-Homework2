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
        ifFilled = False
        if 'pizza' in inputStr:
            self.SemanticFrame.Intent = "INFORM_pizza"
            for pizza in PizzaMenu.pizzas:
                if pizza in inputStr:
                    self.SemanticFrame.info = pizza
                    ifFilled = True
                    break
        elif 'topping' in inputStr:
            self.SemanticFrame.Intent = "INFORM_topping"
            for topping in PizzaMenu.Toppings:
                if topping in inputStr:
                    self.SemanticFrame.info = topping
                    ifFilled = True
                    break
        elif 'crust' in inputStr:
            self.SemanticFrame.Intent = "INFORM_crust"
            for crust in PizzaMenu.crusts:
                if crust in inputStr:
                    self.SemanticFrame.info = crust
                    ifFilled = True
                    break
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
        elif 'revise' in inputStr:
            self.SemanticFrame.Intent = 'REVISE_info'
            ifFoundAttribute = False
            for attribute in Order.allAttribute():
                if attribute in inputStr:
                    self.SemanticFrame.info = attribute
                    ifFoundAttribute = True
                    break
            if not ifFoundAttribute:
                raise NameError('The system cannot recognize the thing you want to revise.')
        if not ifFilled:
            raise NameError('The system cannot recognize your input, your option is not in the menu.')
        return self.SemanticFrame
