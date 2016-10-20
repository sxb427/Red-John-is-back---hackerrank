import math
def count(N):
	if N<4:
		return 1
	else:
		count = 0
		highest = (N/4)*4
		for i in range(0,highest+1,4):
			a = i/4
			b = N-i
			asum = math.factorial(a+b)/(math.factorial(a)*math.factorial(b))
			count = count + asum
	return count
def prime(n):
	temp = int(n**(0.5))
	alist = range(2,temp+1)
	count = 0
	for i in alist:
		if n%i == 0:
			count = 1
			break
	if count==0:
		return True
	else:
		return False
T = input()
for i in range(T):
	x = input()
	y = count(x)
	if y==1:
		print 0
	elif y==2:
		print 1
	else:
		asum = 0
		for i in range(3,y+1):
			if prime(i):
				asum = asum + 1
		print asum + 1























		


