from enum import Enum


class VehicleType(Enum):
    CAR = "CAR"
    BIKE = "BIKE"
    TRUCK = "TRUCK"


class Vehicle:
    def __init__(self, vehicle_type: str, reg_no: str, color: str) -> None:
        self.vehicleType = vehicle_type  # Raw string matching "CAR", "BIKE", "TRUCK"
        self.reg_no = reg_no
        self.color = color
