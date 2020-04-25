#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: fabian
"""
import numpy
import sys
from Ex00 import transform_NN_to_NA
from scipy.optimize import linprog

def get_descriptive_name(arc_idx, node_names):
    source, destination = arc_idx
    return (node_names[source], node_names[destination])
    

node_names = ["Factory 1", "Factory 2", "Factory 3", "Warehouse a", "Warehouse b"]

matrix = [[0, 0, 0, 1, 1],
           [0, 0, 0, 1, 1],
           [0, 0, 0, 1, 1],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0]]

matrix_NN = numpy.array(matrix)
cost_vector = numpy.array([10, 20, 10, 10, 10, 30])
beq = numpy.array([10, 20, 15, -25, -20])

Aeq, arc_idxs = transform_NN_to_NA(matrix_NN) 

bounds = tuple([(0, None) for arch in range(0, Aeq.shape[1])])

if len(cost_vector) != len(arc_idxs):
    print("The quantity of arches and the cost array don't match")
    sys.exit()
    
# check if the arch has the correct cost    
for index, arch in enumerate(arc_idxs):
    print("The arch: {} has a cost of: {}".format(arch, cost_vector[index]))

print("\n\n## Optimazer inputs ## \n\n"
      "Cost vector: {} \n"
      "Node-Arch matrix: \n {} \n"
      "Demand-Supply vector: {} \n"
      "Bounds of each arch: {} \n".format(cost_vector, Aeq, beq, bounds))


# Optimize
result = linprog(cost_vector, A_eq = Aeq, b_eq=beq, bounds=bounds, method="simplex")

# Resuts 
print("\n\n## Results ## \n\n")
 
raw_quantity_carried_per_archs = result.x 
quantity_carried_per_archs = [ int(value) for index, value in enumerate(raw_quantity_carried_per_archs) ]


for i in range(len(arc_idxs)):    
    source, destination = get_descriptive_name(arc_idxs[i], node_names)
    print("\tThe quantity carried from {} to {} is: {}".format(source, destination, quantity_carried_per_archs[i]))

print("\n\tThe cost is {:.2f} \n".format(result.fun))
