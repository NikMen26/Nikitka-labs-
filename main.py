lst = [1, 2, 3, 4, 5]
summ = 0
for i in range(len(lst)):
    summ += lst[i] * (1 - 2 * (i % 2))
print(summ)
