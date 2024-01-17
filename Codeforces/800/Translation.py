def translate(s, t):
    if s == "".join(reversed(t)):
        return "YES"
    else:
        return "NO"

s = input()
t = input()
print(translate(s,t))