from bfs import bfs
from dfs import dfs
from iddfs import iddfs



import networkx as nx
import matplotlib.pyplot as plt
# Your graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

# Create directed graph
G = nx.DiGraph()

# Add edges
for node, neighbors in graph.items():
    for neighbor in neighbors:
        G.add_edge(node, neighbor)

# Draw
plt.figure(figsize=(6, 5))
pos = nx.spring_layout(G)  # auto layout

nx.draw(
    G, pos,
    with_labels=True,
    node_color='lightblue',
    node_size=2000,
    font_size=12,
    font_weight='bold',
    arrows=True
)

plt.title("Graph Representation")
plt.show()

print("BFS:", end=" ")
bfs(graph, 'A')
print("\nDFS:", end=" ")
dfs(graph, 'A')
print("\nIDDFS:")
iddfs(graph, 'A', 3)
