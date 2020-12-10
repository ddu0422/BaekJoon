import sys

iron_bar = sys.stdin.readline().rstrip()
result = 0
count = 0
previous = ''

for c in iron_bar:
    if c == '(':
        count += 1

    if c == ')':
        # ')'일 경우 '('의 개수를 빼주어야 한다.
        count -= 1
        if previous == '(':
            result += count
        else:
            result += 1

    previous = c

print(result)
