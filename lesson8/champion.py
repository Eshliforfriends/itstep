set = 1
exit = 'stop'
excercises = [] # list of excercises number
while True:
    user_input = input(f"Insert number of excercises in set No.{set}, or stop to excit. ")
    try:
        num = int(user_input)
        if num < 0:
            print('Enter positive integer number or stop. ')
        else:
            set += 1
            excercises.append(num)
    except ValueError:
        if user_input == exit:
            print(set)
            print(sum(excercises))
            print(max(excercises))
            print(min(excercises))
            print(sum(excercises) / len(excercises))
            break
        else:
            print('Enter integer number or stop')