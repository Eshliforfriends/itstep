tasks = ['You have 2 tasks:\n 1. Visit library  2. Laundry',
        'You fave 2 tasks:\n 1. English lesson 2. Coffee with Mike',
        'You fave 2 tasks:\n 1. Cleaning in a room 2. Python exam',
        'You fave 1 task:\n 1. Play football',
        'You fave 1 tasks:\n 1. Read a book',
        'You have 2 task:\n 1. Visit parents  2. Go shopping',
        'You have 1 task:\n 1. Purchase grocery']
days = dict(monday = 'You have 2 tasks:\n 1. Visit library  2. Laundry',
            tuesday= 'You fave 2 tasks:\n 1. English lesson 2. Coffee with Mike',
            wednesday= 'You fave 2 tasks:\n 1. Cleaning in a room 2. Python exam',
            thursday = 'You fave 1 task:\n 1. Play football',
            friday = 'You fave 1 tasks:\n 1. Read a book',
            saturday = 'You have 2 task:\n 1. Visit parents  2. Go shopping',
            sunday = 'You have 1 task:\n 1. Purchase grocery')
smth = input('Enter a day: ')
error = 'Please enter appropriate format'
try:
    if type(int(smth)) == int:
        if int(smth) in range(1, 8):
            print(tasks[int(smth)-1])
        else:
            print(error)
except ValueError:
    if type(str(smth)) == str:
        if smth.lower() in days:
            print(days[smth.lower()])
        else:
            print(error)
