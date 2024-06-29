"""ROCK PAPER SCISSOR GAME
Winning Rules as follows:
Rock vs paper-> paper wins
Rock vs scissor-> Rock wins
paper vs scissor-> scissor wins."""
import random
user=input("put options  separated by comma:")
i=user.split(",")
print(i)
user1=random.choice(i)
print(f"user 1 option is:{user1}")
user2=input("user 2 option among rock,paper,scissor is:")
if(user1=="rock" and user2=="paper"):
    print("user2 wins")
elif(user1=="rock" and user2=="scissor"):
    print("user1 wins")
elif(user1=="paper" and user2=="scissor"):
    print("user2 wins")
elif(user1=="paper" and user2=="rock"):
    print("user1 wins")
elif(user1=="scissor" and user2=="rock"):
    print("user2 wins")
elif(user1=="scissor" and user2=="paper"):
    print("user1 wins")
else:
    print("nobody wins")