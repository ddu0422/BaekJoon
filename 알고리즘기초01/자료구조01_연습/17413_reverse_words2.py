import sys

words = sys.stdin.readline().rstrip()
has_angle_brackets = False
stack = []
result = []


def moveFromStackToResult():
    while stack:
        result.append(stack.pop())


for word in words:
    if not has_angle_brackets and word == ' ':
        moveFromStackToResult()
        result.append(' ')
        continue

    if word == '<':
        moveFromStackToResult()
        has_angle_brackets = True
    elif word == '>':
        result.append(word)
        has_angle_brackets = False
        continue

    if has_angle_brackets:
        result.append(word)
    else:
        stack.append(word)

moveFromStackToResult()

print(''.join(result))
