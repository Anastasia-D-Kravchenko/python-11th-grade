import networkx as nx
import matplotlib.pyplot as plt
edges = [(1, 1), (0, 4), (2, 6), (2, 3), (2, 4), (3, 4), (5, 6), (5, 1)]
G = nx.Graph(edges)
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_color='black', font_size=10, edge_color='gray', linewidths=1, alpha=0.7)
plt.savefig('graph.png')
plt.show()