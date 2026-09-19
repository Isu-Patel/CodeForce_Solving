import sys

s = input().strip()
n = len(s)

path = {}

answer = 0


def parse(pos):
    global answer

    start = pos
    while pos < n and s[pos] not in ':,.':
        pos += 1

    name = s[start:pos]

    answer += path.get(name, 0)

    path[name] = path.get(name, 0) + 1

    if pos < n and s[pos] == ':':
        pos += 1

        while True:
            pos = parse(pos)

            if s[pos] == ',':
                pos += 1
            else:
                break

    pos += 1

    path[name] -= 1
    if path[name] == 0:
        del path[name]

    return pos


parse(0)

print(answer)
