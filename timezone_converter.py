#!/usr/bin/env python3
"""
Timezone Converter CLI Tool
Converts times from one timezone to another automatically
"""

from datetime import datetime
from zoneinfo import ZoneInfo
import re
import sys


# Common timezone abbreviations mapping
TIMEZONE_MAP = {
    'EST': 'America/New_York',
    'EDT': 'America/New_York',
    'CST': 'America/Chicago',
    'CDT': 'America/Chicago',
    'MST': 'America/Denver',
    'MDT': 'America/Denver',
    'PST': 'America/Los_Angeles',
    'PDT': 'America/Los_Angeles',
    'UTC': 'UTC',
    'GMT': 'GMT',
    'BST': 'Europe/London',
    'CET': 'Europe/Paris',
    'IST': 'Asia/Kolkata',
    'JST': 'Asia/Tokyo',
    'AEST': 'Australia/Sydney',
    'AEDT': 'Australia/Sydney',
}


def parse_time_input(time_string):
    """
    Parse a time string like "3 PM EST", "6:49 PM (PDT)", "15:00 EST", etc.
    Returns: (datetime object, source timezone)
    """
    # Pattern to match times with timezone
    # Matches: "3 PM EST", "3:30 PM EST", "6:49 PM (PDT)", "3:30:45 PM EST", etc.
    # First, try to find a timezone abbreviation (with or without parentheses, case-insensitive)
    tz_pattern = r'\(?([A-Za-z]{3,4})\)?'

    # Find ALL potential timezone matches and check if any are valid
    tz_abbr = None
    for match in re.finditer(tz_pattern, time_string):
        potential_tz = match.group(1).upper()
        if potential_tz in TIMEZONE_MAP:
            tz_abbr = potential_tz
            break

    if not tz_abbr:
        return None, None

    # Now find the time part (hours, minutes, and optional seconds)
    time_pattern = r'(\d{1,2})(?::(\d{2}))?(?::(\d{2}))?\s*(AM|PM|am|pm)?'
    time_match = re.search(time_pattern, time_string)

    if not time_match:
        return None, None

    hour = int(time_match.group(1))
    minute = int(time_match.group(2)) if time_match.group(2) else 0
    am_pm = time_match.group(3).upper() if time_match.group(3) else None

    # Convert to 24-hour format if AM/PM is specified
    if am_pm:
        if am_pm == 'PM' and hour != 12:
            hour += 12
        elif am_pm == 'AM' and hour == 12:
            hour = 0

    # Get the full timezone name (we already verified it's valid above)
    tz_name = TIMEZONE_MAP[tz_abbr]

    # Create datetime object with today's date
    now = datetime.now()
    dt = datetime(now.year, now.month, now.day, hour, minute)

    # Add timezone info
    dt_with_tz = dt.replace(tzinfo=ZoneInfo(tz_name))

    return dt_with_tz, tz_abbr


def convert_timezone(dt, target_tz):
    """
    Convert a datetime object to a target timezone
    """
    target_zone = ZoneInfo(target_tz)
    converted = dt.astimezone(target_zone)
    return converted


def get_local_timezone():
    """
    Get the user's local timezone
    """
    # Get local timezone from the system
    local_dt = datetime.now().astimezone()
    return local_dt.tzinfo


def format_time(dt):
    """
    Format datetime in a readable way
    """
    return dt.strftime("%I:%M %p %Z")


def main():
    """
    Main function to run the CLI tool
    """
    if len(sys.argv) < 2:
        print("Timezone Converter")
        print("-" * 40)
        print("Usage: python timezone_converter.py \"3 PM EST\"")
        print("\nExamples:")
        print('  python timezone_converter.py "3 PM EST"')
        print('  python timezone_converter.py "15:00 UTC"')
        print('  python timezone_converter.py "9:30 AM PST"')
        print("\nSupported timezones:")
        for abbr in sorted(TIMEZONE_MAP.keys()):
            print(f"  {abbr}")
        sys.exit(1)

    # Get the time string from command line argument
    time_input = " ".join(sys.argv[1:])

    # Parse the input
    source_dt, source_tz = parse_time_input(time_input)

    if not source_dt:
        print(f"Could not parse time: {time_input}")
        print("Please use format like: '3 PM EST' or '15:00 UTC'")
        sys.exit(1)

    # Get user's local timezone
    local_tz = get_local_timezone()

    # Convert to local timezone
    local_dt = source_dt.astimezone(local_tz)

    # Display results
    print("\n" + "=" * 50)
    print(f"Original time: {format_time(source_dt)}")
    print(f"Your local time: {format_time(local_dt)}")
    print("=" * 50)

    # Show some other common timezones for reference
    print("\nOther timezones:")
    common_zones = ['America/New_York', 'America/Los_Angeles',
                    'Europe/London', 'UTC', 'Asia/Tokyo']

    for zone_name in common_zones:
        try:
            converted = convert_timezone(source_dt, zone_name)
            zone_abbr = converted.strftime("%Z")
            print(f"  {zone_name:25} {format_time(converted)}")
        except:
            pass


if __name__ == "__main__":
    main()
