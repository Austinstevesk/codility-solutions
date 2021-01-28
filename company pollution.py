"""
An industrial company has N factories each producing some pollution every month. The company decided to
reduce the fume emissions using one or more filters. Every such filter reduces the pollution by half. 
When the second(subsequent) filter is applied, it again reduces by half the remaining pollution 
emitted after fitting the existing filter(s). You are given an array of N integers describing the
amount of pollution produced by the factories. Your tas is to find the minimum number of filters needed
to decrease the total sum of pollution by at least half.

Which given an array of integers A of length N, returns the minimum number of filters needed to reduce
the total pollution by half
"""



def solution(A):
	sum_of_list = sum(A)
	half_sum_of_list = sum_of_list/2
	perform = True
	count = 0
	while perform:
		max_value_of_Array = max(A)
		index_of_max = A.index(max_value_of_Array)
		A[index_of_max] = max_value_of_Array/2
		new_sum = sum(A)
		count +=1
		if new_sum <= half_sum_of_list:
			perform = False
	print(count)
	return count
solution([10,4,6,8])