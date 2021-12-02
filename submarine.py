from dataclasses import dataclass

@dataclass
class Submarine:

    x: int = 0
    y: int = 0
    z: int = 0

    def forward(self, dx: int):
        ...

    def backward(self, dx: int):
        ...

    def left(self, dy: int):
        ...

    def right(self, dy: int):
        ...

    def up(self, dz: int):
        ...

    def down(self, dz: int):
        ...

    def move(self, direction: str, distance: int):
        if direction == "forward":
            self.forward(distance)
        elif direction == "backward":
            self.forward(distance)
        elif direction == "left":
            self.left(distance)
        elif direction == "right":
            self.right(distance)
        elif direction == "down":
            self.down(distance)
        elif direction == "up":
            self.up(distance)


