"""
Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, 
разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го 
члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.

Ввод: 7 2 5
Вывод: 7 9 11 13 15
"""
# lst = input("введите первый элемент, разность и количество элементов, через пробел: ").split(" ")

# if len(lst) != 3:
#     print("введено не верное количество элементов")
# else:
#     firstEl = int(lst[0])
#     increment = int(lst[1])
#     countEl = int(lst[2])
    
#     for i in range(countEl):
#         print(firstEl)
#         firstEl += increment

"""
Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат 
заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
Вывод: [1, 9, 13, 14, 19]
"""
#lst = input("введите числа, через пробел: ").split(" ")
# ran = input("введите минимальное и максимальное значение, через пробел: ").split(" ")
# min = int(ran[0])
# max = int(ran[1])

# if min > max:
#     min = max
#     max = int(ran[0])

lst = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min = 7
max = 10
lst2 = []
for i in range(len(lst)):
    if int(lst[i]) >= min and int(lst[i]) <= max:
        lst2.append(i)

print(lst)
print(lst2)