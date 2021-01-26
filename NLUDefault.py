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
        if 'pizza' in inputStr:
            self.SemanticFrame.Intent = "INFORM_pizza"
            for pizza in PizzaMenu.pizzas:
                if pizza in inputStr:
                    self.SemanticFrame.Slots["pizza_type"] = pizza
                    break
        elif 'topping' in inputStr:
            self.SemanticFrame.Intent = "INFORM_topping"
            for topping in PizzaMenu.Toppings:
                if topping in inputStr:
                    self.SemanticFrame.Slots["topping_type"] = topping
                    break
        elif 'crust' in inputStr:
            self.SemanticFrame.Intent = "INFORM_crust"
            for crust in PizzaMenu.crusts:
                if crust in inputStr:
                    self.SemanticFrame.Slots["crust_type"] = crust
                    break
        elif 'size' in inputStr:
            self.SemanticFrame.Intent = "INFORM_size"
            for size in PizzaMenu.sizes:
                if size in inputStr:
                    self.SemanticFrame.Slots["size_type"] = size
                    break
        elif 'side' in inputStr:
            self.SemanticFrame.Intent = "INFORM_side"
            for side in PizzaMenu.sides:
                if side in inputStr:
                    self.SemanticFrame.Slots["side_type"] = side
                    break
        elif 'drink' in inputStr:
            self.SemanticFrame.Intent = "INFORM_drinks"
            for drink in PizzaMenu.drinks:
                if drink in inputStr:
                    self.SemanticFrame.Slots["drink_type"] = drink
                    break
        elif 'pick-up' in inputStr:
            self.SemanticFrame.Intent = "INFORM_pick_up"
            if "delivery_type" not in self.SemanticFrame.Slots:
                self.SemanticFrame.Slots["delivery_type"] = 'pick-up'
        elif 'delivery' in inputStr:
            self.SemanticFrame.Intent = "INFORM_delivery"
            if "delivery_type" not in self.SemanticFrame.Slots:
                self.SemanticFrame.Slots["delivery_type"] = 'delivery'
        elif re.compile("^[\dA-Z]{3}-[\dA-Z]{3}-[\dA-Z]{4}$", re.IGNORECASE).match(inputStr) is not None:
            self.SemanticFrame.Intent = 'INFORM_phone'
            self.SemanticFrame.Slots["phone_type"] = inputStr
        elif 'address' in inputStr:
            self.SemanticFrame.Intent = 'INFORM_address'
            self.SemanticFrame.Slots['address'] = inputStr
        elif 'name' in inputStr:
            self.SemanticFrame.Intent = 'INFORM_name'
            self.SemanticFrame.Slots['name'] = inputStr
        else:
            self.SemanticFrame.Intent = 'WRONG'
        return self.SemanticFrame
