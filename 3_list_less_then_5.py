ages = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_ages = [None] * len(ages)
i = 0
for x in range(len(ages)):
    if ages[x] < 5:
        new_ages[i] = ages[x]
        i += 1
print(new_ages[0:i])