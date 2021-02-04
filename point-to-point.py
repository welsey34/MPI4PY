#! /usr/bin/env python3

'''
Sending two 2 x 3 np.arrays with values ranging from 1 - 100 from one node to another 
using MPI4PY's point to point.
'''

from mpi4py import MPI
import numpy as np
import sys

comm = MPI.COMM_WORLD
assert comm.size == 2 #Assuring it only runs on 2 cores
rank = comm.Get_rank()
root = 0

data1 = np.random.rand(2, 3)
data1 = [i*100 for i in data1]

data2 = np.random.rand(2,3)
data2 = [i*100 for i in data2]


if comm.rank == root:
	comm.send(data1, dest=1, tag=11)
	comm.send(data2, dest=1, tag=22)
elif comm.rank == 1:
	comm.recv(source=0, tag=11)
	comm.recv(source=0, tag=22)
	print("From {} the data1 -> {}".format(rank, data1))
	print("From {} the data2 -> {}".format(rank, data2))
	
 






