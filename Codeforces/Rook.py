def chess(position):
    places = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    letter = list(position)[0]
    number = list(position)[1]
    for i in range(1,9):
        if letter + str(i) != position:
            print(letter + str(i))
    for i in places:
        if i + number != position:
            print(i + number)
n = int(input("Enter an integer: "))
while n:
    po = input()
    chess(po)
    n-=1