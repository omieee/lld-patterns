from datetime import datetime, timezone
import time
from typing import Any

from src.utils import SLOT_FIT, SLOT_STATUS, VEHICLE_TYPE, RATE_MULTIPLIER, RATE_CARD


class ParkingLot:
    def __init__(self, name: str, floors: int = 0, slots: int = 0) -> None:
        self.name = name
        self.floors = floors
        self.total_slots = slots

    @property
    def getTotalSlots(self) -> int:
        return self.total_slots


class ParkingSlot:
    def __init__(
        self,
        _parkinglot: ParkingLot,
        _slnumber: int,
        _slotfit: SLOT_FIT,
        _slfloor: int = 0,
        _slstatus: SLOT_STATUS = SLOT_STATUS.VACANT,
    ) -> None:
        self.parkinglot = _parkinglot
        self.slnumber = _slnumber
        self.slotfit = _slotfit
        self.slfloor = _slfloor
        self.slstatus = _slstatus

    @property
    def slotstatus(self):
        return self.slstatus

    @slotstatus.setter
    def slotstatus(self, status: SLOT_STATUS):
        self.slstatus = status

    def __repr__(self) -> str:
        return (
            f"\nParkingSlot(Number: {self.slnumber}, Floor: {self.slfloor}, "
            f"Fit: {self.slotfit}, Status: {self.slstatus})"
        )


class ParkingSlots:
    def __init__(self) -> None:
        self.parkingSlots = []

    def addSlot(self, psl: ParkingSlot) -> None:
        self.parkingSlots.append(psl)

    def getAllSlots(self):
        return self.parkingSlots

    def getVacantSlotBasedOnSize(self, slotFit: SLOT_FIT) -> ParkingSlot | None:
        for psl in self.parkingSlots:
            if psl.slotfit == slotFit and psl.slstatus == SLOT_STATUS.VACANT:
                return psl
        return None


class Vehicle:
    def __init__(self, vtype: VEHICLE_TYPE, reg: str) -> None:
        self.vtype = vtype
        self.reg = reg
        self.entryTime = None
        self.slnumber = None
        self.flnumber = None

    def getVehicle(self) -> dict:
        return {
            "vtype": self.vtype,
            "reg": self.reg,
            "entry": self.entryTime,
            "slot": self.slnumber,
            "floor": self.flnumber,
        }

    def setSlot(self, slot: int):
        self.slnumber = slot

    def setFloor(self, floor: int):
        self.flnumber = floor

    def resetVehicle(self) -> None:
        del self


class TicketManager:
    def __init__(self) -> None:
        self.tickets = []

    def createTicket(self, veh: Vehicle, allotedSlot: ParkingSlot) -> dict | None:
        if allotedSlot:
            allotedSlot.slotstatus = SLOT_STATUS.TAKEN
            veh.setSlot(allotedSlot.slnumber)
            veh.setFloor(allotedSlot.slfloor)
            out = {
                "vehicle": veh,
                "allotedslot": allotedSlot,
                "allotedtime": int(datetime.now(timezone.utc).timestamp()),
            }
            self.tickets.append(out)
            return out
        return None

    def closeTicket(self, veh: Vehicle) -> bool:
        for tkt in self.tickets:
            if tkt["vehicle"].reg == veh.reg:
                tkt["allotedslot"].slotstatus = SLOT_STATUS.VACANT
                print("Tickets:", self.tickets)
                self.tickets.remove(tkt)
                veh.resetVehicle()
                return True
        return False


class ParkingManager:
    def __init__(self, pslots: ParkingSlots) -> None:
        self.pslots = pslots
        self.tktmgr = TicketManager()

    def park_vehicle(self, veh: Vehicle) -> dict | None:
        requiredType = None
        if veh.vtype == VEHICLE_TYPE.BIKE:
            requiredType = SLOT_FIT.SMALL
        elif veh.vtype == VEHICLE_TYPE.CAR:
            requiredType = SLOT_FIT.MEDIUM
        elif veh.vtype == VEHICLE_TYPE.TRUCK:
            requiredType = SLOT_FIT.LARGE
        if requiredType:
            allocatedSlot = self.pslots.getVacantSlotBasedOnSize(requiredType)
            if allocatedSlot:
                tkt = self.tktmgr.createTicket(veh=veh, allotedSlot=allocatedSlot)
                return tkt
        return None

    def unpark_vehicle(self, ticket) -> bool:
        if ticket["allotedtime"]:
            bill = Billing()
            billamt = bill.calculate_bill(ticket=ticket)
            # Handle payment here in actual for now payment is true
            return bool(billamt and self.tktmgr.closeTicket(ticket["vehicle"]))


class Billing:
    def calculate_bill(self, ticket) -> int | None:
        if ticket["allotedtime"]:
            difference_time = (
                int(datetime.now(timezone.utc).timestamp())
                + 10000
                - ticket["allotedtime"]
            )
            if difference_time / 3600 > 2:
                final_bill = (
                    RATE_CARD["MIN"]
                    + (round(difference_time / 3600) - 2)
                    * RATE_CARD["AFTER_2_HOUR_PER_HOUR"]
                )
            else:
                final_bill = RATE_CARD["MIN"]
            return final_bill
        return None
