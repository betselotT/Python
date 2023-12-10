again = True
while again:
    choice1 = input("Player 1, please enter your choice (Rock, Paper or Scissors): ")
    choice2 = input("Player 2, please enter your choice (Rock, Paper or Scissors): ")
    if choice1 == 'Rock':
        if choice2 == 'Paper':
            print("Player 2 wins!")
            print("Want to start a new game?")
            choice = input("Enter yes or no: ")
            if choice == 'yes':
                    again = True
            else:
                    break
        elif choice2 == 'Scissors':
            print("Player 1 wins!")
            print("Want to start a new game?")
            choice = input("Enter yes or no: ")
            if choice == 'yes':
                again = True
            else:
                break
        elif choice2 == 'Rock':
            print("It is a draw!")
            print("Want to start a new game?")
            choice = input("Enter yes or no: ")
            if choice == 'yes':
                again = True
            else:
                break
    elif choice1 == 'Paper':
        if choice2 == 'Paper':
            print("It is a draw!")
            print("Want to start a new game?")
            choice = input("Enter yes or no: ")
            if choice == 'yes':
                again = True
            else:
                break
        elif choice2 == 'Scissors':
            print("Player 2 wins!")
            print("Want to start a new game?")
            choice = input("Enter yes or no: ")
            if choice == 'yes':
                again = True
            else:
                break
        elif choice2 == 'Rock':
            print("Player 1 wins!")
            print("Want to start a new game?")
            choice = input("Enter yes or no: ")
            if choice == 'yes':
                again = True
            else:
                break
    elif choice1 == 'Scissors':
        if choice2 == 'Paper':
            print("Player 1 wins!")
            print("Want to start a new game?")
            choice = input("Enter yes or no: ")
            if choice == 'yes':
                again = True
            else:
                break
        elif choice2 == 'Scissors':
            print("It is a draw!")
            print("Want to start a new game?")
            choice = input("Enter yes or no: ")
            if choice == 'yes':
                again = True
            else:
                break
        elif choice2 == 'Rock':
            print("Player 2 wins!")
            print("Want to start a new game?")
            choice = input("Enter yes or no: ")
            if choice == 'yes':
                again = True
            else:
                break
    else:
        print("Please only enter from among the three choices!")
        again
