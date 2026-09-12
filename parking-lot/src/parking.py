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
    def update_slot(self, status: SLOT_STATUS):
        self.slstatus = status


class ParkingSlots:
    def __init__(self) -> None:
        self.parkingSlots = []

    def addSlot(self, psl: ParkingSlot) -> None:
        self.parkingSlots.append(psl)

    def getVacantSlotBasedOnSize(self, slotFit: SLOT_FIT) -> ParkingSlot | None:
        for psl in self.parkingSlots:
            if psl.slotfit == slotFit and psl.slstatus == SLOT_STATUS.VACANT:
                return psl
        return None


class Vehicle:
    def __init__(self, vtype: VEHICLE_TYPE, reg: str) -> None:
        self.vtype = vtype
        self.reg = reg
        self.parkingSlot = None
        self.entrytime = None

    def allotSlot(self, psls: ParkingSlots) -> ParkingSlot | None:
        requiredType = None
        if self.vtype == VEHICLE_TYPE.BIKE:
            requiredType = SLOT_FIT.SMALL
        elif self.vtype == VEHICLE_TYPE.CAR:
            requiredType = SLOT_FIT.MEDIUM
        elif self.vtype == VEHICLE_TYPE.TRUCK:
            requiredType = SLOT_FIT.LARGE
        if requiredType:
            allocatedSlot = psls.getVacantSlotBasedOnSize(requiredType)
            if allocatedSlot:
                allocatedSlot.update_slot = SLOT_STATUS.TAKEN
                self.parkingSlot = allocatedSlot.slnumber
                self.entrytime = int(datetime.now(timezone.utc).timestamp())
                return allocatedSlot
        return None


class Billing:
    def calculate_bill(self, veh: Vehicle, psls: ParkingSlots) -> int | None:
        if veh.parkingSlot and veh.entrytime:
            difference_time = (
                int(datetime.now(timezone.utc).timestamp()) + 10000 - veh.entrytime
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
