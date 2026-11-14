from mp02.src.mp02_practice import MP02_practice


def test_mp02_practice() -> None:
    SAMPLE = [
        "3",
        "T1 Anita Maths",
        "T2 Ravi Science",
        "T3 Meena English",
        "2",
        "R101 40",
        "R102 30",
        "4",
        "C1 T1 R101 Mon 9",
        "C2 T2 R102 Mon 10",
        "C3 T3 R101 Tue 9",
        "C4 T1 R102 Wed 11",
    ]
    mp02 = MP02_practice()
    assert (
        3,
        2,
        4,
        "T3 Meena English",
        "R102 30",
        "C4 T1 R102 Wed 11",
    ) == mp02.validate_sample(SAMPLE)


def test_mp02_practice_3() -> None:
    NO_ROOMS = [
        "2",
        "T1 Anita Maths",
        "T2 Ravi Science",
        "0",
        "1",
        "C1 T1 R101 Mon 9",
    ]
    mp02 = MP02_practice()
    assert (2, 0, 1, "T2 Ravi Science", "", "C1 T1 R101 Mon 9") == mp02.validate_sample(
        NO_ROOMS
    )
