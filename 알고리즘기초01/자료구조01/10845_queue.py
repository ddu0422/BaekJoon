import sys
from collections import deque

"""
[문제]
push X : 정수 X를 큐에 넣는다.
pop : 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력, 큐가 비어 있을 경우 -1을 출력
size : 큐에 크기
empty : 큐가 비어있으면 1, 아니면 0
front : 큐의 가장 앞에 있는 정수 출력, 큐가 비어 있을 경우 -1을 출력
back : 큐의 가장 뒤에 있는 정수를 출력, 큐가 비어 있을 경우 -1을 출력
"""

n = int(sys.stdin.readline().rstrip())
queue = deque()

for _ in range(n):
    commands = sys.stdin.readline().rstrip().split()
    command = commands[0]

    if len(commands) > 1:
        value = commands[1]

    if command == 'push':
        queue.append(value)

    if command == 'pop':
        print(queue.popleft() if queue else -1)

    if command == 'size':
        print(len(queue))

    if command == 'empty':
        print(0 if queue else 1)

    if command == 'front':
        print(queue[0] if queue else -1)

    if command == 'back':
        print(queue[-1] if queue else -1)
