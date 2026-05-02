import sys

def is_valid_chat(C):
    return c.isalnum() or c == '_'

def is_valid_part(s, min_len=1, max_len=16):
    return min_len <= len(s) <= max_len and all(is_valid_chat(c) for c in s)

s = input().strip()

if s.count('@') != 1:
    print("No")
    sys.exit()

pos = s.find('@')
username = s[:pos]
hostname_part = s[pos + 1:]

if not is_valid_part(username):
    print("No")
    sys.exit()

if '/' in hostname_part:
    hostname, resource = hostname_part.split('/', 1)
    if not is_valid_part(resource):
        print("NO")
        sys.exit()
else:
    hostname = hostname_part
    resource = None

if not(1 <= len(hostname) <= 32):
    print("NO")
    sys.exit()

parts = hostname.split('.')
if not parts or any(not part for part in parts):
    print("NO")
    sys.exit()

for part in parts:
    if not is_valid_part(part):
        print("NO")
        sys.exit()

print("YES")
