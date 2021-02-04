#! /usr/bin/env python3

from math import *
import numpy as np 



from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
processor = MPI.Get_processor_name()


''' 
This project will calculate the area under a curve using trapezoidal reimann sums
Given a function f(x) and an interval a -> b, as well the number of partitions n, it will use 
trapezoids of height (h) = (b-a) / 2 and bases of (f(x1) + f(x2)) / 2 to calculate the area under the given curve.  
'''

'''
The above goal has been completed and now the current goal is to be given an interval (a,b), and once given the interval,
split the interval itself into comm.size() subintervals. Scatter those subintervals across the cluster and have each cluster perform
trapezoidalRiemannSum(function, a, b, n) function on each cluster with the given subinterval.
'''

print(size)


def closestNumber(number, divisible) : 
    # Find the quotient 
    q = int(number / divisible) 
      
    # 1st possible closest number 
    n1 = divisible * q 
      
    # 2nd possible closest number 
    if((number * divisible) > 0) : 
        n2 = (divisible * (q + 1))  
    else : 
        n2 = (divisible * (q - 1)) 
      
    # if true, then n1 is the required closest number 
    if (abs(number - n1) < abs(number - n2)) : 
        return n1 
      
    # else n2 is the required closest number  
    return n2


def trapezoidalRiemannSum(function, a, b, n):
    
    deltax = ( b - a ) / n
    x = list()
    calc = list()


    for i in range(int(a), int(n)):
        data = ( round( (float(a) + i * deltax) , 10), round( (float(a) + (i+1) * deltax) , 10))
        x.append(data)

    #print(x)

    for i in x:
        for j in i:
            calc.append(j)

    calc = list(set(calc))
    allmult = deltax/2
    
    if(n==1):
        calc = list(map(lambda x : eval(f), calc))
        return (round((( (calc[0] + calc[1]) / 2 ) * deltax ), 4))
    else:
        print("first item {} : last item {}".format(calc[0], calc[-1]))
        innersum = calc[1:-1]
       #print("innersum : {}".format(innersum))
        outersum = [calc[0], calc[-1]]
        #print("outersum : {}".format(outersum))
        innersum=list(map(lambda x : 2 * eval(f), innersum))
        #print("innersum after calculation : {}".format(innersum))
        outersum = list(map(lambda x : eval(f), outersum))
        #print("outersum after calculation : {}".format(outersum))
        return round( ((deltax/2) * (sum(innersum) + sum(outersum))), 2  )


a = 0

b = 1000
b = closestNumber(b, size)

dxu = (b - a) / size
subintervals = list()


for i in range(a, size):
	data = ()

f = "x"



