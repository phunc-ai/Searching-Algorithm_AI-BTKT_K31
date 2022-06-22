class Graph:
    # Constructor
    def __init__(self, num_of_nodes, directed=True):
        self.m_num_of_nodes = num_of_nodes
        self.m_nodes = range(self.m_num_of_nodes)
		
        # Directed or Undirected
        self.m_directed = directed
		
        # Graph representation - Adjacency list
        # We use a dictionary to implement an adjacency list
        self.m_adj_list = {node: set() for node in self.m_nodes}      
	
    # Add edge to the graph
    def add_edge(self, node1, node2, weight=1):
        self.m_adj_list[node1].add((node2, weight))

        if not self.m_directed:
            self.m_adj_list[node2].add((node1, weight))
    
    # Print the graph representation
    def print_adj_list(self):
        for key in self.m_adj_list.keys():
            print("node", key, ": ", self.m_adj_list[key])


    def dfs(self, start, target, max_depth, path=[], visited=set(), expanded_cost=0):
        path.append(start)
        visited.add(start)
        if start == target:
            return path, visited, expanded_cost
        
        if max_depth <= 0:
            path.pop()
            return [], visited, expanded_cost

        for (neighbour, weight) in self.m_adj_list[start]:
            if neighbour not in visited:
                expanded_cost += 1
                result, visited, expanded_cost = self.dfs(neighbour, target, max_depth - 1, path, visited, expanded_cost)
                if len(result) != 0:
                    return result, visited, expanded_cost
        path.pop()
        return [], visited, expanded_cost
    
    def iddfs(self, start, target, max_depth, path=[], visited=set()):
        total_visited = set()
        total_expaned_cost = 0
        for i in range(1, max_depth + 1):
            result, loop_visited, loop_expanded_cost = self.dfs(start, target, i, path=[], visited=set())
            total_expaned_cost += loop_expanded_cost
            for v in loop_visited:
                total_visited.add(v)
            if result:
                return result, total_visited, total_expaned_cost
        return [], total_visited, total_expaned_cost


def ids(adj_graph, start, end):
    graph = Graph(len(adj_graph.keys()), directed=False)

    for h_node in adj_graph.keys():
      for t_node in adj_graph[h_node]:
        graph.add_edge(h_node, t_node)
      

    # Execute the algorithm
    path, expanded_nodes, total_expaned_cost = graph.iddfs(start, end, 100)
    path_cost = len(path) - 1
    
    return expanded_nodes, total_expaned_cost, path, path_cost



if __name__ == '__main__':
    graph = Graph(6, directed=False)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.add_edge(2, 5)
    graph.print_adj_list()
    path, total_visted, total_expaned_cost = graph.iddfs(0, 4, 3)
    print(total_expaned_cost)
    print(path)
    print(total_visted)