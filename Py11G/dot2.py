import tkinter as tk
def analyze():
    try:
        A = float(a.get().strip())
        B = float(b.get().strip())
        C = float(c.get().strip())
        Mx = float(mx.get().strip())
        My = float(my.get().strip())
        Nx = float(nx.get().strip())
        Ny = float(ny.get().strip())

        r_text_.delete(1.0, tk.END)
        if (A * Mx + B * My + C) * (A * Nx + B * Ny + C) > 0:
            result = "Ці дві точки лежать по один бік від заданої прямої ax + by + c = 0"
        elif (A * Mx + B * My + C) * (A * Nx + B * Ny + C) < 0:
            result = "Ці дві точки лежать по різні боки від заданої прямої ax + by + c = 0"
        else:
            result = "Задані точки не збігаються і не знаходяться по одній вертикалі або горизонталі на площині."
        r_text_.insert(tk.END, result)
    except ValueError:
        r_text_.delete(1.0, tk.END)
        r_text_.insert(tk.END, "Помилка: введіть числові значення для координат.")
root = tk.Tk()
root.geometry('600x400')
root.title("Взаємне розміщення прямої та данних двох точок")
root.configure(bg='#FFE0C1')

frame = tk.Frame(root, bg='#FFE0C1')
frame.pack(padx=10, pady=10)

tk.Label(frame, text="Введiть коефiцiенти рiвняння прямої Ax+By+C=0", bg='#FFE0C1').grid(row=0, column=0, columnspan=6, pady=10)
tk.Label(frame, text="A=", bg='#FFE0C1').grid(row=1, column=0)
tk.Label(frame, text="B=", bg='#FFE0C1').grid(row=1, column=2)
tk.Label(frame, text="C=", bg='#FFE0C1').grid(row=1, column=4)

a = tk.Entry(frame)
b = tk.Entry(frame)
c = tk.Entry(frame)

a.grid(row=1, column=1)
b.grid(row=1, column=3)
c.grid(row=1, column=5)

tk.Label(frame, text="Введiть координати данних двох точок", bg='#FFE0C1').grid(row=2, column=0, columnspan=8, pady=10)
tk.Label(frame, text="Mx=", bg='#FFE0C1').grid(row=3, column=0)
tk.Label(frame, text="My=", bg='#FFE0C1').grid(row=4, column=0)
tk.Label(frame, text="Nx=", bg='#FFE0C1').grid(row=3, column=4)
tk.Label(frame, text="Ny=", bg='#FFE0C1').grid(row=4, column=4)

mx = tk.Entry(frame)
my = tk.Entry(frame)
nx = tk.Entry(frame)
ny = tk.Entry(frame)

mx.grid(row=3, column=1)
my.grid(row=4, column=1)
nx.grid(row=3, column=5)
ny.grid(row=4, column=5)

tk.Button(frame, text='Провести аналiз випадкiв взаємного розмiщення прями i данних точок', command=analyze).grid(row=5, column=0, columnspan=8, pady=10)

r_text = tk.StringVar()
r_label = tk.Label(frame, text="Відповідь:", bg='#FFE0C1')
r_label.grid(row=6, column=1, padx=10, pady=10)
r_text_ = tk.Text(frame, height=4, width=30, wrap="word")
r_text_.grid(row=6, column=2, columnspan=3, padx=10, pady=10)

tk.Button(frame, text="Вихiд", command=root.destroy).grid(row=8, column=0, pady=10)

root.mainloop()