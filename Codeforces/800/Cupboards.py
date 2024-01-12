def minimum_seconds(n, cupboard_info):
    left_open = 0
    right_open = 0

    for i in range(n):
        l, r = cupboard_info[i]
        left_open += l
        right_open += r

    min_left = min(left_open, n - left_open)
    min_right = min(right_open, n - right_open)

    print(min_left + min_right)


n = int(input("Enter the numbers: "))
cupboard_info = []
for i in range(n):
    l, r = map(int, input().split())
    cupboard_info.append((l, r))
result = minimum_seconds(n, cupboard_info)
