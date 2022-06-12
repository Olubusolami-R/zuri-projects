import random
game=['R','P','S']
game_dict={'R':'rock','P':'paper','S':'scissors'}

user=""
cpu=""
winner=""

while winner=="":
    user=input("Enter R for rock, P for paper or S for scissors: ").upper()
    while user not in game:
        user=input("You entered an invalid value. Enter R for rock, P for paper or S for scissors: ").upper()

    cpu=random.choice(game)
    #game logic
    if user=='R' and cpu=='P':
        winner='cpu'
    elif user=='S' and cpu=='R':
        winner='cpu'
    elif user=='P' and cpu=='S':
        winner='cpu'
    elif user==cpu:
        print("It's a tie")
        winner=""
    else:
        winner="user" #any other valid combination means the user wins

print("-------Results\nPlayer("+game_dict[user]+") : CPU("+game_dict[cpu]+")")

if winner=="cpu":   
    print("CPU won this round!")
else:
    print("You won this round!")