"""
Function taking 2 arrays A and B, returns the minimal value occuring in both lists
"""

"""def solution(A,B):
	list1 = []
	for i in A:
		if i in B:
			list1.append(i)
			print(list1)
	if list1 == []:
		return -1
	else:
		return min(list1)"""

def solution(A, B):
    A.sort()
    B.sort()
    i = 0
    for a in A:
        if i < len(B) - 1 and B[i] < a:
            i += 1
        if a == B[i]:
        	print(a)
    if a != B[i]:
    	print(-1)
        


X = [1,3,2,1]
Y = [0,2,5,3,2]
solution(X,Y)