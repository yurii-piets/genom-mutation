class Location:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def transform(self, tupl):
        return Location(self.x + tupl[0], self.y + tupl[1])

    def __repr__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
