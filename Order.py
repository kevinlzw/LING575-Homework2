class Order:

    def __init__(self, pizza=None, crust=None, size=None, topping=None):
        self.pizza = pizza
        self.crust = crust
        self.size = size
        self.topping = topping
        self.phone = None
        self.delivery_type = None
        self.address = None

    def fillAttribute(self, name, value):
        setattr(self, name, value)

    @staticmethod
    def allAttribute():
        return ['pizza', 'crust', 'size', 'topping', 'phone', 'delivery_type', 'address']

    def asDict(self):
        return {
            'pizza': self.pizza,
            'crust': self.crust,
            'size': self.size,
            'topping': self.topping,
            'phone': self.phone,
            'delivery_type': self.delivery_type,
            'address': self.address
        }

    def __str__(self):
        return '{} {} with {} crust and {} topping'.format(self.size, self.pizza, self.crust, self.topping)

    def ifOrderStarted(self):
        return not (
                not self.pizza and not self.crust and not self.size and not self.topping and not self.phone and not self.delivery_type and not self.address)

    def ifOnlyPhone(self):
        return self.phone and (
                not self.pizza and not self.crust and not self.size and not self.topping and not self.delivery_type and not self.address)

    def ifPhoneFilled(self):
        return self.phone is not None

    def NotFilledAttribute(self):
        if not self.pizza:
            return 'pizza'
        elif not self.topping:
            return 'topping'
        elif not self.crust:
            return 'crust'
        elif not self.size:
            return 'size'
        elif not self.delivery_type:
            return 'delivery_type'
        elif not self.address and self.delivery_type == 'delivery':
            return 'address'
        elif not self.phone:
            return 'phone'
        return
