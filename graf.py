class Graph:
    def __init__(self, directed=False):
        self.nodes = set()
        self.edges = []
        self.directed = directed

    def add_node(self, node):
        self.nodes.add(node)

    def add_edge(self, u, v, weight=None):
        self.nodes.add(u)
        self.nodes.add(v)
        if weight is not None:
            self.edges.append((u, v, weight))
        else:
            self.edges.append((u, v))

    def analyze(self):
        print("--- ANALÝZA GRAFU ---")
        
        print(f"Orientovaný graf: {'Ano' if self.directed else 'Ne'}")

        has_weights = any(len(edge) == 3 for edge in self.edges)
        print(f"Ohodnocený (vážený) graf: {'Ano' if has_weights else 'Ne'}")

        has_loops = any(edge[0] == edge[1] for edge in self.edges)
        print(f"Obsahuje smyčky: {'Ano' if has_loops else 'Ne'}")

        print("Planární: [Vyžaduje dodatečný algoritmický test, např. Kuratowského podgrafy]")

        print("Chromatické číslo: [Vyžaduje obarvování grafu, např. NP-těžký problém]")
        
        print("---------------------")

if __name__ == "__main__":
    g = Graph(directed=False)
    
    g.add_edge("A", "B", 4)
    g.add_edge("B", "C", 2)
    g.add_edge("C", "A", 1)
    g.add_edge("A", "A")
    
    g.analyze()