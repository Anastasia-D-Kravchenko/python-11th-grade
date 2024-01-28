#------------------------------------------------------------------------
print("Завдання 1")
import random
n = int(input())
mas = [random.randrange(-100, 100) for _ in range(n)]
print(mas)
n = len(mas)
max_val = mas[0]
for i in range(n):
    if mas[i] > max_val:
        max_val = mas[i]
print('Максимальне значення =', max_val)
# ------------------------------------------------------------------------
print("Завдання 2")
n = int(input())
mas = [random.randrange(-100, 100) for _ in range(n)]
print(mas)
n = len(mas)
min_val = mas[0]
for i in range(n):
    if mas[i] < min_val:
        min_val = mas[i]
print('Мінімальне значення =', min_val)
#------------------------------------------------------------------------
print("Завдання 3")
n = 15
mas = [random.randrange(-100, 100) for _ in range(n)]
print(mas)
n = len(mas)
max_val = mas[0]
min_val = mas[0]
for i in range(n):
    if mas[i] > max_val:
        max_val = mas[i]
    if mas[i] < min_val:
        min_val = mas[i]
print('Максимальне значення =', max_val)
print('Мінімальне значення =', min_val)
print(f'Півсума: {(max_val+min_val)/2}')
#------------------------------------------------------------------------
print("Завдання 4")
n = int(input())
mas = [random.randrange(-100, 100) for _ in range(n)]
print(mas)
n = len(mas)
min_val1 = mas[0]
for i in range(n):
    if mas[i] > 0:
        if mas[i] < min_val1:
            min_val1 = mas[i]
print('Мінімальне додатне значення =', min_val1)
#------------------------------------------------------------------------
print("Завдання 5")
n = 15
C = [random.randrange(-100, 100) for _ in range(n)]
print("Початковий масив:", C)
n = len(C)
max_val = C[0]
min_val = C[0]
max_index = 0
min_index = 0
for i in range(1, n):
    if C[i] > max_val:
        max_val = C[i]
        max_index = i
    if C[i] < min_val:
        min_val = C[i]
        min_index = i
C[min_index], C[max_index] = C[max_index], C[min_index]
print('Масив після обміну:', C)
print('Максимальне значення =', max_val)
print('Мінімальне значення =', min_val)
#------------------------------------------------------------------------
print("Завдання 6")
n = 12
a = [random.randrange(-100, 100) for _ in range(n)]
print("Початковий масив:", a)
max_val = a[0]
for i in range(n):
    if a[i] > max_val:
        max_val = a[i]
print('Максимальне значення =', max_val)
max_index = a.index(max_val)
b = a[:max_index]
print("Масив b:", b)
#------------------------------------------------------------------------
print("Завдання 7")
n = 15
a = [random.randrange(-100, 100) for _ in range(n)]
print("Початковий масив:", a)
min_val = a[0]
for i in range(n):
    if a[i] < min_val:
        min_val = a[i]
min_index = a.index(min_val)
b = a[min_index+1:]
print('Найменше значення =', min_val)
print("Масив b:", b)