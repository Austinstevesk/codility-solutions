def solution(a: int, b:int, c:int) -> str:
    a = {'char': 'a', 'count': a}
    b = {'char': 'b', 'count': b}
    c = {'char': 'c', 'count': c}
    
    letters = sorted([a,b,c], key=lambda x: x['count'])
    letters = list(filter(lambda x: x['count'] > 0, letters))
    res = ""
    lst = []
    
    while len(letters) > 0:
        #add the most frequent
        top = letters.pop()
        lst.append(top)
        
        if len(res) > 1 and top['char'] * 2 == res[-2:]:
            continue
        
        res += top['char']
        top['count'] -= 1
        
        while len(lst) > 0:
            item = lst.pop()
            if item['count'] > 0:
                letters.append(item)
                
        letters.sort(key=lambda x: x['count'])
        
    return res
    
    
print(solution(a=2, b=8, c=10))



from heapq import heappush, heappop
import heapq
def solution(a: int, b: int, c: int):
    res, maxHeap = "", []
    for count, char in [(-1, 'a'), (-b, 'b'), (-c, 'c')]:
        if count != 0:
            heapq.heappush(maxHeap, (count, char))
            
    while maxHeap:
        count, char = heapq.heappop(maxHeap)
        if len(res) > 1 and res[-1] == res[-2] == char:
            if not maxHeap:
                break
            count2, char2 = heapq.heappop(maxHeap)
            res+= char2
            count2 += 1
            if count2:
                heapq.heappush(maxHeap, (count2, char2))
                
        else:
            res += char
            count += 1
            
            
        if count:
            heapq.heappush(maxHeap, (count, char))
    return res
    
        
print(solution(a=1, b=1, c=7))