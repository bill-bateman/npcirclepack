
class Node():
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.next = None
        self.prev = None
        pass

    @classmethod
    def from_np(cls, index, pos):
        return cls(pos[index][0], pos[index][1], pos[index][2])

    def __str__(self):
        return f"({self.x},{self.y},{self.r})"