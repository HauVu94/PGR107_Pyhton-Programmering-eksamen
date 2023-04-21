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


bug = Bug(5)
print("move once")
bug.move()

print("turn to the left")
bug.turn()

print("move twice")
bug.move()
bug.move()

print("turn to the right")
bug.turn()

print("move four times")
bug.move()
bug.move()
bug.move()
bug.move()

print("expected bug position: 8")
print(f"actual bug position: {bug.getPotition()}")
