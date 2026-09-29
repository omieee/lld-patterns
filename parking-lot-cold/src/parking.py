from enum import Enum


class ParkingSlots(Enum):
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"


class ParkingStatus(Enum):
    VACANT = "VACANT"
    BOOKED = "BOOKED"


class ParkingLot:
    def create_parking_lot(
        self, no_of_floors: int, no_of_slots_per_floor: int, id: str = "PR1234"
    ) -> dict:
        output = {
            "id": id,
            "nof": no_of_floors,
            "nospf": no_of_slots_per_floor,
            "floors": [],
        }

        for _ in range(1, no_of_floors + 1):
            current_floor_slots = []
            for sl in range(1, no_of_slots_per_floor + 1):
                slot_data = self._generate_slot_data(sl)
                current_floor_slots.append(slot_data)
            output["floors"].append(current_floor_slots)

        return output

    def _generate_slot_data(self, slot_num: int) -> dict:
        """Helper to create baseline type mapping configurations."""
        if slot_num == 1:
            return {
                "type": ParkingSlots.LARGE,
                "status": ParkingStatus.VACANT,
                "vehicle": None,
            }
        elif slot_num in (2, 3):
            return {
                "type": ParkingSlots.SMALL,
                "status": ParkingStatus.VACANT,
                "vehicle": None,
            }
        else:
            return {
                "type": ParkingSlots.MEDIUM,
                "status": ParkingStatus.VACANT,
                "vehicle": None,
            }

    def add_floor(self, lot_dict: dict, no_of_slots: int):
        new_floor = []
        for sl in range(1, no_of_slots + 1):
            new_floor.append(self._generate_slot_data(sl))
        lot_dict["floors"].append(new_floor)
        lot_dict["nof"] += 1

    def add_slot_to_floor(
        self, lot_dict: dict, floor_num: int, slot_type: ParkingSlots
    ):
        floor_idx = floor_num - 1
        if 0 <= floor_idx < len(lot_dict["floors"]):
            lot_dict["floors"][floor_idx].append(
                {"type": slot_type, "status": ParkingStatus.VACANT, "vehicle": None}
            )
