testcase1 = """5
ID         MARKS      NAME       CLASS     
1          97         Raymond    7         
2          50         Steven     4         
3          91         Adrian     9         
4          72         Stewart    5         
5          80         Peter      6   """

tc = testcase1.split('\n')

from collections import namedtuple
StudentData = namedtuple('StudentData', 'id,mark,name,course')
nos = int(tc[0])
print(sum(map(float,[student.mark for student in [StudentData(*tc[i].split()) for i in range(2,nos + 2)]]))/nos)
