import argparse

import numpy as np
import visualize

from utils import *
from visualize import *
from convex_block import *
from methods import *


def main(algorithm='bfs'):
    with open('input.txt', 'r') as f:
        raw_lines = f.readlines()
    lines = []
    for rl in raw_lines:
        l = rl.strip('\n').split(' ')
        l = [int(ele) for ele in l]
        lines.append(l)
    
    # Load shape
    shapes = lines[0]
    n_rows, n_cols = int(shapes[0]), int(shapes[1])
    
    # Load start and end points
    checkpoints = lines[1]

    start_pos = (int(checkpoints[0]), int(checkpoints[1]))
    end_pos = (int(checkpoints[2]), int(checkpoints[3]))

    # Create graph w.r.t shape and points
    graph = np.arange(n_rows * n_cols).reshape((n_rows, n_cols))
    start_num = start_pos[0] * n_cols + start_pos[1]
    end_num = end_pos[0] * n_cols + end_pos[1]

    # Make block
    num_blocks = lines[2][0]
    pol_pts = []
    wall_pts = []
    in_pol_pts = []
    for i in range(3, 3 + num_blocks):
        pol_block_pts = []
        block = lines[i]
        assert len(block) % 2 == 0
        for i in range(int(len(block) / 2)):
            pol_block_pts.append([int(block[2*i]), int(block[2*i + 1])])
        
        # Find points on wall exclude pol_block_pts
        wall_block_pts = []
        for i in range(len(pol_block_pts)):
            if i == len(pol_block_pts) - 1:
                wall_block_pts.extend(make_convex_block(pol_block_pts[i], pol_block_pts[0]))
            else:
                wall_block_pts.extend(make_convex_block(pol_block_pts[i], pol_block_pts[i+1]))
        
        # Find points inside poligons
        all_pol_block_pts = pol_block_pts + wall_block_pts
        in_block_pol_pts = []
        for i in range(n_rows):
            for j in range(n_cols):
                if is_inside_polygon(all_pol_block_pts, (i, j)) and ([i, j] not in all_pol_block_pts):
                    in_block_pol_pts.append([i, j])
        
        pol_pts.extend(pol_block_pts)
        wall_pts.extend(wall_block_pts)
        in_pol_pts.extend(in_block_pol_pts)


    # Convert graph to adjacent dictionary
    adj_graph = convet_graph_to_adj_dict(graph, pol_pts + wall_pts + in_pol_pts)

    if algorithm == 'bfs':
        expanded_nodes, expanded_cost, num_path, path_cost = bfs(adj_graph, start_num, end_num)
    if algorithm == 'ucs':
        expanded_nodes, expanded_cost, num_path, path_cost = ucs(adj_graph, start_num, end_num)
    if algorithm == 'ids':
        expanded_nodes, expanded_cost, num_path, path_cost = ids(adj_graph, start_num, end_num)
    if algorithm == 'astar':
        expanded_nodes, expanded_cost, num_path, path_cost = a_star(adj_graph, start_num, end_num, n_cols)
    if algorithm == 'gbfs':
        expanded_nodes, expanded_cost, num_path, path_cost = gbfs(adj_graph, start_num, end_num, n_cols)

    path = convert_num_to_pos(num_path, n_cols)
    expanded_pos = convert_num_to_pos(expanded_nodes, n_cols)

    maze = np.zeros(shape=(n_rows, n_cols))

    for pt in pol_pts:
        maze[pt[0],pt[1]] = visualize.POL_POINT
    for pt in wall_pts:
        maze[pt[0], pt[1]] = visualize.WALL
    for pt in in_pol_pts:
        maze[pt[0], pt[1]] = visualize.IN_POL
    for pt in expanded_pos:
        maze[pt[0], pt[1]] = visualize.EXP_NODE

    maze[start_pos[0], start_pos[1]] = visualize.START
    maze[end_pos[0], end_pos[1]] = visualize.END

    draw(maze, path, title="{}\tExpanded Cost:{}\tPath Cost:{}".format(algorithm.upper(), expanded_cost, path_cost))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="Searching algorithms")
    parser.add_argument('--algorithm', '-alg', type=str, choices=['bfs', 'ucs', 'ids', 'astar', 'gbfs'])
    args = parser.parse_args()
    print("Searching using {} algorithm!".format(args.algorithm.upper()))
    main(args.algorithm)
    # main('bfs')