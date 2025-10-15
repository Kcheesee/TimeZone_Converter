#!/usr/bin/env python3
"""
Timezone Converter Menu Bar App
A Mac menu bar app that converts timezones from clipboard
"""

import rumps
import pyperclip
from timezone_converter import parse_time_input, format_time


class TimezoneConverterApp(rumps.App):
    def __init__(self):
        super(TimezoneConverterApp, self).__init__("🌍", quit_button="Quit")
        self.menu = ["Convert from Clipboard"]

    @rumps.clicked("Convert from Clipboard")
    def convert_clipboard(self, _):
        """Convert timezone from current clipboard content"""
        # Get clipboard content
        clipboard_text = pyperclip.paste()

        if not clipboard_text:
            rumps.alert("No clipboard content", "Please copy some text with a time first!")
            return

        # Try to parse and convert
        source_dt, source_tz = parse_time_input(clipboard_text)

        if not source_dt:
            rumps.alert(
                "No time found",
                f"Couldn't find a time with timezone in:\n\n{clipboard_text[:100]}"
            )
            return

        # Convert to local timezone
        local_dt = source_dt.astimezone()

        # Show result
        result = f"Original: {format_time(source_dt)}\n\nYour local time: {format_time(local_dt)}"
        rumps.alert("Timezone Conversion", result)


if __name__ == "__main__":
    TimezoneConverterApp().run()
