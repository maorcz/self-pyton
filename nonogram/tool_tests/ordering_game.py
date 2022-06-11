from functools import total_ordering


@total_ordering
class Data:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):

        # Changing the functionality
        # of equality operator
        return self.value != other.value


# Driver code
print(Data(2) < Data(3))
print(Data(2) > Data(3))
print(Data(3) == Data(3))
print(Data(3) == Data(5))
