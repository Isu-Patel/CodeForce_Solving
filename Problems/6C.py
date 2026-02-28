import sys
input = sys.stdin.readline

n = int(input())
t = list(map(int, input().split()))

l = 0
r = n - 1

alice_time = 0
bob_time = 0

alice_count = 0
bob_count = 0

while l <= r:
    if alice_time <= bob_time:
        alice_time += t[l]
        alice_count += 1
        l += 1
    else:
        bob_time += t[r]
        bob_count += 1
        r -= 1

print(alice_count, bob_count)