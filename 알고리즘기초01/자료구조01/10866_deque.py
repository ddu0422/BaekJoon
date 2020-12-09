import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
queue = deque()

for _ in range(n):
    commands = sys.stdin.readline().rstrip().split()
    command = commands[0]

    if len(commands) > 1:
        value = commands[1]

    if command == 'push_front':
        queue.appendleft(value)

    if command == 'push_back':
        queue.append(value)

    if command == 'pop_front':
        print(queue.popleft() if queue else -1)

    if command == 'pop_back':
        print(queue.pop() if queue else -1)

    if command == 'size':
        print(len(queue))

    if command == 'empty':
        print(0 if queue else 1)

    if command == 'front':
        print(queue[0] if queue else -1)

    if command == 'back':
        print(queue[-1] if queue else -1)
