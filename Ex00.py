#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: fabian
"""
import numpy

# This function receive a node node matrix and create a new node arch matrix 
def transform_NN_to_NA(matrix_NN): 
    #Create a new empty node arch matrix
    
    archs = numpy.argwhere(matrix_NN)
    #print(archs)

    matrix_NA = numpy.zeros([len(matrix_NN[0]), len(archs)]).astype(int)
    #print(matrix_NA)
    
    for index, arch in enumerate(archs): 
        # the index is the colums
        matrix_NA[arch[0]][index] = 1
        matrix_NA[arch[1]][index] = -1
       
    arc_idxs = [(arc[0], arc[1]) for arc in archs] 
       
    return matrix_NA, arc_idxs


def get_active_archs(arc_idxs, selected):
    active_archs = []
    for index, value in enumerate(selected):
        if value > 0: 
            active_archs.append(arc_idxs[index])
            
    return active_archs

# Test 
matrix_NN = [[0,1,1],
             [0,0,0],
             [0,0,0]]

print("Node-Node matrix \n", matrix_NN)

matrix_NA, arc_idxs = transform_NN_to_NA(matrix_NN) 
print("Node-Arch matrix \n", matrix_NA)
print("Archs \n", arc_idxs)

selected = [1,0]
active_archs = get_active_archs(arc_idxs, selected)
print("Selected archs \n", active_archs)