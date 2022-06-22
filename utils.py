import numpy as np
from typing import List, Tuple


INT_MAX = 10000


def convet_graph_to_adj_dict(graph, exclude_pts):
    n_rows, n_cols = graph.shape
    adjacency_dict = {}
    for row in range(n_rows):
        for col in range(n_cols):
            key = graph[row, col]
            if [row, col] in exclude_pts:
                adjacency_dict[key] = []
                continue

            vals = []

            if (row - 1) >= 0:
                if [row - 1, col] not in exclude_pts:
                    vals.append(graph[row - 1, col])
            if (row + 1) <= n_rows - 1:
                if [row + 1, col] not in exclude_pts:
                    vals.append(graph[row + 1, col])
            if (col - 1) >=0:
                if [row, col - 1] not in exclude_pts:
                    vals.append(graph[row, col - 1])
            if (col + 1) <= n_cols - 1:
                if [row, col + 1] not in exclude_pts:
                    vals.append(graph[row, col + 1])
            
            adjacency_dict[key] = vals
    
    return adjacency_dict


def convert_num_to_pos(nums: List, n_cols) -> List:
    positions = []
    for num in nums:
        x = num // n_cols
        y = num % n_cols
        positions.append((x, y))
    return positions


def onSegment(p:tuple, q:tuple, r:tuple) -> bool:
     
    if ((q[0] <= max(p[0], r[0])) &
        (q[0] >= min(p[0], r[0])) &
        (q[1] <= max(p[1], r[1])) &
        (q[1] >= min(p[1], r[1]))):
        return True
         
    return False
 

def orientation(p:tuple, q:tuple, r:tuple) -> int:
     
    val = (((q[1] - p[1]) *
            (r[0] - q[0])) -
           ((q[0] - p[0]) *
            (r[1] - q[1])))
            
    if val == 0:
        return 0
    if val > 0:
        return 1 # Collinear
    else:
        return 2 # Clock or counterclock
 
def doIntersect(p1, q1, p2, q2):
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)
 
    if (o1 != o2) and (o3 != o4):
        return True
     
    if (o1 == 0) and (onSegment(p1, p2, q1)):
        return True
 
    if (o2 == 0) and (onSegment(p1, q2, q1)):
        return True
 
    if (o3 == 0) and (onSegment(p2, p1, q2)):
        return True

    if (o4 == 0) and (onSegment(p2, q1, q2)):
        return True
 
    return False
 
def is_inside_polygon(points:list, p:tuple) -> bool:
     
    n = len(points)
     
    if n < 3:
        return False
         
    extreme = (INT_MAX, p[1])
    count = i = 0
     
    while True:
        next = (i + 1) % n
         
        if (doIntersect(points[i],
                        points[next],
                        p, extreme)):
                             
            if orientation(points[i], p,
                           points[next]) == 0:
                return onSegment(points[i], p,
                                 points[next])
                                  
            count += 1
             
        i = next
         
        if (i == 0):
            break
         
    return (count % 2 == 1)
 
# Driver code
if __name__ == '__main__':
    # graph = np.arange(30)
    # graph = graph.reshape((5, 6))
    # adj_graph = convet_graph_to_adj_dict(graph)
    # nums = [2, 8, 14, 20, 26, 27, 28, 29]
    # print(convert_num_to_pos(nums, n_cols=6))
     
    polygon1 = [[4, 5], [4, 6], [4, 7], [4, 8], [6, 10], [7, 10], [9, 9], [9, 8], [9, 7], [9, 6], [8, 4], [7, 4], [6, 4], [5, 4], [4, 4], [5, 9], [8, 10], [9, 5]]
     
    p = (2, 3)
    if (is_inside_polygon(points = polygon1, p = p)):
      print ('Yes')
    else:
      print ('No')