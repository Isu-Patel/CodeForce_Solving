import sys

s = ''.join(sys.stdin.read().split())

stack = []
ans = []

i = 0

while i < len(s):
    if s.startswith("<table>", i):
        stack.append(0)
        i += 7

    elif s.startswith("</table>", i):
        cells = stack.pop()
        ans.append(cells)
        i += 8

    elif s.startswith("<td>", i):
        stack[-1] += 1
        i += 4

    elif s.startswith("</td>", i):
        i += 5

    elif s.startswith("<tr>", i):
        i += 4

    elif s.startswith("</tr>", i):
        i += 5

    else:
        i += 1

ans.sort()

print(*ans)