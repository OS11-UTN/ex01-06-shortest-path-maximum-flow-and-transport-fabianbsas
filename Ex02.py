#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: fabian
"""

import numpy
import sys
from Ex00 import transform_NN_to_NA, get_active_archs
from scipy.optimize import linprog


matrix = [[0,1,1,0,0,0],
          [0,0,0,1,0,1],
          [0,0,0,0,1,0],
          [0,0,0,0,0,1],
          [0,0,0,0,0,1],
          [0,0,0,0,0,0]]

matrix_NN = numpy.array(matrix)
cost_vector = numpy.array([2, 1, 2, 5, 2, 1, 2])
beq = numpy.array([1,0,0,0,0,-1])

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


for method in ["interior-point", "simplex"]: 
    
    # Optimize
    result = linprog(cost_vector, A_eq = Aeq, b_eq=beq, bounds=bounds, method=method)

    # Resuts 
    print("Solution with method {}:".format(method))
    
    raw_active_archs = result.x 
    active_archs = [ int(value) for index, value in enumerate(raw_active_archs) ]

    print("\tThe raw solution is: {} \n".format(active_archs))

    active_archs = get_active_archs(arc_idxs, active_archs)
    print("\tThe archs that make the shortest path are: {} \n".format(active_archs))
 
    print("\tThe minimun cost is {:.2f} \n".format(result.fun))
    
    
