Neng = int(input("Enter number English"))
eng = list(input().split())
Nfr = int(input("Enter number French"))
fr = list(input().split())
a = set(eng)
b = set(fr)

answer = a.intersection(b)
print(len(answer))
