from Order import Order
from SemanticFrame import SemanticFrame
from PizzaMenu import *
import re


class NLUDefault:

    def __init__(self):
        self.SemanticFrame = SemanticFrame()

    def resetSemanticFrame(self):
        self.SemanticFrame = SemanticFrame()

    def parse(self, input_str):
        self.SemanticFrame.Domain = "pizza"
        input_str = input_str.lower()
        if_filled = True
        if 'cancel' in input_str:
            self.SemanticFrame.Intent = 'CANCEL_order'
        elif 'repeat' in input_str:
            self.SemanticFrame.Intent = 'REPEAT_order'
        elif 'start-over' in input_str:
            self.SemanticFrame.Intent = 'START_over'
        elif 'revise' in input_str:
            self.SemanticFrame.Intent = 'REVISE_info'
            ifFoundAttribute = False
            for attribute in Order.allAttribute():
                if attribute in input_str:
                    self.SemanticFrame.info = attribute
                    ifFoundAttribute = True
                    break
            if not ifFoundAttribute:
                raise NameError('The system cannot recognize the thing you want to revise.')
        elif 'pizza' in input_str:
            self.SemanticFrame.Intent = "INFORM_pizza"
            added = False
            specialty = False
            for pizza in PizzaMenu.specialty:
                if pizza in input_str:
                    self.SemanticFrame.info = pizza
                    added = True
                    specialty = True
                    self.SemanticFrame.Intent = "INFORM_specialty"
                    break
            if not specialty:
                for pizza in PizzaMenu.pizzas:
                    if pizza in input_str:
                        self.SemanticFrame.info = pizza
                        added = True
                        break
            if_filled &= added
        elif 'topping' in input_str:
            self.SemanticFrame.Intent = "INFORM_topping"
            added = False
            for topping in PizzaMenu.Toppings:
                if topping in input_str:
                    self.SemanticFrame.info = topping
                    added = True
                    break
            if_filled &= added
        elif 'crust' in input_str:
            self.SemanticFrame.Intent = "INFORM_crust"
            added = False
            for crust in PizzaMenu.crusts:
                if crust in input_str:
                    self.SemanticFrame.info = crust
                    added = True
                    break
            if_filled &= added
        elif 'size' in input_str:
            self.SemanticFrame.Intent = "INFORM_size"
            added = False
            for size in PizzaMenu.sizes:
                if size in input_str:
                    self.SemanticFrame.info = size
                    if_filled = True
                    added = True
                    break
            if_filled &= added
        elif 'pick-up' in input_str:
            self.SemanticFrame.Intent = "INFORM_pick_up"
            self.SemanticFrame.info = 'pick-up'
        elif 'delivery' in input_str:
            self.SemanticFrame.Intent = "INFORM_delivery"
            self.SemanticFrame.info = 'delivery'
        elif re.compile("^.*[\dA-Z]{3}-[\dA-Z]{3}-[\dA-Z]{4}.*$", re.IGNORECASE).match(input_str) is not None:
            self.SemanticFrame.Intent = 'INFORM_phone'
            self.SemanticFrame.info = re.findall('[\dA-Z]{3}-[\dA-Z]{3}-[\dA-Z]{4}', input_str)[0]
        elif 'address' in input_str:
            self.SemanticFrame.Intent = 'INFORM_address'
            self.SemanticFrame.info = input_str.replace('address', '')
        elif 'yes' in input_str:
            self.SemanticFrame.Intent = 'CONFIRM_info'
        elif 'reorder' in input_str:
            self.SemanticFrame.Intent = 'INFORM_reorder'
        elif 'check' in input_str:
            self.SemanticFrame.Intent = 'CHECK_order'
        elif 'no' in input_str:
            self.SemanticFrame.Intent = 'REJECT_info'
        if not if_filled:
            self.SemanticFrame.Intent = 'UNKNOWN'
        cur_semantic_frame = self.SemanticFrame
        self.resetSemanticFrame()
        return cur_semantic_frame
