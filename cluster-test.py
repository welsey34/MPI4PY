#!/usr/bin/env python3


from mpi4py import MPI
import sys


comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
name = MPI.Get_processor_name()
root = 0

fpIn = open("/clusterfs/test.txt", "r")
contents = fpIn.read()

print("I am process {} of {} on {}. HELLO {}".format(rank, size, name, contents))
#print(contents)





