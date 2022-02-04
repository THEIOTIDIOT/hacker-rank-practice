# Uses zip to make tuples of each list of grades
# calculates an average for each tuple

# Enter your code here. Read input from STDIN. Print output to STDOUT
inp = """5 3
89 90 78 93 80
90 91 85 88 86  
91 92 83 89 90.5
"""

#i = list(map(int,input().split()))
i = inp.split('\n')

grades = list(map(int,i[0].split()))[0]
students = list(map(int,i[0].split()))[1]

students_grades = list()
for _ in range(students):
    students_grades += [list(map(float,i[1+_].split()))]

    
for course in zip(*students_grades):
    print(sum(course) / len(course))
