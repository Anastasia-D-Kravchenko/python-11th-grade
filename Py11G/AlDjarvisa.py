# Програма реалізації алгоритму Джарвіса
print("Вправа_1")
n = int(input('Кількість точок: '))
# x = [10, 5, 11, 13, 7, 3, 17, 8]
# y = [14, 16, 4, 17, 7, 3, 9, 10]
x = [2, 3, 4, 5, 5, 7, 10]
y = [5, 7, 2, 6, 5, 1, 8]
t = [0] * n
xn = [0] * n
yn = [0] * n
m = 0
for i in range(1, n):
    if x[i] < x[m]:
        m = i
    elif x[i] == x[m] and y[i] < y[m]:
        m = i
k = 0
x1 = x[m]
y1 = y[m]
xn[k] = x1
yn[k] = y1
poisk = True
while poisk:
    poisk = False
    for i in range(n):
        if t[i] == 0:
            x2 = x[i]
            y2 = y[i]
            pt = True
            for j in range(n):
                if (x[j] - x1) * (y2 - y1) - (y[j] - y1) * (x2 - x1) < 0:
                    pt = False
            if not pt:
                for j in range(n):
                    if (x[j] - x1) * (y2 - y1) * (y[j] - y1) * (x2 - x1) < 0:
                        pt = False
            if pt:
                k = k + 1
                x1 = x2
                y1 = y2
                t[i] = k
                xn[k] = x1
                yn[k] = y1
                poisk = True
print('Координати точок опуклої оболонки:')
for i in range(k + 1):
    print(xn[i], yn[i])
#побудова мінімальної опуклої оболонки мовою Python
#В роботі використано: https://habr.com/ru/articles/144921/
print("\nВправа_2")
def jarvis_march(A):
    def rotate(p, q, r):
        return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    n = len(A)
    P = list(range(n))
    for i in range(1, n):
        if A[P[i]][0] < A[P[0]][0] or (A[P[i]][0] == A[P[0]][0] and A[P[i]][1] < A[P[0]][1]):
            P[i], P[0] = P[0], P[i]
    H = [P[0]]
    del P[0]
    P.append(H[0])
    while True:
        right = 0
        for i in range(1, len(P)):
            if rotate(A[H[-1]], A[P[right]], A[P[i]]) < 0:
                right = i
        if P[right] == H[0]:
            break
        else:
            H.append(P[right])
            del P[right]
    return H
#Координати стибзіні звідси: https://ua.maptons.com/45984
cities = {
    "Київ": (30.5234, 50.4501),
    "Харків": (36.2304, 49.9935),
    "Львів": (24.0232, 49.8429),
    "Одеса": (30.7233, 46.4825),
    "Черкаси": (32.0621, 49.4444),
    "Житомир": (28.6364, 50.2547),
    "Херсон": (32.0572, 46.6354),
    "Запоріжжя": (35.0462, 47.8388),
    "Полтава": (34.5499, 49.5883),
    "Чернігів": (31.0132, 51.4979),
    "Луцьк": (25.6086, 50.7472),
    "Ужгород": (22.3036, 48.6208),
}
coordinates = list(cities.values())
convex_hull = jarvis_march(coordinates)
print("Мінімальна опукла оболонка:")
for idx in convex_hull:
    print(list(cities.keys())[idx])
non_hull_cities = [city for city in cities.keys() if coordinates.index(cities[city]) not in convex_hull]
print("\nМіста, які не розташовані на ребрах і вершинах оболонки:")
print(non_hull_cities)