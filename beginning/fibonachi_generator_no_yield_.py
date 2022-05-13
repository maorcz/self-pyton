class FibVal():
    def __init__(self, val):
        if val < 0:
            raise Exception('fibonachi can\'t be negative')

        self.val = val
        self.first_value = 0
        self.second_val = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.val <= self.first_value:
            raise StopIteration

        self.second_val += self.first_value
        self.first_value = self.second_val - self.first_value
        return self.second_val - self.first_value


class FibIdx():
    def __init__(self, last_idx):
        if last_idx < 0:
            raise Exception('please enter a valid index value (>=0)')

        self.last_idx = last_idx
        self.first_val = 0
        self.second_val = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.last_idx <= 0:
            raise StopIteration

        self.last_idx -= 1
        self.second_val += self.first_val
        self.first_val = self.second_val - self.first_val
        return self.second_val - self.first_val


for t in enumerate(FibVal(6765)):
    print(t)

for t in enumerate(FibIdx(20)):
    print(t)
