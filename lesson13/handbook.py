import random
id_codes = []
phone_numbers = []
users = ['John', 'Mike', 'Olivia', 'Peter', 'Charlie', 'Bob']
def handbook(users, id_codes, phone_numbers):
    id_codes = random.sample(range(1000, 9999), len(users))
    phone_numbers = random.sample(range(1000000, 9999999), len(users))
    handbook = list(zip(users, id_codes, phone_numbers))
    def sort_id(users, id_codes, phone_numbers):
        id_codes.sort()
        return id_codes

    def sort_phone(users, id_codes, phone_numbers):
        phone_numbers.sort()
        return phone_numbers

    def list_all(users, id_codes, phone_numbers):
        handbook.sort(key=lambda x: x[0])
        return handbook

    keys = {'C': sort_id,
            'N': sort_phone,
            'L': list_all
            }
    while True:
        user_input = input('Please enter the key: \n'
                       'C to sort by ID codes \n'
                       'N to sort by phone numbers \n'
                       'L to see list of users with id and phone number, and \n'
                       'E to exit\n'
                           '')
        if user_input != 'E':
            if user_input in keys:
                print(keys[user_input](users, id_codes, phone_numbers))
            else:
                print('Enter appropriate key or E to exit')
        else:
            print('End')
            break

handbook(users,id_codes, phone_numbers)

