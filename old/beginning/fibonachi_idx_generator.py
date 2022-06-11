def fibonachi_val(val):
    first = 0
    second = 1

    while first < val:
        yield first
        first, second = second, second + first


def fibonachi_idx(idx):
    first = 0
    second = 1

    for _ in range(idx):
        yield first
        first, second = second, second + first


for t in enumerate(fibonachi_val(6765)):
    print(t)

for t in enumerate(fibonachi_idx(20)):
    print(t)
