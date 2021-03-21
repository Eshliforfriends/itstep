diary = {
    ('1','monday'): ['Visit library', 'Laundry'],
    ('2', 'tuesday'):['English lesson', 'Coffee with Mike'],
    ('3', 'wednesday'): ['Cleaning in a room','Python exam'],
    ('4', 'thursday'): ['Play football'],
    ('5', 'friday'): ['Read a book'],
    ('6', 'saturday'): ['Visit parents', 'Go shopping'],
    ('7', 'sunday'): ['Purchase grocery']
}

def diary_func(diary):
    def view_tasks(diary):
        day = input('Enter day in word or number format (e.g. `Monday or 1):\n')
        for item in diary.keys():
            if day.lower() in item:
                return diary[item]

    def add_tasks(diary):
        new_day = input('Enter a day:\n')
        new_task = input('Enter new tasks for the day:\n')
        for item in diary.keys():
            if new_day.lower() in item:
                diary[item].append(new_task)
                return diary[item]

    def delete_tasks(diary):
        day_to_change = input('Enter a day to change:\n')
        for item in diary.keys():
            if day_to_change.lower() in item:
                print(diary[item])
                task_to_delete = input('Enter number of task you want to delete :\n')
                del diary[item][int(task_to_delete) -1]
                return diary[item]

    keys = {'A': view_tasks,
            'B': add_tasks,
            'C': delete_tasks
            }
    while True:
        user_input = input('Enter a key:\n'
                     'A to view tasks for the day\n'
                     'B to add new tasks\n'
                     'C to delete tasks\n'
                     'D to exit program\n'
                     )
        if user_input != 'D':
            if user_input in keys:
                print(keys[user_input](diary))
            else:
                print('Enter appropriate key or D to exit')
        else:
            break

print(diary_func(diary))


