#!/usr/bin/env python

s=raw_input('Enter List : ')
d=(s.split(' '))

l1=[];l2=[]
for i in range(len(d)):
	if i%2==0:
		l1.append(d[i])
	else:
		l2.append(int(d[i]))

c=(zip(l1,l2))
print c
print dict(c)


#   we can do it directly as following #
#import itertools
#print dict(itertools.izip_longest(*[iter(d)] * 2, fillvalue=""))