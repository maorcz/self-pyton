class Fib():
    def __init__(self, num):
        if num >= 0:
            self.super_prev = 0
            self.prev = 1
            self.curr = 1
            self.num = num
        else:
            return Fib(self,num)

    def __iter__(self):
        return self

    def __next__(self):
        if (self.curr < self.num):
            self.curr = self.super_prev + self.prev
            self.super_prev = self.prev
            self.prev = self.curr 
            return self.curr
        raise StopIteration

fib = Fib(6765)
for i in fib:
    print(i)