while True:
    str = input('enter a str: ')

    check = False
    str_size = len(str)
    y = str_size-1

    if str_size % 2 == 0:
        for x in range(int(str_size/2)):
            if str[y] == str[x]:
                check = True
            else:
                check = False
                break
            y -= 1


    else:
        check = False
    if check:
        print("the str is a palindrome")
    else:
        print("the str is not a palindrome")