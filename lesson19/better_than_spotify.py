import os
import json

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


def main(write = False):
    func_music_library = []
    record = {
        "Назва групи": str,
        "Виконавці": [],
        "Дата заснування": int,
        "Альбоми": [],
    }

    try:
        with open('func_music_library.json', "rb") as n:
            func_music_library = json.load(n)
    except FileNotFoundError:
        with open('../lesson19/func_music_library.json', 'w') as f:
            data_j = json.dump(func_music_library, f)

    def add_record():
        editing = True
        name = input('Введіть назву групи: ')
        creation_date = input('Введіть дату створення групи: ' )
        participants = []
        albums = []
        x = "Y"
        while editing:
            participant = input('Введіть учасника групи: ')
            if input('Введіть "Y" щоб додати ще виконавців ') != x.lower():
                editing = False
            participants.append(participant)
        editing = True
        while editing:
            album = input('Введіть назву альбому: ')
            if input('Введіть "Y" щоб додати ще альбоми ') != x.lower():
                editing = False
            albums.append(album)
        record["Назва групи"] = name
        record["Виконавці"] = participants
        record["Дата заснування"] = creation_date
        record["Альбоми"] = albums
        func_music_library.append(record)

    def change_record():
        for n, i in enumerate(func_music_library):
            print(n + 1, i)
        def change_name():
            name = input('Введіть назву групи: ')
            func_music_library[int(number)-1]["Назва групи"] = name
        def change_participants():
            editing = True
            participants =[]
            x ='Y'
            while editing:
                participant = input('Введіть учасника групи: ')
                if input('Введіть "Y" щоб додати ще виконавців ') != x.lower():
                    editing = False
                participants.append(participant)
            func_music_library[int(number)-1]["Виконавці"] = participants
        def change_creation_date():
            creation_date = input('Введіть дату створення групи: ')
            func_music_library[int(number)-1]["Дата заснування"] = creation_date
        def change_albums():
            editing = True
            albums =[]
            x ='Y'
            while editing:
                album = input('Введіть учасника групи: ')
                if input('Введіть "Y" щоб додати ще виконавців ') != x.lower():
                    editing = False
                albums.append(album)
            func_music_library[int(number)-1]["Альбоми"] = albums

        keys = {
            "k": change_name,
            "m": change_participants,
            "l": change_creation_date,
            "n": change_albums
        }
        key = ''
        try:
            number = input('Введіть номер запису для зміни: ')
            if 0 < int(number) <= len(func_music_library):
                print(func_music_library[int(number) - 1])
                while key != 'e':
                    key = input('Введіть \n'
                            'K щоб змінити назву групи \n'
                            'L щоб змінити дату альбому \n'
                            'M щоб змінити учасників \n'
                            'N щоб змінити альбом \n'
                            'O щоб закінчити зміни\n')
                    if key.lower() in keys:
                        keys[key.lower()]()
                    elif key.lower() == 'o':
                        print('Закінчення роботи')
                        break
                    else:
                        print('Помилка введення')
        except ValueError:
            print('Error')


    def del_record():
        for n, i in enumerate(func_music_library):
            print(n + 1, i)
        number = input('Введіть номер запису для видалення: ')
        if 0 < int(number) <= len(func_music_library):
            print(func_music_library[int(number) - 1])
            func_music_library.pop(int(number) -1)
            print(func_music_library)
        else:
            print('Помилка введення')

    def view_the_list():
        if func_music_library:
            print('\nВаш список записів: ')
            for n, i in enumerate(func_music_library):
                print('\nЗапис номер {}: '.format(n + 1))
                for j in i:
                    print(func_music_library[n][j])
                    # print(j + ': ', end=' ')
                    # print(*func_music_library[n][j], sep=', ', end='.\n')
        else:
            print("\nСписок записів порожній")


    box = {
        "a": add_record,
        "c": change_record,
        "d": del_record,
        "v": view_the_list
    }

    key = ''
    while key != 'e':
        print("Музична бібліотека")
        print("Введіть A для додавання нового запису")
        print("Введіть C для зміни запису")
        print("Введіть D для видалення запису")
        print("Введіть V для огляду запису")
        print("Введіть E для закінчення")
        key = input("Ви вводите: ")
        if key.lower() in box:
            box[key.lower()]()
        elif key.lower() == 'e':
            with open('../lesson19/func_music_library.json', 'w') as f:
                data_j = json.dump(func_music_library, f)
            print('Закінчення роботи з файлом')
            break
        else:
            print('Помилка введення')


if __name__ == '__main__':
    main()