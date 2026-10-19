import sys

from src.parking import ParkingLot, ParkingSlots
from src.parking_manager import ParkingManager
from src.vehicle import Vehicle, VehicleType


def main():
    pl = ParkingLot()
    manager = None
    # Track the active structural dictionary reference locally
    cpl = None

    for line in sys.stdin:
        parts = line.split()
        if not parts:
            continue
        cmd, args = parts[0], parts[1:]

        if cmd == "exit":
            break

        elif cmd == "create_parking_lot":
            lot_id = str(args[0])
            nof = int(args[1])
            nosf = int(args[2])
            cpl = pl.create_parking_lot(nof, nosf, lot_id)
            manager = ParkingManager(cpl)
            print(
                f"Created parking lot with {cpl['nof']} floors and {cpl['nospf']} slots per floor"
            )

        elif cmd == "add_floor":
            if cpl and pl:
                no_of_slots = int(args[0])
                pl.add_floor(cpl, no_of_slots)
                print(f"Added floor to parking lot. Total floors now: {cpl['nof']}")

        elif cmd == "add_slot_to_floor":
            if cpl and pl:
                floor_num = int(args[0])
                # Convert string token (e.g. "small", "medium", "large") to Enum variant
                raw_slot_type = str(args[1]).upper()
                try:
                    slot_type = ParkingSlots[raw_slot_type]
                    pl.add_slot_to_floor(cpl, floor_num, slot_type)
                    print(f"Added slot of type {slot_type.name} to Floor {floor_num}")
                except KeyError:
                    print(f"Invalid slot type: {args[1]}")

        elif cmd == "park_vehicle":
            if manager:
                v_type, reg_no, color = args[0], args[1], args[2]
                vehicle = Vehicle(v_type, reg_no, color)
                result = manager.park_vehicle(vehicle)
                if result == "Parking Lot Full":
                    print(result)
                else:
                    print(f"Parked vehicle. Ticket ID: {result}")

        elif cmd == "unpark_vehicle":
            if manager:
                ticket_id = args[0]
                result = manager.unpark_vehicle(ticket_id)
                print(result)

        elif cmd == "display" and manager:
            display_type, vehicle_type = args[0], args[1]
            if vehicle_type in VehicleType.__members__:
                if display_type == "free_count":
                    manager.display_free_count(vehicle_type)
                elif display_type == "free_slots":
                    manager.display_free_slots(vehicle_type)
                elif display_type == "occupied_slots":
                    manager.display_occupied_slots(vehicle_type)
            else:
                print(f"Vehicle type {vehicle_type} is invalid")


if __name__ == "__main__":
    main()
