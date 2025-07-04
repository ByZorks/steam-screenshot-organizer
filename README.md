# Steam Screenshots Organizer

This is a simple Python script that organizes your Steam screenshots into folders based on the game they belong to. It
scans the Steam screenshot directory, identifies the games, and moves the screenshots into corresponding folders. This
script is useful for keeping your Steam screenshots organized and easily accessible. For now, it only supports Windows.

## Functionalities

- Automatically organize Steam screenshots into game-specific folders.
- Automatically detect Steam's screenshot directory.
    - Users can specify a custom directory if needed.

## How to Use with Python

1. Clone the repository.
2. Make sure you have Python installed on your system.
3. Install the required dependencies by running:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the script:
   ```bash
    python Main.py
    ```

## Build Executable using PyInstaller

### Install PyInstaller

```bash
pip install -U pyinstaller
```

### Build the Executable

```bash
pyinstaller .\Main.py --distpath "../dist" --name "Steam Screenshots Organizer" --workpath "../build" --specpath "../"
```

## License

This project is licensed under GNU General Public License v3.0. See the [LICENSE](COPYING) file for details.