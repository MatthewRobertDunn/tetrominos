def Vector2d:
    def __init__(x,y):
        this.x = x
        this.y = y
    
    def add(self, other):
        return vector2d(self.x + other.x,self.y+other.y)
    

def Array2d:
    def __init__(x,y):
        self.width = x
        self.height = y
        self.grid =[None] * (x*y)

    def __getitem__(self, key):
        return self.grid[key.x + key.y*self.width]

    def __setitem__(self, key, value):
        self.grid[key.x + key.y*self.width] = value


def range2d(xMax, yMax = None):
    if yMax = None:
        xMax = yMax
    for x in range(xMax):
        for y in range(yMax):
            yield return Vector2d(x,y)