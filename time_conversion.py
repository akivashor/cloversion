from datetime import datetime, timedelta, date
from dateutil.parser import parse


def convert_minutes_to_hours_fraction(total_minutes: float) -> float:
    """
    Convert total minutes to hours fraction.
    """
    hours = total_minutes // 60
    minutes = total_minutes % 60
    minutes_fraction = float(minutes) / 60
    hours_and_minutes_fraction = hours + minutes_fraction
    return hours_and_minutes_fraction


def round_seconds(time_obj: datetime.time) -> datetime.time:
    """
    Round a time to the nearest second.
    Please note that this does not work for time 23:59:59.
    """
    if time_obj.microsecond >= 500000:
        new_datetime = datetime.combine(date.today(), time_obj)
        new_datetime = new_datetime + timedelta(seconds=1)
        new_time = new_datetime.time()
    else:
        new_time = time_obj
    new_time = new_time.replace(microsecond=0)
    return new_time


def timestamp_to_datetime(timestamp_object: float or str, time_format: str = '%Y-%m-%d %H:%M:%S',
                          return_format: str = None) -> str or datetime:
    """
    Convert a timestamp to a datetime object or formatted string.
    """
    if isinstance(timestamp_object, float) or isinstance(timestamp_object, str):
        if isinstance(timestamp_object, str):
            date_time_object = datetime.strptime(timestamp_object, time_format)
        else:
            date_time_object = datetime.fromtimestamp(float(timestamp_object))
        if return_format:
            time_str = date_time_object.strftime(return_format)
            return time_str
        else:
            return date_time_object


def round_timedelta_seconds(timedelta_obj: timedelta) -> timedelta:
    """
    Round a timedelta to the nearest second.
    """
    total_seconds = timedelta_obj.total_seconds()
    rounded_seconds = round(total_seconds)
    return timedelta(seconds=rounded_seconds)


def add_timedelta_to_time(time_string: str, time_delta_string: str, time_format: str = '%H:%M:%S') -> str:
    """
    Add a timedelta to a time string and return the resulting time string.
    """
    try:
        time = datetime.strptime(time_string, time_format)
        time_delta = parse(time_delta_string) - parse('0:00:00')
        new_time = (time + time_delta).time()
        return round_seconds(new_time).strftime(time_format)
    except ValueError:
        print('Invalid input format.')
        return time_string


def time_to_units(time_string: str, units: str = 'm', string_format: str = '%H:%M:%S') -> float:
    """
    Convert a time string to units fraction.
    Default is minutes.
    Available units: 'h' (hours), 'm' (minutes), 's' (seconds).
    """
    try:
        time = datetime.strptime(time_string, string_format)
        seconds = time.hour * 3600.0 + time.minute * 60.0 + time.second
        if units == 's':
            return seconds
        elif units == 'm':
            return seconds / 60
        if units == 'h':
            return seconds / 3600
    except ValueError as e:
        error_message = "Could not convert {}. Error: {}".format(time_string, e)
        raise ValueError(error_message)


