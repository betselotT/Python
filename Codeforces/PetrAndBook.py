n = int(input())
count = 0
arr = []
for i in range(7):
    pages = int(input())
    arr.append(pages)
for i in range(len(arr)):
    if count != n:
        count += arr[i]
    else:
        print(arr[i])