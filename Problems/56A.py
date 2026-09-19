import sys

input = sys.stdin.readline

alcohol = {
    "ABSINTH", "BEER", "BRANDY", "CHAMPAGNE",
    "GIN", "RUM", "SAKE", "TEQUILA",
    "VODKA", "WHISKEY", "WINE"
}

n = int(input())
ans = 0

for _ in range(n):
    x = input().strip()

    if x.isdigit():
        if int(x) < 18:
            ans += 1

    else:
        if x in alcohol:
            ans += 1

print(ans)