#Python
"""Given 2 strings S and C. S represents a table in CSV format where rows are separated by new line characters('\n') and
each row consists of one or more fields separated by commas(',').
Write a function which gived 2 strings S and C consisting of N and M characters, respectively,returns the maximum value
in that column."""

S = "city,temp2,temp\nParis,7,-3\nDubai,4,-4\nPorto.-1,-2"
C = "temp"

from io import StringIO
from csv import reader

def solution(S,C):
    mylist = []
    list_data = [row.split(',') for row in S.split('\n')]
    print(list_data)
    dict_data = {col:[list_data[j+1][i] for j in range(len(list_data)-1)] for i, col in enumerate(list_data[0])}
    for i in dict_data[C]:
        mylist.append(int(i))
    
    print(max(mylist))
    
    return max(mylist)
#solution(S,C)

"""
Picks a riddle of random values from random. If a character in the 
riddle is "?" it is replaced by random letters. The first character
should not be similar to the second and the last should not be similar
to the second last. Also, no 2 characters should be consecutive"""

import random
import string
random_values = list(string.ascii_lowercase)
def solution(riddle):
	riddle_split = []
	riddle_split[:0] = riddle
	print("riddle_split",riddle_split)
	for i in riddle_split:
		if i == '?':
			i_index = riddle_split.index(i)
			riddle_split[i_index] = random.choice(random_values)
			if riddle_split[i_index] == 0:
				if riddle_split[i_index] == riddle_split[i_index+1]:
					riddle_split[i_index] = random.choice(random_values)
				else:
					pass

			elif riddle_split[i_index] == riddle_split[-1]:
				if riddle_split[i_index] == riddle_split[i_index-2]:
					riddle_split[i_index] = random.choice(random_values)
				else:
					pass

			else:
				 if riddle_split[i_index] == riddle_split[i_index+1] or riddle_split[i_index] == riddle_split[i_index-1]:
				 	riddle_split[i_index] = random.choice(random_values)

				 else:
				 	pass



			print(riddle_split)
			finished_string = ''.join(riddle_split)
			print(finished_string)


	

solution("a?vcs?fga?")


"""
Counting the values iterated in a list A to get to a value greater
than the mean of the values in the list A"""
from statistics import mean
def solution(A):
	avg = mean(A)
	count = 0 
	for i in A:
		while i < avg:
			i = i+1
			count = count + 1
	return count


 #PostgreSQL
"""SELECT g1.country,g1.sumofimporter,g2.sumofexporter
from(SELECT c.country, COALESCE(sum(t1.value), 0) as sumofimporter from companies c full
outer join trades t1 on seller t1.seller = c.name group by c.country order by c.country ASC
)g1 join(SELECT c.country, COALESCE(sum(t2.value), 0) as sum of exporter from companies
c full outer join trades t2 on buyer = c.name group by c.country order by c.country ASC
)g2 on g2.country = g1.country"""




