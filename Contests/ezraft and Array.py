# Hello Eveyone hows there I am Isu posting todays contest question
# You can check it on github and I will post more contest question.
# So stay with me.
t = int(input())

for _ in range(t):
    n = int(input())

    if n == 1:
        print(1)
    elif n == 2:
        print(-1)
    else:
        ans = [1, 2, 3]
        x = 6
        while len(ans) < n:
            ans.append(x)
            x *= 2
        print(*ans)