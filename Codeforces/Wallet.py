def wallet(alice, bob):
    if (alice - bob) % 2 == 0:
        return "Bob"
    else:
        return "Alice"


n = int(input())
while n:
    a, b = map(int, input().split())
    print(wallet(a, b))
    n -= 1
# THis is a comment