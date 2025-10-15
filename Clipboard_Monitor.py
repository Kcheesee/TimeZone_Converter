#!/usr/bin/env python3
""" Clipboard monitor for Timezone conversion 
Watches your clipboard and automatically converts times to you"""

import pyperclip
import time
from timezone_converter import parse_time_input, format_time
def monitor_clipboard():
    """Continuously monitor the clipboard for time str"""
    print("Clipboard monitor started!")
    print("Copy any text with times like '3 PM EST' and I'll convert it for you.")
    print("Press Ctrl+C to stop.\n")
    # Store the last clipboard content so we know when it changes
    last_clipboard = ""

    # Keep running forever (until you press Ctrl+C)
    while True:
        try:
            # Get current clipboard content
            current_clipboard = pyperclip.paste()

            # Check if clipboard changed
            if current_clipboard != last_clipboard:
                # Update what we remember
                last_clipboard = current_clipboard

                # Try to find and convert a time in the text
                source_dt, source_tz = parse_time_input(current_clipboard)

                if source_dt:
                    # We found a time! Convert it to local timezone
                    local_dt = source_dt.astimezone()

                    print("\n" + "="*50)
                    print(f"Found time: {format_time(source_dt)}")
                    print(f"Your local time: {format_time(local_dt)}")
                    print("="*50 + "\n")

            # Wait 1 second before checking again
            time.sleep(1)

        except KeyboardInterrupt:
            # User pressed Ctrl+C to stop
            print("\nClipboard monitor stopped.")
            break


if __name__ == "__main__":
    monitor_clipboard()