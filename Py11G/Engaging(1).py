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
print("Завдання презентація")
def check(expression):
    list = []
    open = "({["
    close = ")}]"
    for i in expression:
        if i in open:
            list.append(i)
        elif i in close:
            if not list or open.index(list.pop()) != close.index(i):
                return False
    return not list
expression1 = "(1 + ((2 + 3) * (4 * 5)))"
result1 = check(expression1)
print(f"1-й випадок: {result1}")
expression2 = "([)]"
result2 = check(expression2)
print(f"2-й випадок: {result2}")