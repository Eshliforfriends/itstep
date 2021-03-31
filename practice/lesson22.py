class CloneTrooper:
    name = None
    type_id = 'CT'
    def __init__(self, identificator):
        self.name = f'{CloneTrooper.type_id}-{identificator}'
        self._id = identificator
    def say_name(self):
        print(f'I am a trooper {self.name }')
    def fight(self):
        print(f'Trooper {self.name } start fighting')

class StormTrooper(CloneTrooper):
    CloneTrooper.type_id = 'ST'
    @staticmethod
    def type():
        return 'Trooper type -> StormTrooper'

print(StormTrooper.type())
standard_trooper = CloneTrooper(1437)
standard_trooper.say_name()
print(standard_trooper.name)
standard_trooper.fight()

