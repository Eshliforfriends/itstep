class CloneTrooper:
    name = None
    type_id = 'CT'
    def __init__(self, identificator):
        self.name = f'CT-{identificator}'
        self._id = identificator
    def say_name(self):
        print(f'I am a trooper {CloneTrooper.type_id}-{self.name }')
    def fight(self):
        print(f'Trooper {CloneTrooper.type_id}-{self.name } start fighting')



standard_trooper = CloneTrooper(1437)
standard_trooper.say_name()
print(standard_trooper.name)
standard_trooper.fight()
