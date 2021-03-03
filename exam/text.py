def text(user_text):
    user_text = user_text.split()
    for i in user_text:
        print(i[1])

user_text = 'The core of extensible programming is defining functions'

text(user_text)