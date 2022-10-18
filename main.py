import random

def play():
    player = ""

    print("Welcome to the game of rock paper scissors!")
    print("Exit the game? - press e")
    
    while player != 'e':
        player = input("Press r for rock, p for paper, s for scissors. What is your choice?")
        if player == 'e':
            exit()
        pc = random.choice(["r", "p", "s"])
        print(f"I choose {pc}")
        if player == pc:
            return "no winner"
        if player_win(player, pc):
            return "You won!"
        else:
            return "I won!"
    
def player_win(player, pc):
    if(player == 'r' and pc == 's') or (player == 's' and pc == 'p')or(player == 'p' and pc == 'r'):
        return True


if __name__=="__main__":
    for x in range(20):
        print(play())

exit()