# Rclone Auto-Mounter

A lightweight Python utility that automatically mounts multiple remote drives (e.g., Dropbox, OneDrive) using [rclone](https://rclone.org/). Each mount is configured through a simple `config.ini` file. The script runs silently in the background and can be compiled into a standalone `.exe` for Windows.

## Features

-   🔧 Configure multiple mount points easily via `config.ini`
-   💾 Supports any rclone-compatible remote (Dropbox, Google Drive, OneDrive, etc.)
-   🕶️ Runs completely hidden (no console window)
-   📦 Build a background `.exe` with a single command (`--build`)

## Usage

### Configuration

Before running the script, you need to configure it through the `config.ini` file. Start by renaming the `config.example.ini` file to `config.ini` and modifying it according to your needs.

### Installation

1. [**Install Python** (3.6+)](https://www.python.org/downloads)
2. [**Install Rclone** and set up your remotes](https://rclone.org/downloads)
3. [**Install Winfsp**](https://winfsp.dev/rel/)
4. **Install PyInstaller** (for building `.exe`):
    ```bash
    pip install pyinstaller
    ```

### Running the Script

To run the script and mount path in the background, simply execute the following command in your terminal:

```bash
python __main__.py
```

or

```bash
python __main__.py --build
```

for getting the .exe.
