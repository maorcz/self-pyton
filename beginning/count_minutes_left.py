from itertools import accumulate

sum = 0
min = int(input('pls enter min '))
while min != -1:
    sum += min
    min = int(input('pls enter min '))

print(sum, "minutes")
print(sum/60, "hours")
