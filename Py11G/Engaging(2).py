from random import*
#------------------------------------------------------------------------  
print("Завдання 414")
list_start = []
for i in range(10):
    list_start.append(randint(-100,100))
print(list_start)
list_new = []
for i in list_start:
    if i > 0:
        list_new.append(i)
print(list_new, f"\nКількість: {len(list_new)}")
#------------------------------------------------------------------------  
print("Завдання 416")
list_start = list(map(int, input("Введіть список чисел: ").split()))
list_new = []
for i in list_start:
    if list_start.count(i) == 1:
        list_new.append(str(i))
print(" ".join(list_new))
#------------------------------------------------------------------------  
print("Завдання 417")
list_start = list(map(int, input("Введіть список чисел: ").split()))
print(set(list_start), f"\nКількість: {len(set(list_start))}")
#------------------------------------------------------------------------  
print("Завдання 419")
list_start = list(map(int, input("Введіть список чисел: ").split()))
m_c = 0
for i in set(list_start):
    count = list_start.count(i)
    if count > m_c:
        most_com = i
        m_c = count
print(most_com)
#------------------------------------------------------------------------  
print("Завдання 424")
list_start = list(map(str, input("Введіть список чисел: ").split()))
print(len(set(list_start)))
#------------------------------------------------------------------------  
print("Завдання 426")
list_start = list(map(str, input("Введіть список чисел: ").split(".")))
print(" ".join(list_start))
#------------------------------------------------------------------------  
print("Завдання 427")
list_start = list(map(int, input("Введіть список чисел: ").split()))
print(f"Найменше {min(list_start)}. \nНайбільше {max(list_start)}. \nКількість {len(list_start)}. \nСереднє значення {sum(list_start)/len(list_start)}.")
#------------------------------------------------------------------------  
print("Завдання 439")
respond = "так"
while respond == "так":
    list_start = input("Введіть математичний вираз: ").split()
    operator = list_start[1]
    if operator == 'plus':
        result = int(int(list_start[0])) + int(int(list_start[2]))
    elif operator == 'minus':
        result = int(list_start[0]) - int(list_start[2])
    elif operator == 'multiply':
        result = int(list_start[0]) * int(list_start[2])
    elif operator == 'divide':
        result = int(list_start[0]) // int(list_start[2])
    print(result)
    respond = input("Бажаєте повторити? ")
#------------------------------------------------------------------------  
print("Завдання 439_2")
respond = "так"
while respond == "так":
    operator_all = {
        'plus': '+',
        'minus': '-',
        'multiply': '*',
        'divide': '//'
    }  
    list_start = input("Введіть математичний вираз: ").split()
    print(eval(f"{list_start[0]} {operator_all.get(list_start[1])} {list_start[2]}"))
    respond = input("Бажаєте повторити? ")
#------------------------------------------------------------------------  
print("Завдання 444")
list_start = list(map(str, input("Введіть список: ").split(",")))
print(",".join(sorted(list_start)))
#------------------------------------------------------------------------  
print("Завдання з презентація")
s = input().split()
stek = []
flag = False
for element in s:
    open = "({["
    close = ")}]"
    if element in open:
        stek.append(element)
    elif element in close:
        if len(stek):
            if stek[-1] == open[close.index(element)]:
                stek.pop()
            else:
                flag = True
                break
if flag or stek:
    print('Nooo')
else:
    print('Yeees')
#------------------------------------------------------------------------  
print("Завдання з файла №2")
respond = "так"
while respond == "так":
    line = input("Введіть математичний вираз: ").split()
    list = []
    operator = ['+', '-', '*', '/']
    for i in line:
        if i not in operator:
            list.append(int(i))
        else:
            if len(list) > 0:
                a = list.pop()
            if len(list) > 0:
                b = list.pop()
            if i == "+":
                ans = a + b
            elif i == "-":
                ans = b - a
            elif i == "*":
                ans = a * b
            elif i == "/":
                ans = b // a
            list.append(ans)
    if len(list) > 1:
        print("ERROR")
    else:
        print(list[0])
    respond = input("Бажаєте повторити? ")