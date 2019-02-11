#!/usr/bin/env python

import sys
n=int(sys.argv[1])

for i in range(1,n+1):
	sys.stdout.write(' '*(n-i))
	for j in range(1,i+1):
		sys.stdout.write(str(j))
	for k in range(1,i):
		sys.stdout.write(str(i-k))
	sys.stdout.write('\n')