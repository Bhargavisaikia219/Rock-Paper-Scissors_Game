import random

def play():
    user=input("Please enter your choice? 'r' for rock, 'p' for paper and 's' for scissor\n")
    computer=random.choice(['r','p','s'])
    print(computer)

    if user==computer:
        return "It\'s a tie!"
    else:
        if((user=='r' and computer=='s') or (user=='s' and computer=='p') or (user=='p' and computer=='r')):
            return "you won"
        else:
            return "you lost"


print(play())