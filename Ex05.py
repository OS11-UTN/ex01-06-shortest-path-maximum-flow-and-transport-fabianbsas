#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: fabian
"""

import numpy


def depth_first_search(matrix_residual, source, sink):
    stack, path = [source], []
    
    while len(stack) > 0:
        current_node = stack[0]
        stack = stack[1:]
        path.append(current_node)
        if current_node == sink:
            break
        for neighbor, value in enumerate(matrix_residual[current_node]):
            if value > 0 and neighbor != source:
                stack.insert(0, neighbor)
             
    if sink == path[-1]:    
        return path
    return []
    

def max_path_flow(matrix, path):
    max_flow = float('inf')
    for idx in range(len(path)-1):
        u = path[idx]
        v = path[idx+1]
        if matrix[u][v] < max_flow:
            max_flow = matrix[u][v]
        
    return max_flow
    


matrix_nodo_nodo_with_cost = numpy.array([[0, 7, 1, 0, 0, 0],
                                         [0, 0, 0, 2, 0, 3],
                                         [0, 0, 0, 0, 2, 0],
                                         [0, 0, 0, 0, 0, 1],
                                         [0, 0, 0, 0, 0, 2],
                                         [0, 0, 0, 0, 0, 0]])


matrix_residual = matrix_nodo_nodo_with_cost.copy()

source = 0
sink = 5

path = depth_first_search(matrix_residual, source, sink)
max_capacity = max_path_flow(matrix_nodo_nodo_with_cost, path)
    
maximum_flow = 0
minimum_cut = []
while len(path) > 1:
    maximum_flow = maximum_flow + max_capacity
    for idx in range(len(path)-1):
        u = path[idx]
        v = path[idx+1]
        if matrix_residual[u][v] == max_capacity:
            minimum_cut.append((u, v))
        matrix_residual[u][v] = matrix_residual[u][v] - max_capacity
        #matrix_residual[v][u] = matrix_residual[v][u] + max_capacity
    
    #print(path, max_capacity)
    #print(matrix_residual)
    path = depth_first_search(matrix_residual, source, sink)
    max_capacity = max_path_flow(matrix_residual, path)
    

print("\n\n## Results ## \n\n")
print("\tThe maximum flow is {}".format(maximum_flow))
print("\tThe minimum cut is {}".format(minimum_cut))



