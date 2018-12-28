import sys
import numpy
if sys.version_info[0]>=3: raw_input=input

def calc(gpa):
	score=[float(i) for i in raw_input().split()]
	coef=numpy.corrcoef(gpa,score)[0,1]
	return 0 if numpy.isnan(coef) else coef

for t in range(int(raw_input())):
	raw_input()
	gpa=[float(i) for i in raw_input().split()]
	m=max([calc(gpa),i1] for i 1in range(1,6))[1]
	print(m)