'''
9. По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N 
(произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while
'''

# n = int(input("Введите число: "))
# if n < 0:
#     print ("введите число больше нуля")
# else:
#     i = 1
#     rez = 1
#     while i <= n:
#         rez *= i
#         i += 1
#     print(rez)

'''
Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, 
то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

0, 1, 1, 2, 3, 5, 8, 
'''

# a = int(input("Введите число: "))
# if a < 1:
#     print("введите число больше 1")
# else:
#     i = 1
#     f = 0
#     old = 0
#     new = 1
#     flag = i != a
    
#     while flag:
#         i += 1
#         f = old + new
#         if f == a:
#             flag = False
#         elif f > a:
#             i = -1
#             flag = False
#         else:
#             old = new
#             new = f

# print(i)

'''

1. Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная 
оттепель за всю историю наблюдений за погодой. Они обратились к синоптикам, а те, в свою очередь, 
занялись исследованиями статистики за прошлые годы. Их интересует, сколько дней длилась самая 
длинная оттепель. Оттепелью они называют период, в который среднесуточная температура ежедневно 
превышала 0 градусов Цельсия. Напишите программу, помогающую синоптикам в работе.

Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). 
В следующих строках располагается N целых чисел.

Каждое число – среднесуточная температура в соответствующий день. 
Температуры – целые числа и лежат в диапазоне от –50 до 50

'''

# n = int(input("Введите дней: "))
# i = 1
# max = 0
# tem = 0

# while i <= n:
#     t = int(input(F"Введите температуру {i} дня: "))
#     if t > 0:
#         tem += 1
#     else:
#         if tem > max:
#             max = tem
#         tem = 0
    
#     if tem > max:
#         max = tem
#     i += 1
# print(max)

'''
Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. 
Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача: 
арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, 
записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза. 
Все числа натуральные и не превышают 30000.

'''
# import random

# n = int(input("Введите количество арбузов: "))
# min = 30000
# max = 0

# for i in range(n):
#     wt = random.randint(3000,30000)
    
#     if wt < min:
#         min = wt
    
#     if wt > max:
#         max = wt
    
# print(f"Арбуз Ивана Васильевича весит - {max} гр., тещин арбуз весит - {min} гр.")