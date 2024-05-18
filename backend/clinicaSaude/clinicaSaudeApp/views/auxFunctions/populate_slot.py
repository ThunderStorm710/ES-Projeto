import datetime
import os
import django

from ...models import TimeSlot


def populate_time_slots(doctor_id, date, start_hour, end_hour):
    date_obj = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    start_time = datetime.time(start_hour, 0)
    end_time = datetime.time(end_hour, 0)

    current_time = datetime.datetime.combine(date_obj, start_time)

    while current_time.time() < end_time:
        slot_end_time = (current_time + datetime.timedelta(hours=1)).time()

        # Create a new TimeSlot object
        time_slot = TimeSlot(
            doctor_id=doctor_id,
            date=date_obj,
            start_time=current_time.time(),
            end_time=slot_end_time,
            is_available=True
        )
        time_slot.save()  # Save the TimeSlot object to the database

        # Increment the current time by 1 hour
        current_time += datetime.timedelta(hours=1)


# Exemplo de uso:
populate_time_slots(doctor_id=1, date='2024-05-18', start_hour=9, end_hour=17)
