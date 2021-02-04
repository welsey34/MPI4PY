#!/usr/bin/env python3

from  mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
root = 0


if rank == root:
	data = np.random.rand(2,3)
else:
	data = None

data = comm.bcast(data, root)
print("rank {} : data {} of type {}".format(rank, data, type(data)))


