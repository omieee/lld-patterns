class Board:
    def __init__(self) -> None:
        self.board_range = 100
        self.start_pos = 1
        self.end_pos = 100

    def draw_board(self) -> list:
        x = []
        for i in range(1, 101):
            x.append(i)
        return x
