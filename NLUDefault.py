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
                    if "pizza_type" in self.SemanticFrame.Slots:
                        break
                    self.SemanticFrame.Slots["pizza_type"] = pizza
                    ifFilled = True
                    break
        elif 'topping' in inputStr:
            self.SemanticFrame.Intent = "INFORM_topping"
            for topping in PizzaMenu.Toppings:
                if topping in inputStr:
                    if "topping_type" in self.SemanticFrame.Slots:
                        break
                    self.SemanticFrame.Slots["topping_type"] = topping
                    ifFilled = True
                    break
        elif 'crust' in inputStr:
            self.SemanticFrame.Intent = "INFORM_crust"
            for crust in PizzaMenu.crusts:
                if crust in inputStr:
                    if "crust_type" in self.SemanticFrame.Slots:
                        break
                    self.SemanticFrame.Slots["crust_type"] = crust
                    ifFilled = True
                    break
        elif 'size' in inputStr:
            self.SemanticFrame.Intent = "INFORM_size"
            for size in PizzaMenu.sizes:
                if size in inputStr:
                    if "size_type" in self.SemanticFrame.Slots:
                        break
                    self.SemanticFrame.Slots["size_type"] = size
                    ifFilled = True
                    break
        elif 'side' in inputStr:
            self.SemanticFrame.Intent = "INFORM_side"
            for side in PizzaMenu.sides:
                if side in inputStr:
                    if "side_type" in self.SemanticFrame.Slots:
                        break
                    self.SemanticFrame.Slots["side_type"] = side
                    ifFilled = True
                    break
        elif 'drink' in inputStr:
            self.SemanticFrame.Intent = "INFORM_drink"
            for drink in PizzaMenu.drinks:
                if drink in inputStr:
                    if "drink_type" in self.SemanticFrame.Slots:
                        break
                    self.SemanticFrame.Slots["drink_type"] = drink
                    ifFilled = True
                    break
        elif 'pick-up' in inputStr:
            self.SemanticFrame.Intent = "INFORM_pick_up"
            if "delivery_type" not in self.SemanticFrame.Slots:
                self.SemanticFrame.Slots["delivery_type"] = 'pick-up'
                ifFilled = True
        elif 'delivery' in inputStr:
            self.SemanticFrame.Intent = "INFORM_delivery"
            if "delivery_type" not in self.SemanticFrame.Slots:
                self.SemanticFrame.Slots["delivery_type"] = 'delivery'
                ifFilled = True
        elif re.compile("^[\dA-Z]{3}-[\dA-Z]{3}-[\dA-Z]{4}$", re.IGNORECASE).match(inputStr) is not None:
            if "phone_type" not in self.SemanticFrame.Slots:
                self.SemanticFrame.Intent = 'INFORM_phone'
                self.SemanticFrame.Slots["phone_type"] = inputStr
                ifFilled = True
        elif 'address' in inputStr:
            if "address" not in self.SemanticFrame.Slots:
                self.SemanticFrame.Intent = 'INFORM_address'
                self.SemanticFrame.Slots['address'] = inputStr
                ifFilled = True
        elif 'name' in inputStr:
            self.SemanticFrame.Intent = 'INFORM_name'
            if "address" not in self.SemanticFrame.Slots:
                self.SemanticFrame.Slots['name'] = inputStr
                ifFilled = True
        else:
            self.SemanticFrame.Intent = 'WRONG'
        if not ifFilled:
            raise NameError('The system cannot recognize your input, your option is not in the menu.')
        return self.SemanticFrame
