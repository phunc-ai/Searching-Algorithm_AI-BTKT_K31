from methods.ucs.graph import Graph, Node
from methods.ucs.ucs_algorithm import UCS

def ucs(adj_graph, start_num, end_num):
    # Create graph
    graph = Graph()
    # Add vertices
    for h_node in adj_graph.keys():
      graph.add_node(Node(h_node))


    for h_node in adj_graph.keys():
      for t_node in adj_graph[h_node]:
        graph.add_edge(h_node, t_node, 1)
      

    # Execute the algorithm
    alg = UCS(graph, start_num, end_num)
    expanded_nodes, expanded_cost, num_path, path_cost = alg.search()
    
    return expanded_nodes, expanded_cost, num_path, path_cost

if __name__ == '__main__':
  ucs()

# V1 -> V3 -> V4 -> V5 -> V6
# Length of the path: 6