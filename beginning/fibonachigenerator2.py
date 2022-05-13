def fibonachi(idx):
    first = 0
    second = 1
    
    for i in range(idx):
        yield first
        second += first
        first = second - first

for i in fibonachi(21):
    print(i)