import random

if not (False):
    pass

def generate_num():
    num = []
    while len(num) < 3:
        digit = str(int(random.uniform(0,9)))
        if digit in num:
            pass
        else:
            num.append(digit)
    return "".join(num)

def test_guess(num, guess):
    if num == guess:
        return 1
    else:
        nope = True
        for i in range(3):
            if guess[i] == num[i]:
                print('Match')
                nope = False
            elif guess[i] in num:
                print('Close')
                nope = False
        if nope:
            print('Nope')
        return 0



while 1:
    num = generate_num()
    #debug
    #print(num)
    guess = input('Enter your guess for a 3 digit number: ')
    while not test_guess(num, guess):
        guess = input('Enter a new guess: ')
    print('Correct number!')


