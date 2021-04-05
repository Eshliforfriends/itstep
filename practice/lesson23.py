class OrcArmy:
    def __init__(self, warrior_amount, damage_per_orc, warrior_health):
        self.warrior_amount =warrior_amount
        self.damage_per_orc = damage_per_orc
        self.warrior_health = warrior_health

    def __add__(self, other):
        total_warrior = self.warrior_amount + other.warrior_amount
        return total_warrior

    def average_orc(self,other):
        return (self.warrior_amount*self.damage_per_orc + other.warrior_amount*other.damage_per_orc)/(self.warrior_amount+other.warrior_amount)

    def average_health(self, other):
        return (self.warrior_amount * self.warrior_health + other.warrior_amount * other.warrior_health) / (self.warrior_amount+other.warrior_amount)

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
    print(f'Total warriors {war1 + war2}')
    print(f'Average damage per orc is {OrcArmy.average_orc(war1, war2)}')
    print(f'Average warrior health is {OrcArmy.average_health(war1, war2)}')
    print(f'Difference in warriors amount is {war1-war2}')


