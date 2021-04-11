class Army():
    def __init__(self, warrior_amount, damage_per_orc, warrior_health, shield):
        self.warrior_amount = warrior_amount
        self.damage_per_orc = damage_per_orc
        self.warrior_health = warrior_health
        self.shield = shield

    def __str__(self):
        return f'Warrior amount is {self.warrior_amount}, Damage per orc is {self.damage_per_orc}, Average warrior health is {self.warrior_health}'


    def __add__(self, other):
        return Army(self.warrior_amount + other.warrior_amount,
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

class OrcArmy(Army):
    def receive_damage(self, damage: int):
        damaged_warriors = damage / self.warrior_health
        if self.warrior_amount > damaged_warriors:
            self.warrior_amount = self.warrior_amount - damaged_warriors
        else:
            return None
        return f'Warrior amount after damage is {damaged_warriors}'

class ElfArmy(Army):
    def receive_damage(self, damage: int):
        damage_upd = damage - self.shield
        damaged_warriors = damage_upd / self.warrior_health
        if self.warrior_amount > damaged_warriors:
            self.warrior_amount = self.warrior_amount - damaged_warriors
        else:
            return None
        self.warrior_amount = self.warrior_amount - damaged_warriors
        return f'Warrior amount after damage is {damaged_warriors}'

if __name__ == '__main__':
    warrior_orc= OrcArmy(9, 2, 6,0)
    warrior_elf= OrcArmy(7, 1, 3,2)
    damage = 18
    print(warrior_orc.receive_damage(damage))
    print(warrior_elf.receive_damage(damage))


