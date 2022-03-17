# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    new_stack = []
    splitted = S.split()
    print(splitted)
    for x in splitted:
        if x.isdigit():
            new_stack.append(int(x))

        elif x == 'DUP':
            if len(new_stack) > 0:
                y = new_stack[-1]
                new_stack.append(y)
            else:
                return -1

        elif x == 'POP':
            if len(new_stack) > 0:
                new_stack.pop()
            else:
                return -1

        elif x == '+':
            if len(new_stack) < 2:
                return -1
            else:
                y = new_stack.pop()
                z = new_stack.pop()

                my_sum = y+z
                
                if 0 <= my_sum < (2**20) - 1:
                    new_stack.append(my_sum)
                else:
                    return -1

        elif x == '-':
            if len(new_stack) < 2:
                return -1
            else:
                y = new_stack.pop()
                z = new_stack.pop()

                my_res = y - z

                if 0 <= my_res < (2**20) -1:
                    new_stack.append(my_res)
                else:
                    return -1

        if len(new_stack) == 0:
            return -1
        else:
            return new_stack[-1]
print(solution('3 5 7 - 7 +'))
print(solution('6 7 DUP POP + 8 -'))