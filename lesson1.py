'''
1. За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров? 
При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.

**Input:**

n = 700

m = 750

**Output:**

n = int(input("Введите скорость: "))
m = int(input("Общее длина: "))
print((m-1)//m +1)

2
3. В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами. 
За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов. 
Выведите наименьшее число парт, которое нужно приобрести для них.

**Input:**

20

21

22

**Output:**

32

n_class = 3
n_part = 0
for i in range(n_class):
    n_student = int(input(f"Введите количество {i+1} классе: "))
    n_part = n_part + ((n_student+1)//2)
print(n_part)

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
5. Вагоны в электричке пронумерованы натуральными числами, начиная с 1 (при этом иногда вагоны 
нумеруются от «головы» поезда, а иногда – с «хвоста»; это зависит от того, в какую сторону едет электричка). 
В каждом вагоне написан его номер. Витя сел в i-й вагон от головы поезда и обнаружил, что его вагон имеет номер j. 
Он хочет определить, сколько всего вагонов в электричке. Напишите программу, которая будет это делать или сообщать, 
что без дополнительной информации это сделать невозможно.

**Input:**

3

4

**Output:**

6

7. Дано натуральное число. Требуется определить, является ли год с данным номером високосным. Если год является 
високосным, то выведите YES, иначе выведите NO. Напомним, что в соответствии с григорианским календарем, 
год является високосным, если его номер кратен 4, но не кратен 100, или он кратен 400.

**Input:**

2016

**Output:**

YES

Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
    
    *Примеры:*
    
    - 6,78 -> 7
    - 0,34 -> 3
'''