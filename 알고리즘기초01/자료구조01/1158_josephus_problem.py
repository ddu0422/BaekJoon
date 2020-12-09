import sys
from collections import deque

n, k = map(int, sys.stdin.readline().rstrip().split())
queue = deque([i + 1 for i in range(n)])
result = []
count = 1

while queue:
    if count % k == 0:
        result.append(queue.popleft())
    else:
        queue.append(queue.popleft())

    count += 1

print('{0}{1}{2}'.format('<', ', '.join([str(c) for c in result]), '>'))
