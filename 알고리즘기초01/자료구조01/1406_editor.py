import sys

"""
[문제]
L : 커서 왼쪽으로 한 칸 옮김 (맨 앞이면 무시)
D : 커서 오른쪽으로 한 칸 옮김 (맨 뒤이면 무시)
B : 커서 왼쪽에 있는 문자 삭제 (맨 앞이면 무시)
P $ : $라는 문자를 커서 왼쪽에 추가

[결과]
편집기에 입력되어 있는 문자열 출력
"""

text = sys.stdin.readline().rstrip()
n = int(sys.stdin.readline().rstrip())
left_stack = [c for c in text]
right_stack = []

for _ in range(n):
    commands = sys.stdin.readline().rstrip().split()
    command = commands[0]

    if len(commands) > 1:
        value = commands[1]

    if command == 'L':
        if left_stack:
            right_stack.append(left_stack.pop())

    if command == 'D':
        if right_stack:
            left_stack.append(right_stack.pop())

    if command == 'B':
        if left_stack:
            left_stack.pop()

    if command == 'P':
        left_stack.append(value)

for c in left_stack:
    print(c, end="")

for c in right_stack[::-1]:
    print(c, end="")
