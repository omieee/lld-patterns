import unittest
from unittest.mock import patch
import io
import sys

from main import main


class TestParkingLotSystem(unittest.TestCase):
    def run_with_input(self, commands_str: str) -> str:
        """Helper to pipe commands into main() and capture terminal output."""
        with patch("sys.stdin", io.StringIO(commands_str)):
            with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
                main()
                return mock_stdout.getvalue()

    def test_01_parking_lot_creation(self):
        """Verify the creation confirmation matches specifications exactly."""
        commands = "create_parking_lot PR1234 2 6\nexit\n"
        expected = "Created parking lot with 2 floors and 6 slots per floor\n"

        actual = self.run_with_input(commands)
        self.assertEqual(actual, expected)

    def test_02_empty_displays(self):
        """Verify displays correctly format layout paths when empty."""
        commands = (
            "create_parking_lot PR1234 1 3\n"
            "display free_count CAR\n"
            "display free_slots CAR\n"
            "display occupied_slots CAR\n"
            "exit\n"
        )
        expected = (
            "Created parking lot with 1 floors and 3 slots per floor\n"
            "No. of free slots for CAR on Floor 1: 0\n"
            "Free slots for CAR on Floor 1: \n"
            "Occupied slots for CAR on Floor 1: \n"
        )

        actual = self.run_with_input(commands)
        self.assertEqual(actual, expected)

    def test_03_parking_and_lot_full(self):
        """Verify correct full lot handling and validation indicators."""
        commands = (
            "create_parking_lot PR1234 1 4\n"
            "park_vehicle TRUCK KA-01-1111 white\n"
            "park_vehicle TRUCK KA-01-2222 black\n"
            "exit\n"
        )
        expected = (
            "Created parking lot with 1 floors and 4 slots per floor\n"
            "Parked vehicle. Ticket ID: PR1234_1_1\n"
            "Parking Lot Full\n"
        )

        actual = self.run_with_input(commands)
        self.assertEqual(actual, expected)

    def test_04_invalid_ticket_handling(self):
        """Verify unparking correctly catches fake or malformed ticket IDs."""
        commands = (
            "create_parking_lot PR1234 1 4\n"
            "unpark_vehicle PR1234_1_5\n"
            "unpark_vehicle BAD_TICKET_ID\n"
            "exit\n"
        )
        expected = (
            "Created parking lot with 1 floors and 4 slots per floor\n"
            "Invalid Ticket\n"
            "Invalid Ticket\n"
        )

        actual = self.run_with_input(commands)
        self.assertEqual(actual, expected)

    def test_05_dynamic_structural_additions(self):
        """Verify dynamic add_floor and add_slot_to_floor commands update and reflect status changes."""
        commands = (
            "create_parking_lot PR1234 1 3\n"
            "add_floor 4\n"
            "add_slot_to_floor 2 LARGE\n"
            "display free_slots TRUCK\n"
            "exit\n"
        )
        # Baseline: F1 has 3 slots (1: TRUCK, 2: BIKE, 3: BIKE). TRUCK on F1 is slot 1.
        # F2 added with 4 slots (1: TRUCK, 2: BIKE, 3: BIKE, 4: CAR). TRUCK on F2 is slot 1.
        # Dynamic addition: Slot 5 added to F2 as LARGE (TRUCK).
        # Expected free slots for TRUCK on F2 should be: 1,5
        expected = (
            "Created parking lot with 1 floors and 3 slots per floor\n"
            "Added floor to parking lot. Total floors now: 2\n"
            "Added slot of type LARGE to Floor 2\n"
            "Free slots for TRUCK on Floor 1: 1\n"
            "Free slots for TRUCK on Floor 2: 1,5\n"
        )

        actual = self.run_with_input(commands)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
