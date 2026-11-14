"""
SAMPLE = [
    "3",
    "T1 Anita Maths",
    "T2 Ravi Science",
    "T3 Meena English",
    "2",
    "R101 40",
    "R102 30",
    "4",
    "C1 T1 R101 Mon 9",
    "C2 T2 R102 Mon 10",
    "C3 T3 R101 Tue 9",
    "C4 T1 R102 Wed 11",
]
"""


class MP02_practice:
    def validate_sample(self, sample: list) -> tuple[int, int, int, str, str, str]:
        no_to_teachers = int(sample[0])
        teachers = []
        rooms = []
        classes = []
        for i in range(1, no_to_teachers + 1):
            teachers.append(sample[i])
        no_of_rooms = int(sample[no_to_teachers + 1])
        if no_of_rooms != 0:
            room_start_number = no_to_teachers + 2
            room_end_number = room_start_number + no_of_rooms
            for i in range(room_start_number, room_end_number):
                rooms.append(sample[i])
        else:
            room_start_number = no_to_teachers + 1
            room_end_number = room_start_number + 1
        no_of_classes = int(sample[no_to_teachers + no_of_rooms + 2])
        class_start_number = (no_to_teachers + no_of_rooms + 1) + 2
        class_end_number = len(sample) - 1
        for i in range(class_start_number, class_end_number + 1):
            classes.append(sample[i])
        if (
            len(teachers) == no_to_teachers
            and len(rooms) == no_of_rooms
            and len(classes) == no_of_classes
        ):
            return (
                no_to_teachers,
                no_of_rooms,
                no_of_classes,
                teachers[-1] if teachers else "",
                rooms[-1] if rooms else "",
                classes[-1] if classes else "",
            )
        else:
            return (-1, -1, -1, "", "", "")
