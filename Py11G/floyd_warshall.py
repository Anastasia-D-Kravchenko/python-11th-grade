infinity = float("inf")
def make_graph():
    # identical graph as the YouTube video: https://youtu.be/4OQeCuLYj-4
    # tuple = (cost, to_node)
    return {
        1: [(5, 2), (8, 3), (2, 6)],
        2: [(5, 1), (5, 3), (3, 5)],
        3: [(8, 1), (5, 2), (2, 4)],
        4: [(2, 3), (3, 5)],
        5: [(3, 2), (3, 4), (4, 6)],
        6: [(2, 1), (4, 5)]
    }
def floyd_warshall(G):
    size = len(G)
    matrix = [ [infinity]*size for i in range(size) ]
    for i in range(size):
        matrix[i][i] = 0
    for node, edges in G.items():
        for edge in edges:
            cost = edge[0]
            to_node = edge[1]
            matrix[node-1][to_node-1] = cost
    for k in range(size):
        for i in range(size):
            for j in range(size):
                if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]
    return matrix
def main():
    G = make_graph()
    shortest_path_matrix = floyd_warshall(G)
    print(f'Shortest path matrix:\n')
    for item in shortest_path_matrix:
        print(item)
main()