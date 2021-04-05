import random
def play():
    user=input("\nPlease enter your choice? 'r' for rock, 'p' for paper and 's' for scissor\n")
    computer=random.choice(['r','p','s'])
    print(f"Computer\'s choice is:\n{computer}")

    if user==computer:
        return "\nIt\'s a tie!"

    if is_win(user,computer):
        return "\nYou won!"

    return "\nYou lost!"

def is_win(player1,player2):
        if(player1=='r' and player2=='s') or (player1=='s' and player2=='p') or (player1=='p' and player2=='r'):
            return True

print(play())

