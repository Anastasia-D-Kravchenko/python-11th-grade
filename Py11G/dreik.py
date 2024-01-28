def func(graph, start, p={}, u=[]):
    if len(p) == 0:
        p[start] = 0
    for x in graph[start]:
        if (x not in u and x!=start):
            if (x not in p.keys() or (graph[start][x] + p[start]) < p[x]):
                p[x] = graph[start][x] + p[start]
    u.append(start)
    min_v = 0
    for x in p:
        if (p[x] < min_v or min_v == 0) and x not in u:
            min_x = x
            min_v = p[x]
    if (len(u) < len(graph) and min_x):
        return func(graph, min_x, p, u)
    else:
        return p


# N = [
#     {1:3, 3:6, 4:1},
#     {0:3, 2:8},
#     {1:8, 3:4, 4:12},
#     {0:6, 2:4, 4:4},
#     {0:1, 2:12, 3:4}
# ]

N = [
    {1:10, 2:15},
    {3:12, 5:15},
    {4:10},
    {4:2, 5:1},
    {},
    {4:5}
]

result = func(N, 0)

# Сортируем вершины перед выводом
sorted_result = sorted(result.items())

print('Мінімальна відстань до вершини. Перша цифра - вершина, друга - значення')
for vertex, distance in sorted_result:
    print(f'{vertex}: {distance}', end=", ")