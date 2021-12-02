from dataclasses import dataclass
import abc

@dataclass
class Submarine:

    x: int = 0
    y: int = 0
    z: int = 0

    @abc.abstractmethod
    def forward(self, dx: int):
        raise NotImplementedError

    @abc.abstractmethod
    def backward(self, dx: int):
        raise NotImplementedError

    @abc.abstractmethod
    def left(self, dy: int):
        raise NotImplementedError

    @abc.abstractmethod
    def right(self, dy: int):
        raise NotImplementedError

    @abc.abstractmethod
    def up(self, dz: int):
        raise NotImplementedError

    @abc.abstractmethod
    def down(self, dz: int):
        raise NotImplementedError

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
