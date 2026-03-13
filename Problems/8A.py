s = input().strip()
s1 = input().strip()
s2 = input().strip()

def check(route):
    i = route.find(s1)
    if i == -1:
        return False
    j = route.find(s2, i + len(s1))
    return j != -1

forward = check(s)
backward = check(s[::-1])

if forward and backward:
    print("both")
elif forward:
    print("forward")
elif backward:
    print("backward")
else:
    print("fantasy")