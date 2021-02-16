set = 1
exit = 'stop'
exercises = [] # list of exercises number
while True:
    user_input = input(f"Insert number of exercises in set No.{set}, or 'stop' to excit. ")
    try:
        num = int(user_input)
        if num < 0:
            print('Enter positive integer number or stop. ')
        else:
            set += 1
            exercises.append(num)
    except ValueError:
        if user_input == exit:
            print(f'You have finished {set} sets')
            print(f'Total number of exercises done is {sum(exercises)} ' )
            print(f'Your best set contained {max(exercises)} exercises')
            print(f'You was pretty tired during the one set and made only {min(exercises)} exercises ')
            print(f'An average number of exercises this time is {sum(exercises) / len(exercises)} ')
            break
        else:
            print('Enter integer number or stop')