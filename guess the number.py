# comparison between player1 and player2
def result():
    if (a < i):
        print("player2 is winner of the game.")
    elif (a > i):
        print("player1 is winner of the game.")
    else:
        print("the game is draw.")
# when player1 is guessing the  number
a = 0
def player2():
    player2 = int(input("enter no of digits present in the number:"))
    player2_low = int(input(f"enter lowest value of {player2}digits number:"))
    player2_high = int(input(f"enter the highest value of {player2}digits number :"))
    import random
    player2_number = random.randrange(player2_low, player2_high)
    player2_digit = str(player2_number)
    def guess_player1():
        player1_number = input("guess the number: ")
        global a
        if (player1_number == player2_digit):
            a = a + 1
            while (1):

                if (a == 1):
                    print("player2 is mastermind.")

                else:
                    print(f"no of total iterations of player1 is:{a}")
                break
            result()
        elif (player1_number != player2_digit):
            a = a + 1
            p = 0
            k = len(player1_number)
            for q in range(k):
                if (player1_number[q] == player2_digit[p]):
                    print(f"matched digit of player2 at {q}th index is:{player1_number[p]}")
                p = p + 1
            guess_player1()
    guess_player1()
# when player 2 is guessing the game
player1 = int(input("enter no of digits present in the number:"))
player1_low = int(input(f"enter lowest value of {player1}digits number:"))
player1_high = int(input(f"enter the highest value of {player1}digits number :"))
import random
player1_number = random.randrange(player1_low, player1_high)
player1_digit = str(player1_number)
i = 0
def guess_player2():
    player2_number = input("guess the number: ")
    global i
    if (player2_number == player1_digit):
        i = i + 1
        while (1):
            if (i == 1):
                print("player2 is mastermind.")

            else:
                print(f"no of total iterations of player2 is:{i}")
            break
        player2()
    elif (player2_number != player1_digit):
        i = i + 1
        n = 0
        j = len(player2_number)
        for m in range(j):
            if (player2_number[m] == player1_digit[n]):
                print(f"matched digit of player2 at {m}th index is:{player2_number[m]}")
            n = n + 1
        guess_player2()
guess_player2()
def result():
    if (a < i):
        print("player2 is winner of the game.")
    elif (a > i):
        print("player1 is winner of the game.")
    else:
        print("the game is draw.")
