#Завдання 1
print("Завдання 1")
list_1 = [1,2,3,4,5]
print('list_1: '+ str(list_1))
print('max list_1: ' + str(max(list_1)),'min list_1: ' + str(min(list_1)),
      'sum: ' + str(sum(list_1)),'average: ' + str(sum(list_1)/len(list_1)), sep = '\n')
print()
#Завдання 2
print("Завдання 2")
list_1 = []
list_2 = []

for i in range(10):
    a = int(input("Введіть числа: "))
    if a % 2 == 0:
        list_1.append(a)
    if a % 2 != 0:
        list_2.append(a)

def rs1(list_1 ):
    numbers_1 = []
    for i in list_1:
        if i in numbers_1:
            continue
        else:
            numbers_1.append(i)
    return numbers_1

def rs2(list_2 ):
    numbers_2 = []
    for f in list_2:
        if f in numbers_2:
            continue
        else:
            numbers_2.append(f)
    return numbers_2
print("Прямій послідовності 1: " + str(rs1(list_1 )),"Зворотній послідовності 1: " + str(rs1(list_1)[::-1]),
    "За зростанням 1: " + str(sorted(rs1(list_1))),
      "За спаданням 1: " + str(sorted(rs1(list_1),reverse=True)), sep='\n')
print()
print("Прямій послідовності 2: " + str(rs2(list_2 )),"Зворотній послідовності 2: " + str(rs2(list_2)[::-1]),
    "За зростанням 2: " + str(sorted(rs2(list_2))),
      "За спаданням 2: " + str(sorted(rs2(list_2),reverse=True)), sep='\n')
print()
#Завдання 3
print("Завдання 3")
a = int(input("Введіть початок проміжку: "))
b = int(input("Введіть кінець проміжку: "))
list_1 = []

for i in range(a, b):
    for f in range(2,i):
        if i % f == 0:
            break
    else:
        list_1.append(i)
print("Список простих значень: " + str(list_1) )
print()

print('Ви можете виконати операції зі списком:\n\t1.додавання\n\t2.множення\n\t')
g = int(input("Оберіть операцію 1,2: "))

if g == 1:
    s = 0
    for t in list_1:
        s += t
    print("Сума:" + str(s))
elif g == 2:
    k = 1
    for y in list_1:
        k *= y
    print("Добуток: " + str(k))
else:
    print('Немає такої операції')
print()
#Завдання 4
print("Завдання 4")
list_3 = []

for i in range(5):
    a = int(input("Введіть числа: "))
    list_3.append(a)
print()
print("Список: " + str(list_3), "Кількість елементів у списку: " + str(len(list_3)), sep='\n')
print()
print('Ви можете виконати операції зі списком:\n\t1.вивести значення на екран у зворотному порядку\n\t'
      '2.вивести значення на екран за зростанням\n\t')
g = int(input("Оберіть операцію 1,2: "))

match g:
    case 1:
        print("Зворотній порядок: " + str(list_3[::-1]))
    case 2:
        print("За зростанням: " + str(sorted(list_3)))
    case _:
        print('Немає такої операції')
print()
#Завдання 5
print("Завдання 5")
from itertools import repeat
a = int(input("Введіть значення: "))

int_list = []
new_list = []
for i in range(2,a):
    for f in range(2,i):
        if i % f == 0:
            break
    else:
        int_list.append(i)
print("int_list: " + str(int_list))
print()

b = int(input('Введiть кількість повторів у новому списку: '))
x = repeat(list(int_list), 3)
for l in x:
    new_list.append(l)
print("new_list:" + str(new_list))
int_list.clear()
print()

print("int_list [значення видалені]: " + str(int_list))

print()
#Завдання 6
print("Завдання 6")
new_list_1 = []
znach = int(input('Яке значення ви шукаєте зі списку 5-го завдання?: '))
for g in new_list:
    new_list_1.extend(g)
print("Кількість повторів вказаного значення: " + str(new_list_1.count(znach)))

indexes = [i for i, c in enumerate(new_list_1) if c == znach]
print(f"Вказане значення '{znach}' за индексом {indexes}")
print("Кінець=)")
