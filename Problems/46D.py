L, b, f = map(int, input().split())
n = int(input())

# parked cars: (start, end, request_id)
parked = []

# request_id -> (start, end)
placed = {}

for req in range(1, n + 1):
    t, x = map(int, input().split())

    if t == 1:
        length = x
        pos = -1

        if not parked:
            if length <= L:
                pos = 0
        else:
            # Before the first car
            if length + f <= parked[0][0]:
                pos = 0
            else:
                # Between cars
                for i in range(len(parked) - 1):
                    start = parked[i][1] + b
                    if start + length + f <= parked[i + 1][0]:
                        pos = start
                        break

                # After the last car
                if pos == -1:
                    start = parked[-1][1] + b
                    if start + length <= L:
                        pos = start

        print(pos)

        if pos != -1:
            end = pos + length
            car = (pos, end, req)

            # insert while keeping order
            idx = 0
            while idx < len(parked) and parked[idx][0] < pos:
                idx += 1
            parked.insert(idx, car)
            placed[req] = (pos, end)

    else:
        rid = x
        pos, end = placed.pop(rid)

        for i, car in enumerate(parked):
            if car[2] == rid:
                parked.pop(i)
                break