from src import parking, utils


def main():
    plot = parking.ParkingLot("Om-Park", 2, 10)

    ps1 = parking.ParkingSlot(
        _parkinglot=plot, _slnumber=1, _slotfit=utils.SLOT_FIT.SMALL, _slfloor=0
    )
    ps2 = parking.ParkingSlot(
        _parkinglot=plot, _slnumber=2, _slotfit=utils.SLOT_FIT.SMALL, _slfloor=1
    )
    ps3 = parking.ParkingSlot(
        _parkinglot=plot, _slnumber=3, _slotfit=utils.SLOT_FIT.SMALL, _slfloor=0
    )
    ps4 = parking.ParkingSlot(
        _parkinglot=plot, _slnumber=4, _slotfit=utils.SLOT_FIT.MEDIUM, _slfloor=0
    )
    ps5 = parking.ParkingSlot(
        _parkinglot=plot, _slnumber=5, _slotfit=utils.SLOT_FIT.MEDIUM, _slfloor=1
    )
    ps6 = parking.ParkingSlot(
        _parkinglot=plot, _slnumber=6, _slotfit=utils.SLOT_FIT.MEDIUM, _slfloor=1
    )
    ps7 = parking.ParkingSlot(
        _parkinglot=plot, _slnumber=7, _slotfit=utils.SLOT_FIT.LARGE, _slfloor=0
    )
    ps8 = parking.ParkingSlot(
        _parkinglot=plot, _slnumber=8, _slotfit=utils.SLOT_FIT.LARGE, _slfloor=0
    )
    ps9 = parking.ParkingSlot(
        _parkinglot=plot, _slnumber=9, _slotfit=utils.SLOT_FIT.LARGE, _slfloor=0
    )
    ps10 = parking.ParkingSlot(
        _parkinglot=plot, _slnumber=10, _slotfit=utils.SLOT_FIT.LARGE, _slfloor=0
    )

    psls = parking.ParkingSlots()
    psls.addSlot(ps1)
    psls.addSlot(ps2)
    psls.addSlot(ps3)
    psls.addSlot(ps4)
    psls.addSlot(ps5)
    psls.addSlot(ps6)
    psls.addSlot(ps7)
    psls.addSlot(ps8)
    psls.addSlot(ps9)
    psls.addSlot(ps10)
    pmgr = parking.ParkingManager(psls)
    biller = parking.Billing()
    print("Hello from parking-lot! Setup is ready, we are open to serve !!")

    veh1 = parking.Vehicle(vtype=utils.VEHICLE_TYPE.BIKE, reg="KA0101")
    ptkt = pmgr.park_vehicle(veh=veh1)
    print(ptkt["vehicle"].getVehicle())
    print("Bill:", biller.calculate_bill(ptkt))
    print("Assuming bill is paid")
    print("Before vacating let's check details: ", psls.getAllSlots())
    pmgr.unpark_vehicle(ptkt)
    print("After vacating let's check details: ", psls.getAllSlots())


if __name__ == "__main__":
    main()
