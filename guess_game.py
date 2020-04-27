import random

userInput = '0'
exactly = 0
above = 0
below = 0

while userInput.lower != 'exit':

    num = int(random.uniform(0, 10))
    userInput = input(f"To play guess a number between 0-10\nEnter exit to stop\n")

    if userInput.isdigit():
        userInputInt = int(userInput)
        if num == userInputInt:
            exactly += 1
        elif num < userInputInt:
            above += 1
        else:
            below +=1
    print(f"num equal: {num}"
          f"\n")
    print(f"Num of exact guesses: {exactly}\nNum of high guesses: {above}\nNum of low guesses: {below}\n")


