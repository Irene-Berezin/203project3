import networkx as nx

def dfs_iterative(G, start):
    # Set to keep track of visited nodes
    visited = set()
    # Stack for DFS; initialize with the start node
    stack = [start]
    
    # Continue until there are no more nodes to process
    while stack:
        # Pop the last node from the stack
        vertex = stack.pop()
        # If we haven't visited the node yet
        if vertex not in visited:
            # Mark it as visited (or process it)
            visited.add(vertex)
            print(vertex)  # You can process the node here (e.g., print it)
            # Add neighbors to the stack.
            # Convert the generator from G.neighbors(vertex) to a list and reverse it
            # for desired processing order.
            for neighbor in reversed(list(G.neighbors(vertex))):
                if neighbor not in visited:
                    stack.append(neighbor)

# Example usage:
# Create a simple graph using NetworkX
G = nx.Graph()
# Add some nodes and edges
G.add_edges_from([
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'D'),
    ('B', 'E'),
    ('C', 'F'),
    ('E', 'F')
])

# Run DFS starting from node 'A'
dfs_iterative(G, 'A')
