# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import deque
def deque_operations(line, dq):
    for i in range(len(line)):
        if i == 0:
            command = line[0]
        elif i == 1:
            parameter = line[1]
    
    if command == 'append':
        dq.append(parameter)
    elif command == 'pop':
        dq.pop()
    elif command == 'popleft':
        dq.popleft()
    elif command == 'appendleft':
        dq.appendleft(parameter)
    
dq = deque()
lines=int(input())
for _ in range(lines):
    line = input().split()
    deque_operations(line, dq)

print(*[x for x in dq], sep=' ')

    