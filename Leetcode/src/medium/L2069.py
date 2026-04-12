class Robot:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0
        self.p = 0
        self.i = True

    def step(self, num: int) -> None:
        self.i = False
        self.p = (self.p + num) % (2 * self.width + 2 * self.height - 4)

    def getPos(self) -> List[int]:
        if self.p < self.width:
            return [self.p, 0]
        elif self.p < self.width + self.height - 1:
            return [self.width - 1, self.p - self.width + 1]
        elif self.p < 2 * self.width + self.height - 2:
            return [self.width - 1 - (self.p - (self.width + self.height - 2)), self.height - 1]
        else:
            return [0, self.height - 1 - (self.p - (2 * self.width + self.height - 3))]

    def getDir(self) -> str:
        if (self.p != 0 and self.p < self.width) or self.i:
            return 'East'    
        elif self.p != 0 and self.p < self.width + self.height - 1:
            return 'North'
        elif self.p != 0 and self.p < 2 * self.width + self.height - 2:
            return 'West'
        else:            
            return 'South'


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()