### AI Contribution
1. AI contributed in creating the test case file for this
2. AI contributed in fixing the bug in `def _can_fit(`

### Purpose
The purpose of this application is to run a multi-floor parking lot from the command line. A lot is created with a fixed number of floors and slots. When a vehicle arrives it is parked in the first vacant slot that matches its type, and a ticket id is printed. When the vehicle leaves, that slot is marked vacant again. The program can also print free and occupied slots, and it can add a floor or a slot after the lot is created.

There is no hourly bill. Checkout only frees the slot and prints the vehicle registration number and color.

### Key Entities
- ParkingLot: Builds the lot. It does not hold the lot as its own state. It returns and later mutates a nested dictionary.
- ParkingSlots: An enum of slot sizes: SMALL, MEDIUM, LARGE. It is not a collection of slots.
- ParkingStatus: VACANT or BOOKED.
- Vehicle: Car, bike, or truck, identified by registration number and color.
- Ticket: A small class that formats `lotId_floor_slot`. The running program never constructs it. The ticket id is a plain string.
- ParkingManager: Finds a slot, parks, unparks, and prints free and occupied counts.

### Class Definition (Class Variables)

```python
class ParkingSlots(Enum):
	SMALL = "small"
	MEDIUM = "medium"
	LARGE = "large"

class ParkingStatus(Enum):
	VACANT = "VACANT"
	BOOKED = "BOOKED"

class ParkingLot:
	# no instance fields
	# create_parking_lot returns:
	# {
	#   "id": id,
	#   "nof": no_of_floors,
	#   "nospf": no_of_slots_per_floor,
	#   "floors": [[{ "type", "status", "vehicle" }, ...], ...]
	# }

class Vehicle:
	vehicleType = vehicle_type   # raw string "CAR" | "BIKE" | "TRUCK"
	reg_no = reg_no
	color = color

class Ticket:
	parking_lot_id = parking_lot_id
	floor = floor
	slot = slot
	ticket_id = f"{parking_lot_id}_{floor}_{slot}"

class ParkingManager:
	pl = parking_lot_dict
```

Slot shape inside each floor is fixed by slot number: slot 1 is LARGE, slots 2 and 3 are SMALL, every later slot is MEDIUM.

### Class Functionality

`ParkingLot`: `create_parking_lot` walks floors and slots and builds the dictionary above. `add_floor` appends another floor and increments `nof`. `add_slot_to_floor` appends one slot of a given size onto an existing floor. None of these methods keep the dictionary on the object. The caller in `main.py` holds it.

`Vehicle`: Stores type, registration number, and color. `VehicleType` is defined next to it and is never used. Type stays a string.

`Ticket`: Builds `ticket_id` from lot id, floor, and slot. Nothing imports this class. `park_vehicle` returns the same string by formatting it inline, and `unpark_vehicle` splits that string to find the slot.

`ParkingManager`: Owns the live dictionary. `park_vehicle` maps CAR to MEDIUM, BIKE to SMALL, and TRUCK to LARGE, scans floors in order for the first vacant slot of that size, marks it BOOKED, stores registration number and color on the slot, and returns `id_floor_slot`. If none is free it returns `"Parking Lot Full"`. `unpark_vehicle` parses the ticket string, checks the slot is BOOKED, clears it, and returns a message with registration number and color. Bad ids return `"Invalid Ticket"`. The three `display_*` methods print free counts, free slot numbers, and occupied slot numbers per floor.

`main.py`: Reads stdin commands (`create_parking_lot`, `park_vehicle`, `unpark_vehicle`, `display`, `add_floor`, `add_slot_to_floor`, `exit`) and prints the manager's results.

### Verdict till now

The command flow works for the cases covered by the tests: create a lot, park until a type is full, reject a bad ticket, and reflect a floor or slot added later. The structure underneath that flow has a few clear gaps.

1) The lot is a dictionary, not a model. `ParkingLot` is a builder. Floors and slots are lists of dicts. There is no `ParkingSlot` object, so status, size, and the parked vehicle have no type of their own. `add_slot_to_floor` also leaves `nospf` stale, so the stored slots-per-floor count no longer matches a floor that grew.
2) `Ticket` is unused. The requirement to issue a ticket is met only as a string. Unpark trusts that string, splits on `_`, and treats the slot coordinates as the ticket. Parking the same slot again reissues the same id. There is no open or closed ticket.
3) `ParkingManager` does the allocation, the occupancy update, the ticket parse, and the printing. `_reqired_slot_type` and `_can_fit` repeat the same CAR/BIKE/TRUCK mapping, and `_find_slot` takes a vehicle type it never reads.
4) `VehicleType` is dead. The fit rule is string comparisons in the manager.
5) There is still no bill. Checkout frees the slot and does not record entry time or duration.

### My Verdict

This pass gets the CLI behavior right and the tests lock that behavior in. The domain model is still thin: the ticket is a string, the slot is a dict, and one manager class both mutates the lot and prints it. Billing from the earlier parking-lot writeup is absent here, so this version solves park, unpark, and display, and stops there.

### Time taken

Total time to write my own code is 109 Minutes. then remaing 10-15 for AI assisted test

<hr>

### How to fix above issues

1) Make `ParkingLot` own its floors. Give each floor a list of `ParkingSlot` objects with size, status, and the vehicle currently in it. `create_parking_lot`, `add_floor`, and `add_slot_to_floor` should update that object, and `nospf` should be derived from the floor or updated when a slot is added.
2) Use `Ticket`. `park_vehicle` creates a ticket bound to the vehicle and the slot and returns its id. `unpark_vehicle` looks the ticket up, closes it, then marks the slot vacant. Stop splitting the id as the only record of the stay.
3) Keep `ParkingManager` as the entry point for `park_vehicle` and `unpark_vehicle`. Slot search and status changes belong on the lot or the slot. Display formatting belongs in `main.py`; the manager should return the counts and slot numbers.
4) Store `VehicleType` on `Vehicle` and use one fit rule. Drop the second copy of the CAR/MEDIUM, BIKE/SMALL, TRUCK/LARGE mapping.
5) If hourly billing is in scope for this problem, add a `Billing` class whose only job is to take a closed ticket and return the amount. Slot freeing stays in unpark, not in billing.
