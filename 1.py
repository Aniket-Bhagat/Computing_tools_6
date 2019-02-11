#!/usr/bin/env python

import sys
n=int(sys.argv[1])

total=0
for i in range(1,n):
	if n%i == 0:
		total+=i

if total == n:
	print 'Number '+str(n)+' is Perfect Number'
else:
	print 'Number '+str(n)+' is not a Perfect Number'