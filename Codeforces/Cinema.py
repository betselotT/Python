def can_sell_tickets(n, bills):
    count_25 = 0
    count_50 = 0

    for bill in bills:
        if bill == 25:
            count_25 += 1
        elif bill == 50:
            if count_25 > 0:
                count_25 -= 1
                count_50 += 1
            else:
                return "NO"
        else:
            if count_50 > 0 and count_25 > 0:
                count_50 -= 1
                count_25 -= 1
            elif count_25 >= 3:
                count_25 -= 3
            else:
                return "NO"

    return "YES"


n = int(input())
bills = list(map(int, input().split()))

result = can_sell_tickets(n, bills)
print(result)
