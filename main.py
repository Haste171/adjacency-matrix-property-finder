import networkx as nx
import numpy as np

M = np.array([
    [0,0,1,0],
    [1,0,1,1],
    [0,1,0,0],
    [1,1,0,0]
])
G = nx.DiGraph(M)
def is_reflexive(G):
    return all(G.has_edge(n, n) for n in G.nodes)

def is_anti_reflexive(G):
    return all(not G.has_edge(n, n) for n in G.nodes)

def is_symmetric(G):
    return all(G.has_edge(v, u) for u, v in G.edges)

def is_antisymmetric(G):
    return all(not (G.has_edge(v, u) and G.has_edge(u, v)) or u == v for u, v in G.edges)

def is_transitive(G):
    for u in G.nodes:
        for v in G.nodes:
            for w in G.nodes:
                if G.has_edge(u, v) and G.has_edge(v, w) and not G.has_edge(u, w):
                    return False
    return True

print("Reflexive:", is_reflexive(G))
print("Anti-Reflexive:", is_anti_reflexive(G))
print("Symmetric:", is_symmetric(G))
print("Antisymmetric:", is_antisymmetric(G))
print("Transitive:", is_transitive(G))
