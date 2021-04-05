import random

def play():
    # taking input from the user

    user = input("\nPlease enter your choice? 'r' for rock, 'p' for paper and 's' for scissor\n")

    computer = random.choice(['r', 'p', 's'])  # returns a randomly selected element from the list
    print(f"Computer\'s choice is:\n{computer}")

    # if user and computer both have same choices

    if user == computer:
        return "\nIt\'s a tie!"

    # calling is_win(player1,player2) to declare the result; if true, returns "You won", otherwise "You lost"

    if is_win(user, computer):
        return "\nYou won!"

    return "\nYou lost!"    #not used else to save an extra line


def is_win(player1, player2):
    # returns True if player1 wins
    # r > s, s > p, p > r

    if (player1 == 'r' and player2 == 's') or (player1 == 's' and player2 == 'p') or (
            player1 == 'p' and player2 == 'r'):
        return True

print(play())
