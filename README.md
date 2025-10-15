# Timezone Converter Suite 🌍

A collection of Python tools for automatic timezone conversion, built to make working across timezones effortless.

## Features

This project includes three different ways to convert timezones:

### 1. 🖥️ Command-Line Tool
Convert times directly from the terminal with a simple command.

```bash
python3 timezone_converter.py "3 PM EST"
```

### 2. 📋 Clipboard Monitor
Automatically monitors your clipboard and converts any timezone it detects in real-time.

```bash
python3 Clipboard_Monitor.py
```

Copy text like "Meeting at 3 PM PST" and get instant conversions!

### 3. 🍎 Mac Menu Bar App
A convenient menu bar application that lives in your Mac's status bar. Click to convert times from your clipboard instantly.

```bash
python3 timezone_menubar.py
```

Or double-click `start_timezone_app.command` to launch.

## Installation

### Requirements
- Python 3.7+
- macOS (for menu bar app)

### Setup

1. Clone this repository:
```bash
git clone https://github.com/yourusername/timezone-converter.git
cd timezone-converter
```

2. Install dependencies:
```bash
pip3 install pyperclip rumps
```

## Usage

### Supported Time Formats
The converter recognizes various time formats:
- `3 PM EST`
- `9:30 AM PST`
- `15:00 UTC`
- `6:49 PM (PDT)`
- `Meeting at 3:30:45 PM EST tomorrow` (extracts time from text)

### Supported Timezones
- EST/EDT (Eastern)
- CST/CDT (Central)
- MST/MDT (Mountain)
- PST/PDT (Pacific)
- UTC/GMT
- BST (British Summer Time)
- CET (Central European)
- IST (India)
- JST (Japan)
- AEST/AEDT (Australian Eastern)

## Auto-Start Menu Bar App (macOS)

To have the menu bar app start automatically on login:

1. Open **System Settings** → **General** → **Login Items**
2. Click the **"+"** button
3. Select `start_timezone_app.command`
4. Click **Add**

Now the timezone converter will be available in your menu bar every time you start your Mac!

## How It Works

The project uses:
- **Python's `zoneinfo` module** for accurate timezone conversions
- **Regular expressions** to parse various time formats from text
- **pyperclip** for clipboard monitoring
- **rumps** for the macOS menu bar interface

## Use Cases

Perfect for:
- 📧 Reading emails from international colleagues
- 🗓️ Scheduling meetings across timezones
- 💬 Following up on Slack messages with different timezone references
- 🌐 Working with remote teams

## Project Structure

```
timezone-converter/
├── timezone_converter.py      # Core conversion logic & CLI tool
├── Clipboard_Monitor.py        # Automatic clipboard monitoring
├── timezone_menubar.py         # Mac menu bar application
├── start_timezone_app.command  # Launcher script for menu bar app
└── README.md                   # This file
```

## Contributing

Feel free to open issues or submit pull requests if you'd like to:
- Add more timezone support
- Improve time format recognition
- Add new features

## License

MIT License - feel free to use this in your own projects!

## Author

Built with ☕ and curiosity about timezones.

---

*Made possible with Python, a lot of regex, and the realization that timezones are harder than they look!*
