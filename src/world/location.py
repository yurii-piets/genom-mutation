class Location:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def transform(self, transition_vector):
        return Location(self.x + transition_vector[0], self.y + transition_vector[1])

    def __repr__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
