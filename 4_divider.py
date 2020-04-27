num = int(input('enter a num: '))

divisors = [None]*num
i = 0

for x in range(1,num):
    if num % x == 0:
        divisors[i] = x
        i += 1
print(divisors[0:i])