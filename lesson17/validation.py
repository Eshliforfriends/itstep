import re

error= 'Enter 1 or 2'
error_input = 'Enter appropriate format'
def users():
    users_data = []
    new_user = {'Surname': 'surname',
                'Name': 'name',
                'Position': 'position',
                'Tel. number': 'number',
                'Email': 'email'
                }
    def add_new(data):
        while True:
            surname_input = input('Enter new user surname\n')
            sur = re.findall('.', surname_input)
            if sur[0].isupper():
                new_user['Surname'] = surname_input
                break
            else:
                print(error_input)
        while True:
            name_input = input('Enter new user name\n')
            nam = re.findall('.', name_input)
            if nam[0].isupper():
                new_user['Name'] = name_input
                break
            else:
                print(error_input)

        while True:
            position_input = input('Enter user"s position\n')
            if type(position_input) == str:
                new_user['Position'] = position_input
                break
            else:
                print(error_input)

        while True:
            number_input = input('Enter user"s tel. number\n')
            if re.match("[+]{1}[3]{1}[8]{1}[0-9]{10}", number_input) and len(number_input) == 13:
                new_user['Tel. number'] = number_input
                break
            else:
                print(error_input)

        while True:
            email_input = input('Enter user"s email\n')
            if re.findall(r'\w@\w.[a-zA-Z]', email_input):
                new_user['Email'] = email_input
                break
            else:
                print(error_input)

        users_data.append(new_user)
        print(users_data)

    def view_all(data):
        return data

    while True:
        user_input = input('Enter 1 to add new user, 2 to view all added users and 3 to exit\n')
        if user_input != 3:
            if user_input == 1:
                print(add_new(users_data))
            elif user_input == 2:
                print(view_all(users_data))
            else:
                print(error)
        else:
            break
            print('Process is finished')


print(users())






