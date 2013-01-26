test_cases=int(raw_input())
answers=[]
def get_first_line():
	n,k=raw_input().split(" ")
	return int(n),int(k)
def get_second_line():
	a,b,c,r=raw_input().split(" ")
	return int(a),int(b),int(c),int(r)
def get_input():
	n,k=get_first_line()
	print (n,k)
	a,b,c,r=get_second_line()
	print (a,b,c,r)
for i in xrange(test_cases): get_input()

