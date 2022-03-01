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


def check_next_day(
    hour: int, initial_period: str, final_period: str, day_of_week: str
) -> str:
    next_day = hour / 24
    first_number = int(str(next_day)[0])
    extra_day = str(next_day).split(".")[1]
    extra_day = extra_day[0]
    if first_number == 1 and int(extra_day) == 0:
        return pre_formatter_next_day(day_of_week, first_number)
    elif initial_period == "PM" and final_period == "AM" and next_day < 1:
        return pre_formatter_next_day(day_of_week, extra_day)


def count_days(hours: int) -> int:
    days = round(hours / 24)
    if days > 1:
        return days


def names_week_day():
    return {
        0: "Sunday",
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "saturDay",
    }


def next_day_of_week(day: str, checker: int):
    days = names_week_day()
    iter_days = iter(days.items())
    if checker == 0 or checker == 1:
        for name in iter_days:
            if name[1].casefold() == day.casefold():
                if name[0] == 6:
                    return "Sunday"
                next_item = next(iter_days)
                return next_item[1]


def all_days_of_week(day: str, total_days: int):
    day = day.casefold()
    days = names_week_day()
    start = 0
    for key, value in days.items():
        if day == value.casefold():
            start = key

    while total_days > 0:
        for key in days.keys():
            if total_days == 0:
                break
            if start == 6:
                start = 0
                total_days = total_days - 1
                continue
            start = start + 1
            total_days = total_days - 1

    for key, value in days.items():
        if key == start:
            return value


def hour_after(total_hour: int) -> int:
    hour = total_hour % 12
    if hour == 0:
        return 12
    return hour


def get_changes_in_period(total_hour: int, initial_period: str) -> str:
    period = total_hour / 24
    mid = str(period).split(".")[1]
    mid = mid[0]
    if int(mid) >= 5:
        if initial_period == "AM":
            return "PM"
        return "AM"
    return initial_period


def pre_formatter_next_day(day_of_week: str, checker: int) -> str:
    if day_of_week:
        day_week = next_day_of_week(day_of_week, checker)
        return f"{day_week} (next day)"
    return "(next day)"


def formatter_next_day(
    hour: int,
    minuts: str,
    next_day: str,
    next_day_period: str,
    final_period: str,
    day_of_week: str,
) -> str:
    if day_of_week:
        return f"{hour}:{minuts} {next_day_period}, {next_day}"
    return f"{hour}:{minuts} {final_period} {next_day}"


def formatter_long_period_days(
    hour: int, minuts: str, days: int, final_period: str, day_of_week: str
) -> str:
    if day_of_week:
        day_week = all_days_of_week(day_of_week, days)
        return f"{hour}:{minuts} {final_period}, {day_week} ({days} days later)"
    return f"{hour}:{minuts} {final_period} ({days} days later)"


def formatter_periods_without_days_count(
    hour: int, minuts: str, final_period: str, day_of_week: str
):
    return f"{hour}:{minuts} {final_period}, {day_of_week}"


def formatter_simple(hour: int, minuts: str, final_period: str) -> str:
    return f"{hour}:{minuts} {final_period}"


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
    more_than_one_day = count_days(hour)
    initial_period = get_period(start)
    final_period = get_changes_in_period(hour, initial_period)
    next_day = check_next_day(hour, initial_period, final_period, day_of_week)
    next_day_period = get_changes_in_period(hour, initial_period)
    hour = hour_after(hour)
    minuts = get_mod_minuts(start_minuts, duration_minuts)
    if next_day:
        return formatter_next_day(
            hour, minuts, next_day, next_day_period, final_period, day_of_week
        )
    elif more_than_one_day:
        return formatter_long_period_days(
            hour, minuts, more_than_one_day, final_period, day_of_week
        )
    elif day_of_week:
        return formatter_periods_without_days_count(
            hour, minuts, final_period, day_of_week
        )
    return formatter_simple(hour, minuts, final_period)


print(add_time("8:16 PM", "466:02", "tuesday"))
