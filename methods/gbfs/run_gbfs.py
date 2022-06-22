from collections import deque
from utils import convert_num_to_pos
 
class Graph:
    def __init__(self, adjac_lis, end_pos, n_cols):
        self.adjac_lis = adjac_lis
        self.end_pos = end_pos
        self.n_cols = n_cols
        self.weight = 0
 
    def get_neighbors(self, v):
        return self.adjac_lis[v]
 
    # This is heuristic function which is having equal values for all nodes
    def h(self, n):
        n_pos = convert_num_to_pos([n], self.n_cols)[0]
        man_dis = abs(n_pos[0] - self.end_pos[0]) + abs(n_pos[1] - self.end_pos[1])
 
        return man_dis
 
    def gbfs_algorithm(self, start, stop):
        # In this open_lst is a lisy of nodes which have been visited, but who's 
        # neighbours haven't all been always inspected, It starts off with the start 
  #node
        # And closed_lst is a list of nodes which have been visited
        # and who's neighbors have been always inspected
        open_lst = set([start])
        closed_lst = set([])
        expanded_cost = 0
 
        # poo has present distances from start to all other nodes
        # the default value is +infinity
        poo = {}
        poo[start] = 0
 
        # par contains an adjac mapping of all nodes
        par = {}
        par[start] = start
 
        while len(open_lst) > 0:
            n = None
 
            # it will find a node with the lowest value of f() -
            for v in open_lst:
                if n == None or poo[v] + self.h(v) < poo[n] + self.h(n):
                    expanded_cost += 1
                    n = v;
 
            if n == None:
                print('Path does not exist!')
                return [], closed_lst, expanded_cost
 
            # if the current node is the stop
            # then we start again from start
            if n == stop:
                reconst_path = []
 
                while par[n] != n:
                    reconst_path.append(n)
                    n = par[n]
 
                reconst_path.append(start)
 
                reconst_path.reverse()
 
                return reconst_path, closed_lst, expanded_cost
 
            # for all the neighbors of the current node do
            for m in self.get_neighbors(n):
              # if the current node is not presentin both open_lst and closed_lst
                # add it to open_lst and note n as it's par
                if m not in open_lst and m not in closed_lst:
                    open_lst.add(m)
                    par[m] = n
                    poo[m] = poo[n] + self.weight
 
                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update par data and poo data
                # and if the node was in the closed_lst, move it to open_lst
                else:
                    if poo[m] > poo[n] + self.weight:
                        poo[m] = poo[n] + self.weight
                        par[m] = n
 
                        if m in closed_lst:
                            closed_lst.remove(m)
                            open_lst.add(m)
 
            # remove n from the open_lst, and add it to closed_lst
            # because all of his neighbors were inspected
            open_lst.remove(n)
            closed_lst.add(n)
 
        print('Path does not exist!')
        return [], closed_lst, expanded_cost


def gbfs(adj_graph, start, end, n_cols):
    end_pos = convert_num_to_pos([end], n_cols)[0]
    graph = Graph(adj_graph, end_pos, n_cols)
    path, visited, expanded_cost = graph.gbfs_algorithm(start, end)
    path_cost = len(path) - 1

    return visited, expanded_cost, path, path_cost



if __name__ == '__main__':
    adjac_lis = {
        'A': [('B', 1), ('C', 3), ('D', 7)],
        'B': [('D', 5)],
        'C': [('D', 12)]
    }
    graph1 = Graph(adjac_lis)
    graph1.gbfs_algorithm('A', 'D')