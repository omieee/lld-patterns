### Purpose
The purpose of this applicastion is to manage vehical parking, once a vehicle arrives it gets a ticket which has a proper slot mentioned in it and when the vehicle checksout the bill is calculated based on number of hours

### Key Entities
- ParkingLot: This is the parking place it can be single or multistoried
- ParkingSlot: These are the individual slots where a vehicle can park
- ParkingSlots: This is the group of all slots within a ParkingLot
- Vehicle: Three vehicle types are suported Bike, Car, Truck and chekin is handled by this Entitity
- Billing: This handles the final billing based on type and duration of stay, and marking the slot available 

### Class Definition (Class Variables)

```python
class ParkingLot
	self.name = name
	self.floors = floors
	self.total_slots = slots
	
class ParkingSlot:
	_parkinglot: ParkingLot,
	_slnumber: int,
	_slotfit: SLOT_FIT,
	_slfloor: int = 0,
	_slstatus: SLOT_STATUS = SLOT_STATUS.VACANT,

class ParkingSlots:
	parkingSlots = []
	
class Vehicle:
	vehcleType = vtype
	registrationNumber = reg
	parkingSlot = None
	entryTime = None
	
class Billing:
	
```

### Class FUnctinality

`ParkingLot`: This class is the first class that get instantiated and more like start of setup it takes name, numbe rof floors and total slots available in the parking space. It also has one getter property to get total slots count.

`ParkingSlot`: This class is the single most unit which represents the individual parking slot or spot. It has getter and a setter which returns the status and sets the status

`PatkingSlots`: This class is more like a helper class which keeps all the individual parking slot in a list for easy manipulation on them. this helps to achieve functionalities like to find which individual slot is vacant

`Vehicle`: This class has details of vehicle and also adds the vehicle to a slot if vacant upon checking in.

`Billing`: This class has just one function that is used at checkout it checks the time difference and generate the bil to be paid and also frees up the parking slot