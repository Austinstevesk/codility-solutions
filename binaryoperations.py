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