import sys

t, m = map(int, input().split())

memory = [0] * m
blocks = {}
next_id = 1

for _ in range(t):
    cmd = input().split()

    if cmd[0] == "alloc":
        n = int(cmd[1])

        pos = -1
        count = 0

        for i in range(m):
            if memory[i] == 0:
                count += 1
            else:
                count = 0

            if count == n:
                pos = i - n + 1
                break

        if pos == -1:
            print("NULL")
        else:
            for i in range(pos, pos + n):
                memory[i] = next_id

            blocks[next_id] = (pos, n)
            print(next_id)
            next_id += 1

    elif cmd[0] == "erase":
        x = int(cmd[1])

        if x not in blocks:
            print("ILLEGAL_ERASE_ARGUMENT")
        else:
            start, length = blocks[x]
            for i in range(start, start + length):
                memory[i] = 0
            del blocks[x]

    else:  # defragment
        new_memory = [0] * m
        idx = 0

        new_blocks = {}

        for bid in sorted(blocks.keys(), key=lambda x: blocks[x][0]):
            start, length = blocks[bid]

            for i in range(length):
                new_memory[idx + i] = bid

            new_blocks[bid] = (idx, length)
            idx += length

        memory = new_memory
        blocks = new_blocks