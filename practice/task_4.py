word_list = ['government', 'Lesson', 'Responsibility', 'other', 'Destiny']
print(map(lambda word: word if word.isupper() else None, word_list))