from collections import defaultdict
print("Код взяла звідси: https://www.geeksforgeeks.org/find-paths-given-source-destination/")
print("Завдання №2")
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.num_to_letter = {0: 'A', 1: 'B', 2: 'D', 3: 'C'}
        self.edge_weights = {}
    def addEdge(self, u, v, weight):
        self.graph[u].append(v)
        self.edge_weights[(u, v)] = weight
    def printAllPathsUtil(self, u, d, visited, path, total_length):
        visited[u] = True
        path.append(u)
        if u == d:
            path_letters = [self.num_to_letter[node] for node in path]
            print("Path:", list(reversed(path_letters)))
            print("Total Length:", total_length)
        else:
            for i in self.graph[u]:
                if not visited[i]:
                    self.printAllPathsUtil(i, d, visited, path, total_length + self.edge_weights[(u, i)])
        path.pop()
        visited[u] = False
    def printAllPaths(self, s, d):
        visited = [False] * (self.V)
        path = []
        self.printAllPathsUtil(s, d, visited, path, 0)
g = Graph(4)
g.addEdge(0, 1, 3)
g.addEdge(0, 2, 2)
g.addEdge(1, 0, 3)
g.addEdge(2, 0, 2)
g.addEdge(1, 2, 5)
g.addEdge(1, 3, 7)
g.addEdge(2, 1, 5)
g.addEdge(3, 1, 7)
g.addEdge(2, 3, 8)
g.addEdge(3, 2, 8)
s = 0
d = 2
print("Following are all different paths from D to A:")
g.printAllPaths(s, d)