import networkx as nx
import numpy as np


M = np.array([
    [0,0,1,0],
    [1,0,1,1],
    [0,1,0,0],
    [1,1,0,0]
])

# Create a directed graph from the adjacency matrix
G = nx.DiGraph(M)

# Reflexivity: Check if all nodes have self-loops
def is_reflexive(G):
    return all(G.has_edge(n, n) for n in G.nodes)

# Anti-reflexivity: Check if no node has a self-loop
def is_anti_reflexive(G):
    return all(not G.has_edge(n, n) for n in G.nodes)

# Symmetry: Check if for every edge (u, v), there is an edge (v, u)
def is_symmetric(G):
    return all(G.has_edge(v, u) for u, v in G.edges)

# Antisymmetry: Check if for every edge (u, v), there is no edge (v, u) unless u == v
def is_antisymmetric(G):
    return all(not (G.has_edge(v, u) and G.has_edge(u, v)) or u == v for u, v in G.edges)

# Transitivity: Check if for every edges (u, v) and (v, w), there is an edge (u, w)
def is_transitive(G):
    for u in G.nodes:
        for v in G.nodes:
            for w in G.nodes:
                if G.has_edge(u, v) and G.has_edge(v, w) and not G.has_edge(u, w):
                    return False
    return True

# Check properties
print("Reflexive:", is_reflexive(G))
print("Anti-Reflexive:", is_anti_reflexive(G))
print("Symmetric:", is_symmetric(G))
print("Antisymmetric:", is_antisymmetric(G))
print("Transitive:", is_transitive(G))
