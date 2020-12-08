import sys

n = int(sys.stdin.readline().rstrip())
current_number = 1
check = [False] * (n + 1)
stack = []
results = []

for _ in range(n):
    number = int(sys.stdin.readline().rstrip())

    # 이미 뺀 숫자라면 더 이상 뺄 수 없다.
    if check[number]:
        results = []
        break

    # 스택이 비어있거나 현재 숫자보다 큰 숫자가 입력되었다면 push한다.
    while current_number <= number:
        stack.append(current_number)
        results.append('+')
        current_number += 1

    # 스택의 top보다 작은 숫자가 주어질 경우 해상 숫자를 꺼낼 때 까지 pop한다.
    while len(stack) > 0 and stack[-1] >= number:
        check[stack.pop()] = True
        results.append('-')

if results:
    for c in results:
        print(c)
else:
    print('NO')
