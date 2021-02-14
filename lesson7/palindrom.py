user_word = input('Enter any word:\n')
try:
    if user_word == user_word[::-1]:
        print(user_word, 'is palindrom')
    else:
        print(user_word, 'is not palindrom')
except ValueError:
    print('Error')
