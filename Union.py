Neng = int(input())
eng = list(input().split())
Nfr = int(input())
fr = list(input().split())

s1 = set(eng)
s2 = set(fr)
print(len(s1.union(s2)))