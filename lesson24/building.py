class Building:
    def __init__(self, name, floors, height, area, city):
        self._name = name
        self.floors = floors
        self.height = height
        self.area = area
        self.city = city

    @property
    def name(self, value):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) > 25:
            print('Name can not exceed 25 characters')
        self._name = value

    @property
    def floor(self):
        return self.floors

    @floor.setter
    def floor(self, value):
        if value <=0:
            raise ValueError('Floors number must be greater than zero')
        self.floors = value

    @property
    def areas(self):
        return self.area

    @areas.setter
    def areas(self, value):
        if value <=0:
            raise ValueError('Area must be greater than zero')
        self.area = value

    @property
    def cities(self):
        return self.city



b = Building('Hotel #1', 10, 400, 500, 'Kyiv')
# b.floor = 0
b.floor






