def add_time(start, duration, day_of_week=False):
    hour_start = get_hour(start)
    minuts_start = get_minuts(start)
    hour_duration = get_hour(duration)
    minuts_duration = get_minuts(duration)
    final = final_time(
        start, hour_start, minuts_start, hour_duration, minuts_duration, day_of_week
    )
    return final


def get_hour(time_data: str) -> str:
    return time_data.split(":")[0]


def get_minuts(time_data: str) -> str:
    minuts_with_period = time_data.split(":")[1]
    minuts = minuts_with_period.split(" ")[0]
    return minuts


def get_mod_minuts(start_minuts: str, duration_minuts: str) -> str:
    sum_minuts = int(start_minuts) + int(duration_minuts)
    mod_hour = sum_minuts % 60
    return str(mod_hour).zfill(2)


def get_extra_hour(start_minuts: str, duration_minuts: str) -> int:
    sum_minuts = int(start_minuts) + int(duration_minuts)
    sum_minuts = sum_minuts / 60
    sum_minuts = str(sum_minuts).split(".")[0]
    return int(sum_minuts)


def get_period(start: str) -> str:
    return start.split(" ")[1]


def check_next_day(hour: int, period: str) -> str:
    if (hour >= 24) or (hour >= 12 and period == "PM"):
        return "(next day)"


def count_days(hours: int) -> int:
    days = round(hours / 24)
    if days > 1:
        return days


def days_of_week(day: str, total_days: int):
    day = day.casefold()
    print("===", day)
    days = {
        0: "Sunday",
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "saturDay",
    }

    start = 0
    for key, value in days.items():
        if day == value.casefold():
            start = key
           

    while total_days > 0:
        for key, day_of_week in days.items():
            start = start + 1
            if start == 6:
                start = 0
        total_days = total_days - 1

    for key, value in days.items():
        if key == start:
            return value


def hour_after_long_period(total_hour: int) -> int:
    hour = total_hour % 12
    if hour == 0:
        return 12
    else:
        return hour


def final_time(
    start: str,
    start_hour: str,
    start_minuts: str,
    durarion_hour: str,
    duration_minuts: str,
    day_of_week: str,
):
    hour = int(start_hour) + int(durarion_hour)
    hour = hour + get_extra_hour(start_minuts, duration_minuts)
    minuts = get_mod_minuts(start_minuts, duration_minuts)
    hour_after_long_time = hour_after_long_period(hour)
    period = get_period(start)
    next_day = check_next_day(hour, period)
    days = count_days(hour)
    if hour >= 12:
        if period == "AM":
            period = "PM"
        elif period == "PM":
            period = "AM"
        if not (period == "PM" and hour == 12):
            hour = hour - 12
    if days:
        if day_of_week:
            day_week = days_of_week(day_of_week, days)
            return (f"{hour_after_long_time}:{minuts} {period}, {day_week} ({days} days later)"
            )
        else:
            return f"{hour_after_long_time}:{minuts} {period} ({days} days later)"
    if next_day:
        return f"{hour}:{minuts} {period} {next_day}"
    elif day_of_week:
        return f"{hour}:{minuts} {period}, {day_of_week}"
    else:
        return f"{hour}:{minuts} {period}"


print(add_time("8:16 PM", "466:02", "tuesday"))
