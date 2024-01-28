import tkinter as tk
def analyze():
    try:
        Ax = float(ax.get().strip())
        Ay = float(ay.get().strip())
        Bx = float(bx.get().strip())
        By = float(by.get().strip())
        r_text_.delete(1.0, tk.END)
        if Ax == Bx and Ay == By:
            r_text_.insert(tk.END, "Задані точки збігаються.")
        elif Ax == Bx:
            r_text_.insert(tk.END, "Задані точки знаходяться по одній вертикалі на площині.")
        elif Ay == By:
            r_text_.insert(tk.END, "Задані точки знаходяться по одній горизонталі на площині.")
        else:
            r_text_.insert(tk.END, "Задані точки не збігаються і не знаходяться по одній вертикалі або горизонталі на площині.")
    except ValueError:
        r_text_.delete(1.0, tk.END)
        r_text_.insert(tk.END, "Помилка: введіть числові значення для координат.")
root = tk.Tk()
root.geometry('500x350')
root.title("Аналіз розміщення двох заданих точок на площині")
root.configure(bg='#C0FFC0')

frame = tk.Frame(root, bg='#C0FFC0')
frame.place(relx=0.5, rely=0.5, anchor='center')

tk.Label(frame, text="Ввести координати данних точок", bg='#C0FFC0').grid(row=0, column=0, columnspan=4, padx=10, pady=10)
tk.Label(frame, text="Ax=", bg='#C0FFC0').grid(row=1, column=0, padx=10, pady=10)
tk.Label(frame, text="Ay=", bg='#C0FFC0').grid(row=2, column=0, padx=10, pady=10)
tk.Label(frame, text="Bx=", bg='#C0FFC0').grid(row=1, column=2, padx=10, pady=10)
tk.Label(frame, text="By=", bg='#C0FFC0').grid(row=2, column=2, padx=10, pady=10)

ax = tk.Entry(frame)
ay = tk.Entry(frame)
bx = tk.Entry(frame)
by = tk.Entry(frame)

ax.grid(row=1, column=1, padx=10, pady=10)
ay.grid(row=2, column=1, padx=10, pady=10)
bx.grid(row=1, column=3, padx=10, pady=10)
by.grid(row=2, column=3, padx=10, pady=10)

tk.Button(frame, text='Провести аналіз даних', width=30, command=analyze).grid(row=3, column=0, columnspan=4, padx=10, pady=10)

r_text = tk.StringVar()
r_label = tk.Label(frame, text="Відповідь:", bg='#C0FFC0')
r_label.grid(row=4, column=0, padx=10, pady=10)
r_text_ = tk.Text(frame, height=4, width=30, wrap="word")
r_text_.grid(row=4, column=1, columnspan=3, padx=10, pady=10)

tk.Button(frame, text="Завершити роботу", command=root.destroy).grid(row=5, column=0, columnspan=4, padx=10, pady=10)

root.mainloop()