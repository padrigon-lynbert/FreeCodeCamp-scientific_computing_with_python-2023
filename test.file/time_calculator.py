from datetime import datetime, timedelta

def add_time(start_time, duration, starting_day=None):
    # Parse start_time to extract hours, minutes, and period
    start_time_obj = datetime.strptime(start_time, "%I:%M %p")
    start_hour = start_time_obj.hour
    start_minute = start_time_obj.minute
    period = start_time_obj.strftime("%p")

    # Parse duration to extract hours and minutes
    duration_parts = duration.split(":")
    duration_hours = int(duration_parts[0])
    duration_minutes = int(duration_parts[1])

    # Convert start_time to minutes
    total_start_minutes = start_hour * 60 + start_minute

    # Add duration to total minutes
    total_minutes = total_start_minutes + duration_hours * 60 + duration_minutes

    # Calculate the new time
    new_hour = total_minutes // 60
    new_minute = total_minutes % 60

    # Adjust period if needed
    if new_hour >= 12:
        period = "PM" if period == "AM" else "AM"
    if new_hour > 12:
        new_hour -= 12

    new_time = f"{new_hour:02d}:{new_minute:02d} {period}"

    # Handle starting_day if provided
    if starting_day:
        starting_day = starting_day.capitalize()
        day_delta = 0

        # Define a dictionary to map days to their index (0 for Monday, 6 for Sunday)
        days = {
            "Monday": 0,
            "Tuesday": 1,
            "Wednesday": 2,
            "Thursday": 3,
            "Friday": 4,
            "Saturday": 5,
            "Sunday": 6
        }

        if starting_day in days:
            day_index = days[starting_day]
            day_delta = (total_minutes // 60) // 24  # Calculate the number of days passed
            new_day_index = (day_index + day_delta) % 7
            new_day = list(days.keys())[list(days.values()).index(new_day_index)]
            new_time += f", {new_day}"

    # Check if it's the next day
    if total_minutes >= 1440:
        new_time += " (next day)"

    return new_time
