def winner(letters):
    anton = letters.count('A')
    danik = letters.count('D')
    if anton > danik:
        return "Anton"
    elif danik > anton:
        return "Danik"
    else:
        return "Friendship"

n = int(input())
letters = input()
print(winner(letters))