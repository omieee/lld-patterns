class Ticket:
    def __init__(self, parking_lot_id: str, floor: int, slot: int) -> None:
        self.parking_lot_id = parking_lot_id
        self.floor = floor
        self.slot = slot
        self.ticket_id = f"{parking_lot_id}_{floor}_{slot}"
