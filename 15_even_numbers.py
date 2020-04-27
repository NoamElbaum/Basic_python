from number_generator import numbers

even = []

for n in range(numbers(40)):
    while 1:
        num = numbers(40)
        if num % 2 == 0:
            even.append(num)
            break
        else:
            num = numbers(40)
print(even)

