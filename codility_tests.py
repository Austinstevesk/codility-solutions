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




 #PostgreSQL
"""SELECT g1.country,g1.sumofimporter,g2.sumofexporter
from(SELECT c.country, COALESCE(sum(t1.value), 0) as sumofimporter from companies c full
outer join trades t1 on seller t1.seller = c.name group by c.country order by c.country ASC
)g1 join(SELECT c.country, COALESCE(sum(t2.value), 0) as sum of exporter from companies
c full outer join trades t2 on buyer = c.name group by c.country order by c.country ASC
)g2 on g2.country = g1.country"""




