import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    a = list(map(int, data[1:1 + n]))
    total = sum(a)
    if total % 2 != 0:
        print(0)
        return
    half = total // 2
    cnt = 0
    s = 0
    for i in range(n):
        s += a[i]
        if s == half:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()
    