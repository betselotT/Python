duration = int(input())
rows = 3
cols = duration
arr = []
for i in range(rows):
    row = []
    for j in range(cols):
        value = int(input(f"Enter value for row {i + 1}, column {j + 1}: "))
        row.append(value)
    arr.append(row)
for row in arr:
    print(row)