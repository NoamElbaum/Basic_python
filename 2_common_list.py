a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

if len(a) > len(b):
    L_list = a
    S_list = b
else:
    L_list = b
    S_list = a

duplicates = [None]*len(S_list)
i = 0

for x in range(len(L_list)):
    for y in range(len(S_list)):
        if L_list[x] == S_list[y]:
            duplicates[i] = L_list[x]
            L_list[x] = None
            i += 1

print(duplicates[0:i])