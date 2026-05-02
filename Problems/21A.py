import sys

def is_valid_char(c):
    return c.isalnum() or c == '_'

def is_valid_part(s, min_len=1, max_len=16):
    return min_len <= len(s) <= max_len and all(is_valid_char(c) for c in s)

s = input().strip()

# Find @
if s.count('@') != 1:
    print("NO")
    sys.exit()

pos = s.find('@')
username = s[:pos]
hostname_part = s[pos+1:]

# Check username
if not is_valid_part(username):
    print("NO")
    sys.exit()

# Split hostname and resource
if '/' in hostname_part:
    hostname, resource = hostname_part.split('/', 1)
    if not is_valid_part(resource):
        print("NO")
        sys.exit()
else:
    hostname = hostname_part
    resource = None

# Check hostname length
if not (1 <= len(hostname) <= 32):
    print("NO")
    sys.exit()

# Split hostname by '.'
parts = hostname.split('.')
if not parts or any(not part for part in parts):  # no empty parts
    print("NO")
    sys.exit()

for part in parts:
    if not is_valid_part(part):
        print("NO")
        sys.exit()

print("YES")