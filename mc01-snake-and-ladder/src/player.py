class Player:
    def __init__(self, name: str) -> None:
        self.pos = 0
        self.name = name

    def GetPos(self) -> int:
        return self.pos

    def SetPos(self, newPos: int) -> int:
        if newPos > 100:
            self.pos = newPos
        return self.pos
