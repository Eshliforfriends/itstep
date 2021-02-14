user_text = input('Enter text: \n')
for i, elem in enumerate(user_text.split('. ')):
    user_text = user_text.replace(elem, elem.capitalize())
print(user_text)
