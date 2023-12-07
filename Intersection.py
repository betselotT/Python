Neng = int(input())
eng = list(input().split())
Nfr = int(input())
fr = list(input().split())
a = set(eng)
b = set(fr)

answer = a.intersection(b)
print(len(answer))