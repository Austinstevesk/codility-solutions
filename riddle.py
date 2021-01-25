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