#!/usr/bin/env python

s=raw_input('Enter List : ')
d=(s.split(','))

def swap(t1, t2): return t2, t1

n=len(d)-1
a=0;b=0
while(a!=n):
	a=0
	for i in range(n):
		if int(d[i])>int(d[i+1]):
			d[i],d[i+1]=swap(d[i],d[i+1])
			b+=1
			print 'Exchange '+str(b) +' : '+','.join(d)
		else:
			a+=1

print('Sorted list: '+','.join(d))