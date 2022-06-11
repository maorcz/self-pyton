class DataHolder:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value
