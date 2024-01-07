def bog(name):
    if len(name) % 2 == 0:
        return "CHAT WITH HER!"
    else:
        return "IGNORE HIM!"

name = set(input())
print(bog(name))