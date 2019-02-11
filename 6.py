#!/usr/bin/env python

import sys
s=sys.argv[1]
R=int(sys.argv[2])
N=len(''.join(s.split(' ')))

def fact(n):
	if(n==0):return 1
	else:return n*fact(n-1)

a=0
while(a==0):
	if N<R:
		sys.stdout.write('Length of "'+s+'" is less than '+str(R)+'. ')
		R=input('Enter n again : ')
	else:
		ans=fact(N)/fact(N-R)
		print ans
		a=1