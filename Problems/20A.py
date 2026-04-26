import sys


def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    path = data[0].strip()
    if not path:
        return

    result_chars = []
    prev_slash = False
    for ch in path:
        if ch == '/':
            if not prev_slash:
                result_chars.append(ch)
            prev_slash = True
        else:
            result_chars.append(ch)
            prev_slash = False

    normalized = ''.join(result_chars)
    if len(normalized) > 1 and normalized.endswith('/'):
        normalized = normalized.rstrip('/')

    sys.stdout.write(normalized)


if __name__ == '__main__':
    main()
