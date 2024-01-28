#------------------------------------------------------------------------
print("Завдання 1")
print("ГЛИБИНА")
graph = {0: [1, 2, 3], 1: [0, 2, 4, 5], 2: [0, 1, 3, 4], 3: [0, 2], 4: [1, 2, 6], 5: [1, 6], 6: [4, 5]}
visited = {i: False for i in graph}
print(visited)
print('Порядок обходу вершин')

def dfs(vertex):
    print(vertex, end=" ")
    visited[vertex] = True
    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            dfs(neighbor)

for current in graph:
    if not visited[current]:
        dfs(current)
print("\nШИРОТА")
graph = {0: [1, 2, 3], 1: [0, 2, 4, 5], 2: [0, 1, 3, 4], 3: [0, 2], 4: [1, 2, 6], 5: [1, 6], 6: [4, 5]}
pozhat = [-1] * len(graph)
print('Початковий стан', pozhat)
def func(s):
    global pozhat
    pozhat[s] = 0
    zherg = [s]
    print('Динаміка зміни стану перегляду вершин')
    while zherg:
        print(pozhat)
        v = zherg.pop(0)
        for m in graph[v]:
            if pozhat[m] == -1:
                zherg.append(m)
                pozhat[m] = pozhat[v] + 1
    for i in range(len(graph)):
        if pozhat[i] == -1:
            func(i)

for i in range(len(graph)):
    if pozhat[i] == -1:
        func(i)
    print('Вершина', i, ', номер обходу', pozhat[i])
#------------------------------------------------------------------------
print("\nЗавдання 2")
print("ГЛИБИНА")
graph = {0: [2, 3], 1: [0, 2, 4, 5, 7], 2: [3, 4, 7, 8], 3: [0, 2], 4: [1, 2, 6], 5: [1, 6, 7], 6: [4, 5, 7], 7: [1, 2, 5, 6], 8: [2]}
visited = {i: False for i in graph}
print(visited)
print('Порядок обходу вершин')

def dfs(vertex):
    print(vertex, end=" ")
    visited[vertex] = True
    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            dfs(neighbor)

for current in graph:
    if not visited[current]:
        dfs(current)
print("\nШИРОТА")
graph = {0: [2, 3], 1: [0, 2, 4, 5, 7], 2: [3, 4, 7, 8], 3: [0, 2], 4: [1, 2, 6], 5: [1, 6, 7], 6: [4, 5, 7], 7: [1, 2, 5, 6], 8: [2]}
pozhat = [-1] * len(graph)
print('Початковий стан', pozhat)
def func(s):
    global pozhat
    pozhat[s] = 0
    zherg = [s]
    print('Динаміка зміни стану перегляду вершин')
    while zherg:
        print(pozhat)
        v = zherg.pop(0)
        for m in graph[v]:
            if pozhat[m] == -1:
                zherg.append(m)
                pozhat[m] = pozhat[v] + 1
    for i in range(len(graph)):
        if pozhat[i] == -1:
            func(i)

for i in range(len(graph)):
    if pozhat[i] == -1:
        func(i)
    print('Вершина', i, ', номер обходу', pozhat[i])