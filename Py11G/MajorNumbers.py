#------------------------------------------------------------------------  
print("Завдання 1")
result = 4.375 * (10 ** 20)
print(result)
#------------------------------------------------------------------------  
print("Завдання 2")
FT = float(input("Введіть температуру в градусах Фаренгейта: "))
CT = 5 / 9 * (FT - 32)
print(f"{FT} градусів Фаренгейта дорівнює {CT:.2f} градусів Цельсія.")
#------------------------------------------------------------------------  
print("Завдання 3")
str_number = '234.25'
result = float(str_number)
print(result)
at_all = 234.25
if result == at_all:
    print("Результат є правильним.")
else:
    print("Результат не є правильним.")
#------------------------------------------------------------------------  
print("Завдання 4")
min_seed_rate = 3
max_seed_rate = 4
min_yield = 3
max_yield = 3.5
area = 100
min_seed_rate = min_seed_rate * area
max_seed_rate = max_seed_rate * area
min_yield = min_yield * area
max_yield = max_yield * area
print(f"Мінімальний посів зерна в насінинах: {min_seed_rate:.0f} млн насінин")
print(f"Максимальний посів зерна в насінинах: {max_seed_rate:.0f} млн насінин")
print(f"Мінімальний врожай в зерні: {min_yield:.0f} тонн")
print(f"Максимальний врожай в зерні: {max_yield:.0f} тонн")
