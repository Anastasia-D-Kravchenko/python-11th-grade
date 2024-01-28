# Імпортуємо бібліотеки tkinter і math
from tkinter import *
from math import sqrt

# Функція solver обчислює корені квадратного рівняння та повертає результат у вигляді текстового рядка
def solver(a, b, c):
    # Обчислюємо дискримінант рівняння
    D = b*b - 4*a*c
    if D >= 0:
        # Якщо дискримінант не менший за нуль, обчислюємо корені(можно ще було 
        # б розділити >0 дискрімінант та =0, а то 2 однаковиї розв'язка напишемо)
        x1 = (-b + sqrt(D)) / (2*a)
        x2 = (-b - sqrt(D)) / (2*a)
        # Формуємо текст з результатами
        text = f"Дискримінант: {D}\n x1 = {x1}\n x2 = {x2}\n"
    else:
        # Якщо дискримінант від'ємний, то формуємо текст: розв'язків немає
        text = f"Дискримінант: {D}\n Рівняння розв'язків немає"
    return text

# Функція inserter вставляє текстовий рядок у багаторядкове текстове поле.
def inserter(value):
    output.delete("0.0", "end")
    output.insert("0.0", value)

# Функція clear очищає текстові поля введення
def clear(event):
    caller = event.widget
    caller.delete("0", "end")

# Функція handler викликається при натисканні кнопки "Розв'язати".
# Вона спробує отримати коефіцієнти a, b і c з текстових полів введення,
# обчислить розв'язок та вставить результат у багаторядкове текстове поле.
# Якщо введені дані не є числами, вставить відповідне повідомлення.
def handler():
    try:
        a_val = float(a.get())
        b_val = float(b.get())
        c_val = float(c.get())
        inserter(solver(a_val, b_val, c_val))
    except ValueError:
        inserter("Вставити числові коефіцієнти квадратного рівняння")

# Створення головного вікна і встановлення його параметрів.
root = Tk()
root.title("Розв'язок квадратного рівняння")
root.geometry("330x230+300+100")
root.resizable(width=False, height=False)

# Створення рамки та розміщення її на головному вікні.
frame = Frame(root)
frame.pack()

# Створення текстових полів введення для коефіцієнтів a, b, 
# c і відповідних написів та встановлення обробника події для них
a = Entry(frame, width=3)
a.grid(row=1, column=1, padx=(10, 0))
a.bind("<FocusIn>", clear)
al = Label(frame, text="x**2+").grid(row=1, column=2)

b = Entry(frame, width=3)
b.bind("<FocusIn>", clear)
b.grid(row=1, column=3)
bl = Label(frame, text="x+").grid(row=1, column=4)

c = Entry(frame, width=3)
c.bind("<FocusIn>", clear)
c.grid(row=1, column=5)
cl = Label(frame, text="= 0").grid(row=1, column=6)

# Створення кнопки "Розв'язати" та встановлення обробника події для неї
but = Button(frame, text="Розв'язати", command=handler).grid(row=1, column=7, padx=(10, 0))

# Створення багаторядкового текстового поля для виведення результату
output = Text(frame, bg="lightblue", font="Arial 12", width=35, height=10)
output.grid(row=2, columnspan=8)

# Запуск головного циклу програми
root.mainloop()