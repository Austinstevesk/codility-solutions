"""Given a string S of length N which encodes a non-negative number V in binary form. two types of operations may be performed
   on it to modify its value:

   if V is odd, subtract 1 from it
   if V is even, divide by 2

   These operations are performed until the value of V becomes 0

   For example, if string S = "011100", its value V initially is 28. the value of V would change as follows:


   * V = 28, which is even: divide by 2 to obtain 14
   * V = 14, which is even: divide by 2 to obtain 7
   * V = 7, which is odd: subtract 1 to obtain 6

   ....
   ...

   * V = 1, which is odd: subtract 1 to obtain 0
"""




def solution(S):
    counter = 0
    
    number = int(S, 2)
    print(number)
    
    while number >0:
        if number % 2 == 0:
            number = number//2
            counter+=1
            
        else:
            number = number - 1
            counter+=1

    return counter
    
print(solution('011100'))





"""An aray A consisting of N integers is given. A slice of that array is a pair of integers (P,Q) such that O<=P<=Q<N. A slice (P,Q) of
array A is called non-negative if all the elements A[P], A[P+1]....A[Q-1], A[Q] are non negative. The sum of a slice (P,Q) of array A is the
value A[P]+A[P+1]+...+A[Q-1]+A[Q]


Write a function that given an array A consisting of of N integers, returns the maximum sum of any non negative slice of that array. The function
should return -1 if there are no non-negative slices in the array"""
def solution(A):
    max_ending = max_slice = 0
    max_A = max(A)
    if max_A > 0:
        for i in range(len(A)):
            max_ending = max(0, max_ending + A[i])
            max_slice = max(max_slice, max_ending)
    else:
        max_slice = max_A
    return max_slice