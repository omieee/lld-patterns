from src.parking import ParkingSlots, ParkingStatus
from src.vehicle import Vehicle


class ParkingManager:
    def __init__(self, parking_lot_dict: dict) -> None:
        self.pl = parking_lot_dict

    def _reqired_slot_type(self, vt: str) -> ParkingSlots | None:
        if vt == "CAR":
            return ParkingSlots.MEDIUM
        elif vt == "BIKE":
            return ParkingSlots.SMALL
        elif vt == "TRUCK":
            return ParkingSlots.LARGE
        return None

    def _can_fit(self, vt: str, st: ParkingSlots) -> bool:
        # FIXED: Enforce exact 1:1 type mapping rule strictly
        st_val = st.value if hasattr(st, "value") else st
        return bool(
            (vt == "CAR" and st_val == "medium")
            or (vt == "BIKE" and st_val == "small")
            or (vt == "TRUCK" and st_val == "large")
        )

    def _find_slot(self, vehicle_type: str, slot_type: ParkingSlots) -> tuple[int, int]:
        for floor_num, current_floor in enumerate(self.pl["floors"], start=1):
            for slot_num, slot in enumerate(current_floor, start=1):
                if slot["status"] == ParkingStatus.VACANT and slot["type"] == slot_type:
                    return floor_num, slot_num
        return (-1, -1)

    def park_vehicle(self, vehicle: Vehicle) -> str:
        vt = vehicle.vehicleType
        rt = self._reqired_slot_type(vt)
        fl, sl = self._find_slot(vt, rt)

        if fl > -1:
            slot = self.pl["floors"][fl - 1][sl - 1]
            slot["status"] = ParkingStatus.BOOKED
            slot["vehicle"] = {"reg_no": vehicle.reg_no, "color": vehicle.color}
            return f"{self.pl['id']}_{fl}_{sl}"
        else:
            return "Parking Lot Full"

    def unpark_vehicle(self, ticket_id: str) -> str:
        try:
            parts = ticket_id.split("_")
            if len(parts) != 3 or parts[0] != self.pl["id"]:
                return "Invalid Ticket"
            floor_num = int(parts[1])
            slot_num = int(parts[2])
        except (ValueError, IndexError):
            return "Invalid Ticket"

        floor_idx = floor_num - 1
        slot_idx = slot_num - 1

        if not (0 <= floor_idx < len(self.pl["floors"])) or not (
            0 <= slot_idx < len(self.pl["floors"][floor_idx])
        ):
            return "Invalid Ticket"

        slot = self.pl["floors"][floor_idx][slot_idx]

        if slot["status"] == ParkingStatus.BOOKED and slot["vehicle"] is not None:
            vehicle_info = slot["vehicle"]
            slot["status"] = ParkingStatus.VACANT
            slot["vehicle"] = None
            return f"Unparked vehicle with Registration Number: {vehicle_info['reg_no']} and Color: {vehicle_info['color']}"
        else:
            return "Invalid Ticket"

    def display_free_count(self, vehicle_type: str):
        for floor_idx, current_floor in enumerate(self.pl["floors"], start=1):
            free_count = sum(
                1
                for slot in current_floor
                if slot["status"] == ParkingStatus.VACANT
                and self._can_fit(vehicle_type, slot["type"])
            )
            print(
                f"No. of free slots for {vehicle_type} on Floor {floor_idx}: {free_count}"
            )

    def display_free_slots(self, vehicle_type: str):
        for floor_idx, current_floor in enumerate(self.pl["floors"], start=1):
            free_slots = [
                str(slot_idx)
                for slot_idx, slot in enumerate(current_floor, start=1)
                if slot["status"] == ParkingStatus.VACANT
                and self._can_fit(vehicle_type, slot["type"])
            ]
            slots_str = ",".join(free_slots)
            print(f"Free slots for {vehicle_type} on Floor {floor_idx}: {slots_str}")

    def display_occupied_slots(self, vehicle_type: str):
        for floor_idx, current_floor in enumerate(self.pl["floors"], start=1):
            occupied_slots = [
                str(slot_idx)
                for slot_idx, slot in enumerate(current_floor, start=1)
                if slot["status"] == ParkingStatus.BOOKED
                and self._can_fit(vehicle_type, slot["type"])
            ]
            slots_str = ",".join(occupied_slots)
            print(
                f"Occupied slots for {vehicle_type} on Floor {floor_idx}: {slots_str}"
            )
