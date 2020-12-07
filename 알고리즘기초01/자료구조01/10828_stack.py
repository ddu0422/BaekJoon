import sys

n = int(sys.stdin.readline().rstrip())
stack = []

for _ in range(n):
    commands = sys.stdin.readline().rstrip().split()
    command = commands[0]

    if len(commands) > 1:
        value = commands[1]

    if command == 'push':
        stack.append(value)
    elif command == 'pop':
        print(stack.pop() if len(stack) else -1)
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        print(0 if len(stack) else 1)
    elif command == 'top':
        print(stack[len(stack) - 1] if len(stack) else - 1)
