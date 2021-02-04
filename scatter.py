#!/usr/bin/env pytho	n3

from mpi4py import MPI
import numpy as np
from time import sleep

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
root = 0
processor = MPI.Get_processor_name()

data = np.random.rand(comm.size, comm.size)
send_buff = []

if comm.rank == root:
	send_buff = data
	print(data)

scat = comm.scatter(send_buff, root)
print("I am {} : {}. I got this array : {}".format(rank, processor, scat))



