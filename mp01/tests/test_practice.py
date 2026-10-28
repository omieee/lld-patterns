from mp01.src.practice import PracticeMp1

"""
books = [("B101", "S1"), ("B205", "S3"), ("B309", "S2"), ("B412", "S5")]
"""


def test_practice_when_book_id_is_b412() -> None:
    pr = PracticeMp1()
    assert "S5" == pr.find_shelf(
        [("B101", "S1"), ("B205", "S3"), ("B309", "S2"), ("B412", "S5")], "B412"
    )


def test_practice_when_match_is_2_nd_item() -> None:
    pr = PracticeMp1()
    assert "S3" == pr.find_shelf(
        [("B101", "S1"), ("B205", "S3"), ("B309", "S2"), ("B412", "S5")], "B205"
    )


def test_practice_when_match_is_not_there() -> None:
    pr = PracticeMp1()
    assert "Not Found" == pr.find_shelf(
        [("B101", "S1"), ("B205", "S3"), ("B309", "S2"), ("B412", "S5")], "BB01"
    )
