import random
import time

while 1:
    num = []
    while len(num) < 3:
        digit = str(int(random.uniform(0,9)))
        if digit in num:
            pass
        else:
            num.append(digit)

    print(num)

    match = 0
    close = False
    while 1:
        guess = input('Enter your guess for a 3 digit number: ')
        for i in range(3):
            if guess[i] == num[i]:
                match += 1
        if match == 0:
            for i in num:
                for x in guess:
                    if(i == x):
                        close = True
            if close:
                print('Close')
                close = False
            else:
                print('Nope')
        elif match == 3:
            break
        else:
            print('match')
            match = 0
    print('correct number')

