
def work_with_phonebook():
    choice = show_menu()
    phone_book = read_csv('phon.txt')

    while (choice < 8):
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            word = "фамилию"
            name = get_search_word(word)
            print(find_by_name(phone_book, name))
        elif choice == 3:
            word = "номер телефона"
            number = get_search_word(word)
            print(find_by_number(phone_book, number))
        elif choice == 4:
            user_data = get_new_user()
            add_user(phone_book, user_data)
            add_user_txt('phon.txt', phone_book)
        elif choice == 5:
            word = "имя нового файла"
            file_name = get_search_word(word)
            add_user_txt(file_name + ".txt", phone_book)
        elif choice == 6:
            user_data = get_del_user()
            del_user(phone_book, user_data)
            add_user_txt('phon.txt', phone_book)
        elif choice == 7:
            print("Работа программы завершена.")
        break
        # choice = show_menu()

def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Удалить данные (по Фамилии и Имени)\n"
          "7. Закончить работу")
    choice = int(input())
    return choice

def read_csv(filename: str) -> list:
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)

    return data

def print_result(phone_book):    
    for line in phone_book:
        print(line)

def get_search_word(word):
    return input(f"Введите {word}: ")

def get_new_user():
    fields = ["Фамилию", "Имя", "Телефон", "Описание"]
    newuser = []
   
    for i in fields:
        newuser.append(input(f"Введите {i}: "))
    
    return newuser

def get_del_user():
    fields = ["Фамилию", "Имя"]
    del_user = []
   
    for i in fields:
        del_user.append(input(f"Введите {i}: "))
    
    return del_user

def find_by_name(phone_book, name):
    for i in phone_book:
        if i["Фамилия"] == name:
            return i
    
    return "нет такой фамилии"

def find_by_number(phone_book, number):
    for i in phone_book:
        if i["Телефон"] == number:
            return i
    
    return "нет такого номера"

def add_user(phone_book, user_data):
    addStr = True

    for i in phone_book:
        # если такая фамилия и имя уже есть в базе то данные будут измененны
        # а не добавленны новые 
        if i["Фамилия"] == user_data[0] and i["Имя"] == user_data[1]:
            i["Телефон"] = user_data[2]
            i["Описание"] = user_data[3]
            addStr = False

    if addStr:
        fields = ["Фамилия", "Имя", "Телефон", "Описание"]
        record = dict(zip(fields, user_data))
        phone_book.append(record)

def del_user(phone_book, user_data):
    not_del = True
    for i in phone_book:
        if i["Фамилия"] == user_data[0] and i["Имя"] == user_data[1]:
            phone_book.remove(i)
            not_del = False
    
    if not_del:
        print("Нет такой Фамилии и Имени!")
        
# Создает новый или перезаписывает существующий файл
def add_user_txt(filename, phone_book):
    text = ""
    for l in phone_book:
        f1 = l["Фамилия"]
        f2 = l["Имя"]
        f3 = l["Телефон"]
        f4 = l["Описание"]
        text += f"{f1},{f2},{f3},{f4}\n"
    
    with open(filename, 'w', encoding='utf-8') as fin:
        fin.write(text)
            

work_with_phonebook()

