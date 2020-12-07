import sys

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    words = sys.stdin.readline().rstrip().split()

    for word in words:
        print(word[::-1], end=" ")
    print()
