def nearly(num):
    num_list = [int(digit) for digit in str(num)]
    count_four = num_list.count(4)
    count_seven = num_list.count(7)

    if count_four + count_seven == 4 or count_four + count_seven == 7:
        return "YES"
    else:
        return "NO"


num = int(input())
print(nearly(num))