from enum import Enum


class SLOT_FIT(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class SLOT_STATUS(Enum):
    VACANT = 0
    TAKEN = 1


class VEHICLE_TYPE(Enum):
    BIKE = 1
    CAR = 2
    TRUCK = 3


RATE_MULTIPLIER = {"NORMAL": 1, "SURGE": 1.5}
RATE_CARD = {"MIN": 50, "AFTER_2_HOUR_PER_HOUR": 20}
