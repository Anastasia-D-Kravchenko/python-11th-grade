import tkinter as tk
import math
def calculate_length():
    try:
        x1 = float(ax.get())
        y1 = float(ay.get())
        x2 = float(bx.get())
        y2 = float(by.get())
        
        length = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        ab_E.delete(0, tk.END)
        ab_E.insert(0, f'{length:.2f}')
    except ValueError:
        ab_E.delete(0, tk.END)
        ab_E.insert(0, 'Некоректні данні')
def calculate_midpoint():
    try:
        x1 = float(ax.get())
        y1 = float(ay.get())
        x2 = float(bx.get())
        y2 = float(by.get())
        
        cx = (x1 + x2) / 2
        cy = (y1 + y2) / 2
        
        cx_E.delete(0, tk.END)
        cx_E.insert(0, f'{cx:.2f}')
        cy_E.delete(0, tk.END)
        cy_E.insert(0, f'{cy:.2f}')
    except ValueError:
        cx_E.delete(0, tk.END)
        cy_E.delete(0, tk.END)
        cx_E.insert(0, 'Некоректні данні')
        cy_E.insert(0, 'Некоректні данні')
root = tk.Tk()
root.geometry('600x400')
root.title("Вікно")
root.configure(bg='#EACEB1')
frame = tk.Frame(root, bg='#EACEB1')
frame.place(relx=0.5, rely=0.5, anchor='center')

tk.Label(frame, text="Ввести координати кінців даного відрізка", bg='#EACEB1').grid(row=0, column=0, columnspan=4, padx=10, pady=10)
tk.Label(frame, text="Ax=", bg='#EACEB1').grid(row=1, column=0, padx=10, pady=10)
tk.Label(frame, text="Ay=", bg='#EACEB1').grid(row=2, column=0, padx=10, pady=10)
tk.Label(frame, text="Bx=", bg='#EACEB1').grid(row=1, column=2, padx=10, pady=10)
tk.Label(frame, text="By=", bg='#EACEB1').grid(row=2, column=2, padx=10, pady=10)

ax = tk.Entry(frame)
ay = tk.Entry(frame)
bx = tk.Entry(frame)
by = tk.Entry(frame)

ax.grid(row=1, column=1, padx=10, pady=10)
ay.grid(row=2, column=1, padx=10, pady=10)
bx.grid(row=1, column=3, padx=10, pady=10)
by.grid(row=2, column=3, padx=10, pady=10)

tk.Button(frame, text='Обчислити довжину відрізка', width=30, command=calculate_length).grid(row=3, column=0, columnspan=4, padx=10, pady=10) 
tk.Button(frame, text='Обчислити координати середини С відрізка', width=40, command=calculate_midpoint).grid(row=4, column=0, columnspan=4, padx=10, pady=10) 

tk.Label(frame, text='|AB|=', width=5, bg='#EACEB1').grid(row=5, column=0, padx=10, pady=10) 
ab_E = tk.Entry(frame)
ab_E.grid(row=5, column=1, padx=10, pady=10) 

tk.Label(frame, text='Cx=', width=5, bg='#EACEB1').grid(row=5, column=2, padx=10, pady=10)
cx_E = tk.Entry(frame)
cx_E.grid(row=5, column=3, padx=10, pady=10)

tk.Label(frame, text='Cy=', width=5, bg='#EACEB1').grid(row=6, column=2, padx=10, pady=10)
cy_E = tk.Entry(frame)
cy_E.grid(row=6, column=3, padx=10, pady=10)

btn_ex = tk.Button(frame, text='Завершити роботу', command=root.destroy, width=30)
btn_ex.grid(row=8, column=0, columnspan=4, padx=10, pady=10)

root.mainloop()