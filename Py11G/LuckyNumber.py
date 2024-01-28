#------------------------------------------------------------------------  
print("Завдання 411")
from random import*
list = []
for i in range(0, 10):
    list.append(randint(0, 100))
print(list)
list_new = []
for i in list:
    if i%2 != 0:
        list_new.append(i)
print(list_new)
#------------------------------------------------------------------------  
print("Завдання 412")
list = []
for i in range(0, 10):
    list.append(randint(0, 100))
print(list)
less_than = int(input("Введіть число: "))
list_new = []
for i in list:
    if i > less_than:
        list_new.append(i)
print(list_new)