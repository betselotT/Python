def finish(pages, days):
    listOfDays = days.split(" ")
    count = 0
    indexchange = 0
    for i in range(len(listOfDays)):
        count += int(listOfDays[i])
        if count >= pages:
            indexchange += i+1
            break
    if count < pages and pages - count != 0:
        recursive_result = finish(pages - count, days)
    if indexchange != 0:
        print(indexchange)


n = int(input())
s = input()
finish(n, s)