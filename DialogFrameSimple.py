from Order import Order


class DialogFrameSimple:

    def __init__(self):
        # For Q3
        self.FrameName = "DialogFrameSimple"
        self.customer_info = {}
        self.cur_order = Order()

    def ifPhoneHasArchived(self):
        return self.cur_order.phone in self.customer_info

    def ifCurOrderStarted(self):
        return self.cur_order.ifOrderStarted()

    def curUnfilledItem(self):
        return self.cur_order.NotFilledAttribute()

    def ifCurOrderOnlyPhone(self):
        return self.ifCurOrderOnlyPhone()

    def addCurOrderToArchive(self):
        self.customer_info[self.cur_order.phone] = self.cur_order
        self.cur_order = Order()