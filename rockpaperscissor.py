player1=str(input("enter 1st player choice"))
player2=str(input("enter 2nd player choice"))

if(player1=="rock" or player1=="ROCK" or player1=="Rock"):
    if(player2=="scissor"):
        print("player1 is the winner")
    if(player2=="paper"):
        print("player2 is the winner")

if(player1=="scissor" or player1=="SCISSOR" or player1=="Scissor"):
    if(player2=="rock"):
        print("player2 is the winner")
    if(player2=="paper"):
        print("player1 is the winner")

if(player1=="paper" or player1=="PAPER" or player1=="Paper"):
    if(player2=="rock"):
        print("player1 is the winner")
    if(player2=="scissor"):
        print("player2 is the winner")