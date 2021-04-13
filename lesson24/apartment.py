class Apartment:
    def __init__(self, number, people, floor, area):
        self.number = number
        self.people = people
        self.floor = floor
        self.area = area

    @property
    def numbers(self, value):
        return self._number

    @numbers.setter
    def set_number(self, value):
        if value is not int:
            print('Number should be integer')
        self._number = value

    @property
    def peoples(self):
        return self.people

    @peoples.setter
    def set_people(self, value):
        if value <0:
            raise ValueError('Number must be greater than zero')
        self.people = value

    @property
    def floors(self):
        return self.floor

    @floors.setter
    def set_floor(self, value):
        if value <=0:
            raise ValueError('Number of floor must be greater than zero')
        self.floor = value


    @property
    def areas(self):
        return self.area

    @areas.setter
    def set_area(self, value):
        if value <=0:
            raise ValueError('Area must be greater than zero')
        self.area = value




a = Apartment(45, 2, 3, 55)
a.set_floor= -8






