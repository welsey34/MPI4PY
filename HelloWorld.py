#!/usr/bin/env python3

from mpi4py import MPI


comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
name = MPI.Get_processor_name()

print("I am process {} of {} on {}!".format(rank, size, name))


