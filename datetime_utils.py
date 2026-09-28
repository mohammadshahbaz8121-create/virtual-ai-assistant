# datetime_utils.py
# Handles current date and time

from datetime import datetime


def get_current_date():
    """Return the current date."""

    current_date = datetime.now()

    return current_date.strftime("%d-%m-%Y")


def get_current_time():
    """Return the current time."""

    current_time = datetime.now()

    return current_time.strftime("%I:%M %p")