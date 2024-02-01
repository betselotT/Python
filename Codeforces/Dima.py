def count(n, fingers_shown):
    total_fingers = sum(fingers_shown)
    count = 0

    for i in range(1, 6):
        if (total_fingers + i) % (n + 1) != 1:
            count += 1
    return count


n = int(input("Enter an integer: "))
fingers_shown = list(map(int, input().split()))
ways = count(n, fingers_shown)
print(ways)
