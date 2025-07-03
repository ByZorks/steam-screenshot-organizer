# Steam Screenshots Organizer

This is a simple Python script that organizes your Steam screenshots into folders based on the game they belong to. It
scans the Steam screenshot directory, identifies the games, and moves the screenshots into corresponding folders. This
script is useful for keeping your Steam screenshots organized and easily accessible. For now, it only supports Windows.

## What it can do

- Automatically organize Steam screenshots into game-specific folders.
- Automatically detect Steam's screenshot directory.
    - Users can specify a custom directory if needed.

# Build Executable using PyInstaller

## Install PyInstaller

```bash
pip install -U pyinstaller
```

## Build the Executable

```bash
pyinstaller .\Main.py --distpath "../dist" --name "Steam Screenshots Organizer" --workpath "../build" --specpath "../"
```
