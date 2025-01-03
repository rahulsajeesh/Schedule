""""
FileName: User Inputs
Purpose: Create a structure for the schedule
Author: Rahul Sajeeshkumar
Last Edited: 01/03/2024
"""

import matplotlib.pyplot as plt
import numpy as np

def create_schedule(events, durations, total_time):
    if sum(durations) > total_time:
        print("The total duration of events exceeds the available time! Please adjust your inputs.")
        return None

    schedule = []
    current_time = 0

    for event, duration in zip(events, durations):
        if current_time + duration <= total_time:
            schedule.append((event, current_time, current_time + duration))
            current_time += duration
        else:
            print(f"Not enough time left to schedule {event}.")
            break
    return schedule