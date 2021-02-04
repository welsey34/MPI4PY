#! /usr/bin/env python3

from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.size
processor = MPI.Get_processor_name()
root = 0
rank = comm.Get_rank()


def trapz(f,a,b,N=50):
	x = np.linspace(a,b,N+1)
	y = f(x)
	y_right = y[1:]
	y_left = y[:-1]
	dx = (b-a)/N
	return (dx/2) * np.sum(y_right + y_left)

a = 0
b = 1
n = 10**7
f = lambda x :np.sqrt(1- x**2)

s = np.linspace(a, b, size+1)
send_buff = []

if(rank == root):
	for i in range(len(s)-1):
		send_buff.append([s[i], s[i+1]])
	print(send_buff)

scat = comm.scatter(send_buff, root)
temp = trapz(f, scat[0], scat[1], n)
#print("I am rank {} on {} and I received {}. The integral is {}".format(rank, processor, scat, temp))

recvbuff = comm.gather(temp, root)

if(rank == root):
	print("I am rank {} on {}, and received {} and the sum * 4 is {} which {} away from pi".format(rank, processor, recvbuff, sum(recvbuff)*4, np.pi-sum(recvbuff)*4))

