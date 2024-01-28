#------------------------------------------------------------------------  
print("Завдання 3")
list = input("Введіть через кому: ").split(",")
list = [int(i) for i in list]
for i in range((len(list)-1)):
    for a in range(i+1,(len(list))):
        if list[i] < list[a]: #ось тут перемикач
            list[i], list[a] = list[a], list[i]
print(", ".join(str(i) for i in list))
#------------------------------------------------------------------------  
print("Завдання 3 зміна кода з книжки")
mas = [34, 12, 8, 5, 20, 17]
n = len (mas)
p = n-1
while p>0:
    y = True
    for i in range (p):
        if mas [i]<mas [i+1]: #ось тут перемикач
            z = mas [i]; mas[i] = mas [i+1]; mas [i+1] = z
            y = False
    p = p-1
for i in range (n): 
    if i != n-1:
        print (mas[i], end =" ")
    else:
        print (mas[i])
#------------------------------------------------------------------------  
print("Завдання 4")
list = input("Введіть через кому: ").split(", ")
alf = ['а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я']
for i in range(len(list)-1):
    for a in range(i+1, len(list)):
        word1 = list[i]
        word2 = list[a]
        for j in range(min(len(word1), len(word2))):
            if alf.index(word1[j]) > alf.index(word2[j]):
                list[i], list[a] = list[a], list[i]
                break
            elif alf.index(word1[j]) < alf.index(word2[j]):
                break
print(", ".join(list))
#------------------------------------------------------------------------  
print("Завдання 5")
from random import*
list = []
for i in range(10):
    list.append(randint(1,8))
print("До сортування:", ", ".join(str(i) for i in list))
for i in range((len(list)-1)):
    for a in range(i+1,(len(list))):
        if list[i] > list[a]: #ось тут перемикач
            list[i], list[a] = list[a], list[i]
print("Після сортування:", ", ".join(str(i) for i in list))
#------------------------------------------------------------------------  
print("Завдання 5 зміна кода з книжки")
from random import*
mas = []
for i in range(10):
    mas.append(randint(1,8))
n = len (mas)
for i in range (n): 
    if i != n-1:
        print (mas[i], end =" ")
    else:
        print (mas[i])
p = n-1
while p>0:
    y = True
    for i in range (p):
        if mas [i]>mas [i+1]: #ось тут перемикач
            z = mas [i]; mas[i] = mas [i+1]; mas [i+1] = z
            y = False
    p = p-1
for i in range (n): 
    if i != n-1:
        print (mas[i], end =" ")
    else:
        print (mas[i])
#------------------------------------------------------------------------  
print("Завдання 6")
from random import*
list = []
for i in range(12):
    list.append(randint(4,11))
print("До сортування:", ", ".join(str(i) for i in list))
for i in range((len(list)-1)):
    for a in range(i+1,(len(list))):
        if list[i] > list[a]: #ось тут перемикач
            list[i], list[a] = list[a], list[i]
print("Після сортування:", ", ".join(str(i) for i in list))
#------------------------------------------------------------------------  
print("Завдання 6 зміна кода з книжки")
from random import*
mas = []
for i in range(12):
    mas.append(randint(4,11))
n = len (mas)
for i in range (n): 
    if i != n-1:
        print (mas[i], end =" ")
    else:
        print (mas[i])
p = n-1
while p > 0:
    m = 0
    for i in range(1, p + 1):
        if mas[i] > mas[m]:
            m = i
    mas[m], mas[p] = mas[p], mas[m]
    p = p - 1
for i in range(n):
    print(mas[i], end=" ")