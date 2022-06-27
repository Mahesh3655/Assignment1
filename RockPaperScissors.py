import getpass
def main():
    n = input("Do you want to play a game Y/N :")
    while n == "Y" or n == 'y':
        player1 = getpass.getpass("Player1 enter your choice : ")
        player2 = getpass.getpass("Player2 enter your choice : ")
        player1 = player1.lower()
        player2 = player2.lower()
        try:
            l = ["rock","paper","scissors"]
            if player1 not in l or player2 not in l:
                raise Exception
            if player1 == player2:
                print("Its a Tie")
            elif player1 == "rock" and player2 == "scissors":
                print("Congratulations.....! Player1")
            elif player1 == "paper" and player2 == "rock ":
                print("Congratulations.....! Player1")
            elif player1 == "scissors" and player2 == "paper":
                print("Congratulations.....! Player1")
            else :
                print("Congratulations.....! Player2")
            n = input("Do you want to play another game(Y|N) :")
        except:
            print("No Winner")
            n = input("Do you want to play another game(Y|N) :")
if __name__ == "__main__":
    main()

