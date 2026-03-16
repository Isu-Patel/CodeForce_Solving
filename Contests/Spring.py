import sys
from math import gcd
input = sys.stdin.readline

def lcm(x, y):
    return x * y // gcd(x, y)

t = int(input())
for _ in range(t):
    a, b, c, m = map(int, input().split())
    
    ab = lcm(a, b)
    ac = lcm(a, c)
    bc = lcm(b, c)
    abc = lcm(ab, c)
    
    fa  = m // a
    fb  = m // b
    fc  = m // c
    fab = m // ab
    fac = m // ac
    fbc = m // bc
    fabc = m // abc
    
    # days each visits with both others
    # days alice visits with bob only (not carol)
    a_ab   = fab - fabc   # alice+bob, not carol
    a_ac   = fac - fabc   # alice+carol, not bob
    b_bc   = fbc - fabc   # bob+carol, not alice
    
    a_alone = fa - fab - fac + fabc
    b_alone = fb - fab - fbc + fabc
    c_alone = fc - fac - fbc + fabc
    
    alice = a_alone * 6 + (a_ab + a_ac) * 3 + fabc * 2
    bob   = b_alone * 6 + (a_ab + b_bc) * 3 + fabc * 2
    carol = c_alone * 6 + (a_ac + b_bc) * 3 + fabc * 2
    
    print(alice, bob, carol)
