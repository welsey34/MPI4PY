#!/usr/bin/env python3

from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
processor = MPI.Get_processor_name()
root = 0
sendbuff = []

if comm.rank == 0:
	m = np.array(range(comm.size *comm.size), dtype=float)
	m.shape = (comm.size, comm.size)
	print(m)
	sendbuff = m

v = comm.scatter(sendbuff, root)
print("I am rank {} on {} and I received array {}".format(rank,processor,v ))

v=v*v
recvbuff = comm.gather(v, root)

if comm.rank == 0:
	print("I am rank {} on {} and gathered \n{}".format(rank, processor, np.array(recvbuff)))
