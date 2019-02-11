#!/usr/bin/env python

import sys
s=list(sys.argv[1])

n=0
empty=[]
for i in range(len(s)):
	empty.append(s[-(i+1)])
	if s[i]==s[-(i+1)]:
		n+=1
	
print ''.join(empty)
if n==len(s):
	print 'Palindrom'
else:
	print 'Not a Palindrom'