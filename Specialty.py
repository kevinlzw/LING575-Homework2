from Order import Order


class SpecialtyPizza(Order):

    def __init__(self, pizzaType):
        # Order.__init__()
        self.pizza = pizzaType
        if pizzaType == 'hawaiian':
            self.crust = 'regular'
            self.size = 'medium'
            self.topping = 'pineapple'
        elif pizzaType == 'meat lovers':
            self.crust = 'thin'
            self.size = 'large'
            self.topping = 'sausage'
        elif pizzaType == 'veggie supreme':
            self.crust = 'regular'
            self.size = 'medium'
            self.topping = 'black olives'
        elif pizzaType == 'vegan':
            self.crust = 'gluten-free'
            self.size = 'large'
            self.topping = 'mushrooms'
        else:
            raise UserWarning("We do not offer that type of specialty pizza. ")
