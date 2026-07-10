from functools import lru_cache

s = input()
n = len(s)

@lru_cache(None)
def dp(pos, used_at, last_letter):
    if pos == n:
        if used_at and last_letter:
            return ""
        return None

    best = None

    # Keep current character as a letter
    res = dp(pos + 1, used_at, True)
    if res is not None:
        best = s[pos] + res

    # Replace "at" with '@'
    if (not used_at) and pos != 0 and s.startswith("at", pos):
        res = dp(pos + 2, True, False)
        if res is not None:
            cur = "@" + res
            if (best is None or
                len(cur) < len(best) or
                (len(cur) == len(best) and cur < best)):
                best = cur

    # Replace "dot" with '.'
    if pos != 0 and s.startswith("dot", pos):
        res = dp(pos + 3, used_at, False)
        if res is not None:
            cur = "." + res
            if (best is None or
                len(cur) < len(best) or
                (len(cur) == len(best) and cur < best)):
                best = cur

    return best

print(dp(0, False, True))