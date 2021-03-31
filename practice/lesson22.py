class CloneTrooper:
    id = None
    def __init__(self, id):
        self._id = id
    def say_name(self):
        print(f'I am a trooper CT-{self._id}')
    def name(self):
        print(f'CT-{self._id}')
    def fight(self):
        print(f'Trooper CT-{self._id} start fighting')



standard_trooper = CloneTrooper(1437)
standard_trooper.say_name()
standard_trooper.name()
standard_trooper.fight()
