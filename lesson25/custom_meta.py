class CustomMeta(type):
    def __new__(self, class_name,bases, attrs):
        attributes = {}
        for key, value in attrs.items():
            if not key.startswith('___'):
                attributes['method_'+ key] = value
                new_class_name = class_name.lower()
            else:
                attributes[key] = value
        return type(new_class_name,bases, attributes)

class Seasons(metaclass=CustomMeta):
    year = 2020
    season = 'Spring'

    def print_season(self):
        print(self.year)

if __name__ == '__main__':
    season = Seasons()
    print(season.method_season)
