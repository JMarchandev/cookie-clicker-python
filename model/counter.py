class Counter:

    def __init__(self, start_value):
        self.counter = start_value
        self.bonus = 1
        self.bonus_price = 10

    def get_value(self):
        return self.counter

    def increment(self):
        self.counter += (1 * self.bonus)

    def get_bonus(self):
        return self.bonus

    def set_bonus(self, new_bonus):
        self.counter -= self.bonus_price
        self.bonus = new_bonus
        self.bonus_price = round(self.bonus_price + (new_bonus * 10))

    def get_bonus_price(self):
        return self.bonus_price
