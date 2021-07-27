class Graph():
    def __init__(self, size):
        self.adj = [ [0] * size for i in range(size)]
        self.size = size

