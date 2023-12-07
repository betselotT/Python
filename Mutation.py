NinA = int(input())
A = set(map(int, input().split()))
N = int(input())
command = []
for i in range(N * 2):
    command.append(input().split())
for i in range(N * 2):
    print(command[i])
i = 0
while i < len(command):
    command, *elements = command[i+1]
    elements = set(map(int, elements))
    if command == 'update':
        A.update(map(int, elements))
    elif command == 'intersection_update':
        A.intersection_update(map(int, elements))
    elif command == 'symmetric_difference_update':
        A.symmetric_difference_update(map(int, elements))
    elif command == 'difference_update':
        A.difference_update(map(int, elements))
    i += 2
ans = sum(A)
print(ans)