import sys

n = int(sys.stdin.readline().rstrip())


def vps(text):
    result = 0

    for c in text:
        if c == '(':
            result += 1
        else:
            if result > 0:
                result -= 1
            else:
                return False

    return result == 0


for _ in range(n):
    text = sys.stdin.readline().rstrip()
    print('YES' if vps(text) else 'NO')
