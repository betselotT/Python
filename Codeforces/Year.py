def calc(year):
    while True:
        year += 1
        if len(set(str(year))) == 4:
            print(year)
            break
year = int(input())
calc(year)