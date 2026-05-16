# import sys

# def main():
#     data = sys.stdin.read().split()
#     if not data:
#         return
#     n = int(data[0])
#     a = list(map(int, data[1:1 + n]))
#     total = sum(a)
#     if total % 2 != 0:
#         print(0)
#         return
#     half = total // 2
#     cnt = 0
#     s = 0
#     for i in range(n):
#         s += a[i]
#         if s == half:
#             cnt += 1
#     print(cnt)

# if __name__ == '__main__':
#     main()
    

import sys
data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit(0)

n = data[0]
arr = data[1:]
total = sum(arr)
cnt = 0
prefix = 0
for i in range(n - 1):
    prefix += arr[i]
    if prefix * 2 == total:
        cnt += 1
print(cnt)
