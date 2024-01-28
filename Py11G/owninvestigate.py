import tkinter as tk
def analyze_placement():
    try:
        x1, y1 = float(ax.get()), float(ay.get())
        x2, y2 = float(bx.get()), float(by.get())
        X, Y = float(nx.get()), float(ny.get())

        on_line = (X - x1) * (y2 - y1) - (Y - y1) * (x2 - x1) == 0
        within_range = min(x1, x2) <= X <= max(x1, x2) and min(y1, y2) <= Y <= max(y1, y2)
        
        r_text_.delete(1.0, tk.END)
        r_text_1.delete(1.0, tk.END)
        r_text_.insert(tk.END, "Точка N" + (" " if on_line else " не ") + "належить прямій, що проходить через задані дві точки.")
        
        if on_line:
            r_text_1.insert(tk.END, "Точка N" + (" " if within_range else " не ") + "належить даному відрізку.")
    except ValueError:
        r_text_.delete(1.0, tk.END)
        r_text_1.delete(1.0, tk.END)
        r_text_.insert(tk.END, "Помилка: введіть числові значення для координат.")
root = tk.Tk()
root.geometry('500x500')
root.title("Аналіз взаємного розміщення точки та відрізка")
root.configure(bg='#FFFFC1')

frame = tk.Frame(root, bg='#FFFFC1')
frame.place(relx=0.5, rely=0.5, anchor='center')

tk.Label(frame, text="Введіть координати кінцевих точок відрізка", bg='#FFFFC1').grid(row=0, column=0, columnspan=4, padx=10, pady=10)
tk.Label(frame, text="Ax=", bg='#FFFFC1').grid(row=1, column=0, padx=10, pady=10)
tk.Label(frame, text="Ay=", bg='#FFFFC1').grid(row=2, column=0, padx=10, pady=10)
tk.Label(frame, text="Bx=", bg='#FFFFC1').grid(row=1, column=2, padx=10, pady=10)
tk.Label(frame, text="By=", bg='#FFFFC1').grid(row=2, column=2, padx=10, pady=10)

ax = tk.Entry(frame)
ay = tk.Entry(frame)
bx = tk.Entry(frame)
by = tk.Entry(frame)

ax.grid(row=1, column=1, padx=10, pady=10)
ay.grid(row=2, column=1, padx=10, pady=10)
bx.grid(row=1, column=3, padx=10, pady=10)
by.grid(row=2, column=3, padx=10, pady=10)

tk.Label(frame, text="Введіть координати точки N", bg='#FFFFC1').grid(row=4, column=0, columnspan=4, padx=10, pady=10)
tk.Label(frame, text="Nx=", bg='#FFFFC1').grid(row=5, column=0, padx=10, pady=10)
tk.Label(frame, text="Ny=", bg='#FFFFC1').grid(row=5, column=2, padx=10, pady=10)

nx = tk.Entry(frame)
ny = tk.Entry(frame)

nx.grid(row=5, column=1, padx=10, pady=10)
ny.grid(row=5, column=3, padx=10, pady=10)

tk.Button(frame, text='Провести аналіз даних', width=30, command=analyze_placement).grid(row=3, column=0, columnspan=4, padx=10, pady=10)

r_text = tk.StringVar()
r_label = tk.Label(frame, text="Відповідь:", bg='#FFFFC1')
r_label.grid(row=6, column=0, padx=10, pady=10)
r_text_ = tk.Text(frame, height=4, width=30, wrap="word")
r_text_.grid(row=6, column=1, columnspan=3, padx=10, pady=10)
r_text_1 = tk.Text(frame, height=4, width=30, wrap="word")
r_text_1.grid(row=7, column=1, columnspan=3, padx=10, pady=10)

tk.Button(frame, text="Завершити роботу", command=root.destroy).grid(row=8, column=0, columnspan=4, padx=10, pady=10)

root.mainloop()