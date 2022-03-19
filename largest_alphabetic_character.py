def solution(S):
    splitted_str = list(S)
    print(splitted_str)
    
    lowercase = [False] * 26
    uppercase = [False] * 26
    
    for c in splitted_str:
        if c.islower():
            lowercase[ord(c) - ord('a')] = True
        if c.isupper():
            uppercase[ord(c) - ord('A')] = True
            
    for i in range(25, -1, -1):
        if uppercase[i] and lowercase[i]:
            return chr(i + ord('A')) + ""
                
    return 'No'


print(solution('aaBaCaDedaFjf'))