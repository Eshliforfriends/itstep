class OrcArmy:
    def __init__(self, warrior_amount, damage_per_orc, warrior_health):
        self.warrior_amount =warrior_amount
        self.damage_per_orc = damage_per_orc
        self.warrior_health = warrior_health

    def __str__(self):
        return f'{self.warrior_amount}, {self.damage_per_orc}, {self.warrior_health}'


    def __add__(self, other):
        return OrcArmy(self.warrior_amount + other.warrior_amount,
                       (self.warrior_amount * self.damage_per_orc + other.warrior_amount * other.damage_per_orc) / (self.warrior_amount + other.warrior_amount),
                       (self.warrior_amount * self.warrior_health + other.warrior_amount * other.warrior_health)/(self.warrior_amount + other.warrior_amount))

    def __sub__(self, other):
        if self.warrior_amount > other.warrior_amount:
            return self.warrior_amount - other.warrior_amount
        elif other.warrior_amount > self.warrior_amount:
            return other.warrior_amount - self.warrior_amount
        else:
            return None


if __name__ == '__main__':
    war1= OrcArmy(4,3,2)
    war2 = OrcArmy(10, 6, 3)
    new_army = war1 + war2
    print(new_army)



