"""
Задача No25. Решение в группах
Напишите программу, которая принимает на вход строку, и отслеживает, 
сколько раз каждый символ уже встречался. Количество повторов добавляется 
к символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_
"""
# stroka = input().split()
# result = {}
# for i in stroka:
#     if i in result:
#         print(f'{i}_{result[i]}', end=' ')
#     else:
#         print(i, end=' ')
#     result[i] = result.get(i, 0) + 1


"""
Пользователь вводит текст(строка). Словом считается последовательность 
непробельных символов идущих подряд, слова разделены одним или большим 
числом пробелов. Определите, сколько различных слов содержится в этом тексте.
Input: She sells sea shells on the sea shore The shells that she sells 
are sea shells I'm sure.So if she sells sea shells on the sea shore 
I'm sure that the shells are sea shore shells
Output: 13
"""

n = "She sells sea shells on the sea shore The shells that she sells" 
k = "are sea shells I'm sure.So if she sells sea shells on the sea shore"
l = "I'm sure that the shells are sea shore shells"

print(len(n.split()))
print(len(k.split()))
print(len(l.split()))

"""
Задача No29. Решение в группах
Ваня и Петя поспорили, кто быстрее решит следующую задачу: 
“Задана последовательность неотрицательных целых чисел. 
Требуется определить значение наибольшего элемента последовательности, 
которая завершается первым встретившимся нулем (число 0 не входит в 
последовательность)”. Однако 2 друга оказались не такими смышлеными. 
Никто из ребят не смог до конца сделать это задание. Они решили так: 
у кого будет меньше ошибок в коде, тот и выиграл спор. 
За помощью товарищи обратились к Вам, студентам.
"""
# import random
# n = int(input("Введите n: "))
# a = [random.randint(0, 100) for x in range(n)]
# print(a)

# max = a[0]
# for i in a:
#     if i == 0:
#         break
#     if i > max:
#         max = i

# print(max)
    
"""
Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников. 
Теперь он использует их в качестве серверов "Пегого дудочника". Помогите владельцу 
фирмы отыскать все зараженные холодильники.

Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр, 
и если в ней присутствует слово "anton" (необязательно рядом стоящие буквы, главное наличие 
последовательности букв), то холодильник заражен и нужно вывести номер холодильника, 
нумерация начинается с единицы

Формат входных данных
В первой строке подаётся число 
n
n – количество холодильников. В последующих 
n
n строках вводятся строки, содержащие латинские строчные буквы и цифры, в каждой строке от 
5
5 до 
100
100 символов.

Формат выходных данных
Программа должна вывести номера зараженных холодильников через пробел. 
Если таких холодильников нет, ничего выводить не нужно.

Sample Input 1:
6
222anton456
a1n1t1o1n1
0000a0000n00t00000o000000n
gylfole
richard
ant0n
Sample Output 1:
1 2 3
Sample Input 2:
9
osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen
anton
aoooooooooontooooo
elelelelelelelelelel
ntoneeee
tonee
253235235a5323352n25235352t253523523235oo235523523523n
antoooooooooooooooooooooooooooooooooooooooooooooooooooon
unton
Sample Output 2:
1 2 7 8
"""
# n = int(input())
# list1 = []
# for i in range(n):
#     a = input()
#     if 'a' in a:
#         a = a[a.find('a'):]
#         if 'n' in a:
#             a = a[a.find('n'):]
#             if 't' in a:
#                 a = a[a.find('t'):]
#                 if 'o' in a:
#                     a = a[a.find('o'):]
#                     if 'n' in a:
#                         list1.append(i + 1)                   
# print(list1)
