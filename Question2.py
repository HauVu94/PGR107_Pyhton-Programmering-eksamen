class Bug:
    def __init__(self, initialPosition):
        self.position = initialPosition
        self.direction = 1

    def turn(self):
        self.direction = - self.direction


    def move(self):
        self.position = self.position + self.direction

    def getPotition(self):
        return self.position


bug = Bug(0)

bug.move()
bug.turn()
bug.move()
bug.move()
print(bug.getPotition())
