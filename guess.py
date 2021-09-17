import random 

print("Number Guessing Game")

number = random.randint(1,10)

print("Guess a number between 1 to 10")

chances = 0

while chances < 5:
    guess = int(input("Enter Your Guess : "))

    if guess == number:
        print("Congratulations You Won!, Your Guess was correct")
        break
    elif guess < number:
        print("The number you guessed is low, Guess a higher number")
    else:
        print("The number you guessed is higher, Guess a lower number")    
    chances += 1

    if not chances < 5:
        print("You Lose!!!, You took too many chances, The number is", number)
