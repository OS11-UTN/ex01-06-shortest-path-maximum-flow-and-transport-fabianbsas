#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: fabian
"""

def get_neighbors(node, gragh):
    neighbors = []
    file = gragh[node]
    for index, value in enumerate(file):
        if value == 1:
            neighbors.append(index)
    return neighbors

def get_distance(node_from, node_to, distances):
    return distances[node_from][node_to]
    
def build_path(precedents, gragh):
    path = []  
    last_node = len(gragh[0]) - 1
    while True: 
        path.insert(0, last_node)
        last_node = precedents[last_node]
        if last_node == None:
            break
    return path
        
def build_distance(path, distances): 
    distance = 0
    cnn = len(path) - 1
    for index in range(cnn):
        node_from = path[index]
        node_to = path[index+1]
        distance = distance + get_distance(node_from, node_to, distances)
    
    return distance

gragh = [[0,1,1,0,0,0],
         [0,0,0,1,0,1],
         [0,0,0,0,1,0],
         [0,0,0,0,0,1],
         [0,0,0,0,0,1],
         [0,0,0,0,0,0]]

distances = [[0,2,2,0,0,0],
             [0,0,0,2,0,5],
             [0,0,0,0,2,0],
             [0,0,0,0,0,1],
             [0,0,0,0,0,2],
             [0,0,0,0,0,0]]

cnn_nodes = len(gragh[0])

nodes_weight = [None] * cnn_nodes
#Initial node must be weigth 0
nodes_weight[0] = 0

precedents = [None] * cnn_nodes

for node in range(cnn_nodes):
    neighbors = get_neighbors(node, gragh)
    for neighbor in neighbors: 
        weight = nodes_weight[node] + get_distance(node, neighbor, distances)  
        if nodes_weight[neighbor] == None  or weight < nodes_weight[neighbor]:
            nodes_weight[neighbor] = weight
            precedents[neighbor] = node
            


# Resuts 
print("\n\n## Results ## \n\n")

path = build_path(precedents, gragh) 
print("the shorther path is {}".format(path))

distance = build_distance(path, distances) 
print("The minimun cost is {}".format(distance))
