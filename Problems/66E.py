import sys
from collections import deque


def possible_starts(a, edge_cost):
    n = len(a)
    prefix = [0]
    for i in range(2 * n):
        prefix.append(prefix[-1] + a[i % n] - edge_cost[i % n])

    minima = deque()
    for i in range(1, n + 1):
        while minima and prefix[minima[-1]] >= prefix[i]:
            minima.pop()
        minima.append(i)

    possible = [False] * n
    for start in range(n):
        possible[start] = prefix[minima[0]] >= prefix[start]

        if minima[0] == start + 1:
            minima.popleft()

        next_index = start + n + 1
        while minima and prefix[minima[-1]] >= prefix[next_index]:
            minima.pop()
        minima.append(next_index)

    return possible


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    a = data[1:n + 1]
    b = data[n + 1:]

    clockwise = possible_starts(a, b)
    counterclockwise = possible_starts(a, b[-1:] + b[:-1])

    answer = [
        i + 1 for i in range(n)
        if clockwise[i] or counterclockwise[i]
    ]

    print(len(answer))
    print(*answer)


if __name__ == "__main__":
    main()