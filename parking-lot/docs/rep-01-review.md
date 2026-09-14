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

<hr>

### Verdict till now

There were some serious mistake in the above architecture which after being pointed out trying to fix here

1) There are few classes which are doing too much and not in sync with naming such as `Vehicle` and `Billing`. The problem with `Vehicle` class is the responsibility to check-in and `Billing` handles checkout and slot updation 
2) There is no Ticket concept in code which existed in requirement. A ticket is an entity which is issued against a vehicle and a spot. Ticket is closed when billing is done and then the spot is marked vacant
3) Getter and setter . I without knowing and not used ever tried to over engineer and screwed badly. Either learn and implement properly or move to two simple functions 
4) There is no slot vacant thing happening now. Major flaw in design 

### My Verdict:

Irrespective of this is first time , I performed poorly because of missing two critical design thing no Ticket, slot not vacant. This exercise also showed not much knowledge of python syntax . 

### Time taken: 

Was way above 90 min may be around 270 min for this thing. Planning was wrong in choosing a time when kid would be sleeping. So this planning needs to be handled next time 

<hr>

### How to fix above issues

1) There has to be a `Ticket` class which will accept the vehicle and selected slot and open a ticket for that vehicle. 
2) We will have a `ParkingManager` CLass that will expose `park_vehicle` and `unpark_vehicle` which will internally call teh `TicketManager` class for ticket related functiponalities
3) There has to be `TickerManager` class that wil handle creation of ticket and closing of ticket
4) And `Billing` is an independent class that has just to calculate bill for a given ticket and return the bill amount
5) Fix the setter and getter

