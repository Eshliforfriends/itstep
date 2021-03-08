import random
issue_year = []
books_names = ['Once upon a time', 'Great book', 'Exactly what you want to read', 'For children', 'Fairytale']
def library(books_names, issue_year):
    issue_year = random.sample(range(1880, 2021), len(books_names))
    library = list(zip(books_names, issue_year))

    def sort_year(books_names, issue_year):
        library.sort(key=lambda x: x[1])
        books_names1, issue_year1 = zip(*library)
        for a, b in zip(issue_year1, books_names1):
            print(f' Year: {a}; Book title: {b}')

    def books_list(books_names, issue_year):
        library.sort(key=lambda x: x[0])
        books_names2, issue_year2 = zip(*library)
        for a, b in zip(books_names2, issue_year2):
            print(f' Book title: {a}; Year: {b}')

    keys = {'Y': sort_year,
            'L': books_list
            }
    while True:
        user_input = input('Please enter the key: \n'
                       'Y to sort by issue year \n'
                       'L to see list of books with issue year, and \n'
                       'E to exit\n'
                           '')
        if user_input != 'E':
            if user_input in keys:
                print(keys[user_input](books_names, issue_year))
            else:
                print('Enter appropriate key or E to exit')
        else:
            print('End')
            break

library(books_names, issue_year)

