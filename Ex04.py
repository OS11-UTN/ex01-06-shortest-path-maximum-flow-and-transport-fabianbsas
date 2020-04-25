#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: fabian
"""

import numpy
import sys
from Ex00 import transform_NN_to_NA
from scipy.optimize import linprog

def get_usage(arc_idxs, result_flow, max_capacity):
    return {arc: '%s/%s' % (flow, cap) for arc, flow, cap in zip(arc_idxs, result_flow, max_capacity)}

def get_minimum_cut(arc_idxs, result_flow, max_capacity):
    max_capacity = numpy.where(max_capacity == None, 999, max_capacity)

    idxs = numpy.argwhere((result_flow - max_capacity) == 0)
    return [arc_idxs[i[0]] for i in idxs]


matrix = [[0,1,1,0,0,0],
          [0,0,0,1,0,1],
          [0,0,0,0,1,0],
          [0,0,0,0,0,1],
          [0,0,0,0,0,1],
          [0,0,0,0,0,0]]

#add a new arch from node t to s (here is from node 5 to 0)
matrix[5][0] = 1

matrix_NN = numpy.array(matrix)
Aeq, arc_idxs = transform_NN_to_NA(matrix_NN) 
cost_vector = numpy.array([0, 0, 0, 0, 0, 0, 0, -1])
beq = numpy.array([0, 0, 0, 0, 0, 0])
max_capacity = numpy.array([7, 1, 2, 3, 2, 1, 2, None])

bounds = tuple([(0, max_capacity[arch]) for arch in range(0, Aeq.shape[1])])
#print(bounds)

if len(max_capacity) != len(arc_idxs):
    print("The quantity of arches and the capacity vector don't match")
    sys.exit()
    
# check if the arch has the correct cost    
for index, arch in enumerate(arc_idxs):
    print("The arch: {} has a cost of: {}".format(arch, max_capacity[index]))


print("\n\n## Optimazer inputs ## \n\n"
      "Cost vector: {} \n"
      "Node-Arch matrix: \n {} \n"
      "Demand-Supply vector: {} \n"
      "Bounds of each arch: {} \n".format(cost_vector, Aeq, beq, bounds))

    
# Optimize
result = linprog(cost_vector, A_eq = Aeq, b_eq=beq, bounds=bounds, method="simplex")

# Resuts 
usage = get_usage(arc_idxs, result.x.astype(int), max_capacity)
min_cut = get_minimum_cut(arc_idxs, result.x.astype(int), max_capacity)
max_flow = result.fun * - 1 # Mult x -1 since the new arch added has negative cost 

print("\n\n## Results ## \n\n")
print("\tThe usage of it arch is: {} \n".format(usage))
print("\tThe archs that make the minimum cut are: {} \n".format(min_cut)) 
print("\tThe minimun cost is {:.2f} \n".format(max_flow))

    
