class OrcArmy:
    def __init__(self, warrior_amount, damage_per_orc, warrior_health):
        self.warrior_amount = warrior_amount
        self.damage_per_orc = damage_per_orc
        self.warrior_health = warrior_health

    def __str__(self):
        return f'Warrior amount is {self.warrior_amount}, Damage per orc is {self.damage_per_orc}, Average warrior health is {self.warrior_health}'


    def __add__(self, other):
        return OrcArmy(self.warrior_amount + other.warrior_amount,
                       (self.warrior_amount * self.damage_per_orc + other.warrior_amount * other.damage_per_orc) / (self.warrior_amount + other.warrior_amount),
                       (self.warrior_amount * self.warrior_health + other.warrior_amount * other.warrior_health)/(self.warrior_amount + other.warrior_amount))

    def __sub__(self, other):
        diff = self.warrior_amount - other.warrior_amount
        if self.warrior_amount > other.warrior_amount:
            return diff
        elif other.warrior_amount > self.warrior_amount:
            return None
        else:
            return None

    def receive_damage(self, damage: int):
        damaged_warriors = damage / self.warrior_health
        self.warrior_amount = self.warrior_amount - damaged_warriors
        return f'Warrior amount after damage is {damaged_warriors}'

if __name__ == '__main__':
    war1= OrcArmy(10,3,3)
    war2 = OrcArmy(10, 6, 3)
    damage = 18
    new_army = war1 + war2
    print(OrcArmy.receive_damage(war1,damage))




