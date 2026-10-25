from src.board import Board
from src.player import Player
import random


def getInputs():
    """
        9
    62 5
    33 6
    49 9
    88 16
    41 20
    56 53
    98 64
    93 73
    95 75
    8
    2 37
    27 46
    10 32
    51 68
    61 79
    65 84
    71 91
    81 100
    2
    Gaurav
    Sagar
    """
    print(
        "Game detail enter, snake, ladder pos and player (Press Enter on an empty line to finish):"
    )
    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
    # multiline_string = "\n".join(lines)
    snake_head_tails = []
    ladder_top_bottom = []
    number_of_snakes = int(lines[0])
    number_of_ladder = int(lines[number_of_snakes + 1])
    player_1 = lines[-2]
    player_2 = lines[-1]

    for i in range(1, number_of_snakes + 1):
        snake_heads = str(lines[i]).split()[0]
        snake_tails = str(lines[i]).split()[1]
        snake_head_tails.append((int(snake_heads), int(snake_tails)))

    for i in range(number_of_ladder, number_of_ladder + 1):
        ladder_bottom = str(lines[i]).split()[0]
        ladder_head = str(lines[i]).split()[1]
        ladder_top_bottom.append((ladder_bottom, ladder_head))

    return (
        player_1,
        player_2,
        number_of_snakes,
        number_of_ladder,
        snake_head_tails,
        ladder_top_bottom,
    )


def roll_dice() -> int:
    return random.randint(1, 6)


def move_pos(
    pl: Player, snake_pos: list[tuple], ladder_pos: list[tuple], places_to_move: int
) -> int | None:
    if pl.GetPos() + places_to_move > 100:
        return None
    new_pos = pl.GetPos()
    for h, t in snake_pos:
        if pl.GetPos() + places_to_move == h:
            new_pos = t
        else:
            new_pos = pl.GetPos() + places_to_move

    for b, t in ladder_pos:
        if pl.GetPos() + places_to_move == b:
            new_pos = t
        else:
            new_pos = pl.GetPos() + places_to_move

    return new_pos


if __name__ == "__main__":
    bd = Board()
    bd.draw_board()
    player1, player2, no_sn, no_la, sht, ltb = getInputs()
    p1 = Player(player1)
    p2 = Player(player2)
    next_player = p1
    while p1.pos != 100 or p2.pos != 100:
        new_pos = roll_dice()
        move_pos(next_player, sht, ltb, new_pos)
