import random
number = random.randint(1,25)
guess = int(input("Guess a number between 1 and 25 \nPlease enter a number: "))
while True:
    if(number<guess):
        guess = int(input("Decrease your number: "))
    if(number>guess):
        guess = int(input("Increase your number: "))
    else:
        print("You won!")
        break