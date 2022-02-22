def add_time(start, duration, day=False):
    hour_start = get_hour(start)
    minuts_start = get_minuts(start)
    hour_duration = get_hour(duration)
    minuts_duration = get_minuts(duration)
    final = final_time(start, hour_start, minuts_start, hour_duration, minuts_duration)
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

def final_time(
    start: str,
    start_hour: str,
    start_minuts: str,
    durarion_hour: str,
    duration_minuts: str,
):
    hour = int(start_hour) + int(durarion_hour)
    hour = hour + get_extra_hour(start_minuts, duration_minuts)
    minuts = get_mod_minuts(start_minuts, duration_minuts)
    period = get_period(start)
    next_day = check_next_day(hour, period)
    if hour >= 12:
        if period == "AM":
            period = "PM"
        elif period == "PM":
            period = "AM"
        if not (period == "PM" and hour == 12):
            hour = hour - 12
    if next_day:
        return f"{hour}:{minuts} {period} {next_day}"
    else:
        return f"{hour}:{minuts} {period}"


print(add_time("11:40 AM", "0:25"))
