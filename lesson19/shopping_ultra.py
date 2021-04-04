import json

def main():
    # shopping_list = [{
    #     'bread': 1.2,
    #     'milk': 1.6,
    #     'potato': 0.4,
    #     'sunflower oil': 2},
    #     {'meat': 2.4,
    #      'eggs': 0.4,
    #      'fish': 6.4
    #      }]

    with open('../lesson19/shopping_list.json', 'rb') as n:
        json_list = json.load(n)
    shopping_list = json_list

    def add_new(shopping_list):
        new_list = {}
        editing = True
        while editing:
            new_item = input('Enter new item: ')
            price = input('Enter item price: ')
            new_list[new_item] = float(price)
            if input('Enter Y to add new item to new list: ') !='Y':
                editing = False
        shopping_list.append(new_list)

    def delete_list(shopping_list):
        for i in shopping_list:
            print(i)
        try:
            delete_item = input('Enter number of list you want to delete: ')
            del shopping_list[int(delete_item) -1]
            print(shopping_list)
        except IndexError:
            print('Inapropriate number of list')


    def find_min(shopping_list):
        sum_list = []
        for item in shopping_list:
            x = sum(item.values())
            print(f'{item} value is {x}')
            sum_list.append(x)
            min_value = min(sum_list)
        print(f'Min value is {min_value}')

    def find_max(shopping_list):
        sum_list = []
        for item in shopping_list:
            x = sum(item.values())
            print(f'{item} value is {x}')
            sum_list.append(x)
            max_value = max(sum_list)
        print(f'Max value is {max_value}')

    keys = {'A': add_new,
            'B': delete_list,
            'C': find_min,
            'D': find_max
            }
    while True:
        user_input = input('Enter a key:\n'
                           'A to add new list\n'
                           'B to delete list\n'
                           'C to find min value list\n'
                           'D to find max value list \n'
                           'E to exit program\n'
                           )
        if user_input != 'E':
            if user_input in keys:
                print(keys[user_input](shopping_list))
            else:
                print('Enter appropriate key or D to exit')
        else:
            with open('../lesson19/shopping_list.json', 'w') as n:
                data_j = json.dump(shopping_list, n)
                print(data_j)
            break

if __name__ == '__main__':
    main()



