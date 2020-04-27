while 1:
    num = int(input("enter a positive num: "))

    if (num <= 0) :
      print("the number is negative")
    else:
        fib = [0] * (num + 1)
        fib[1] = 1
        some = fib[0] + fib[1]

        for i in range(2, num + 1):
            fib[i] = fib[i - 1] + fib[i - 2]
            some = some + fib[i]
        print(f"the fibonachi sum of {num} is {some}")