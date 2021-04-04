import random
def play():
    user=input("Please enter your choice? 'r' for rock, 'p' for paper and 's' for scissor\n")
    computer=random.choice(['r','p','s'])
    print(computer)
play()
