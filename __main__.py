import subprocess
import sys
import configparser
import shlex
import os

config = configparser.ConfigParser()
config.read('config.ini')

APP_NAME = config['DEFAULT']['app_name']
RCLONE_PATH = config['DEFAULT']['rclone_url']


def start_rclone(commands):
    subprocess.Popen(
        commands,
        creationflags=subprocess.CREATE_NO_WINDOW,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )


def build_executable():
    script_path = os.path.abspath(__file__)

    pyinstaller_path = subprocess.check_output(["where", "pyinstaller"], universal_newlines=True).strip()

    subprocess.run([
        pyinstaller_path,
        "--noconsole",
        "--onefile",
        "--name", APP_NAME,
        script_path
    ])



def main():
    for section in config.sections():
        if 'rclone_args' in config[section]:
            args = shlex.split(config[section]['rclone_args'])
            cmd = [RCLONE_PATH] + args
            start_rclone(cmd)


if __name__ == "__main__":
    if "--build" in sys.argv:
        build_executable()
    else:
        if sys.platform == "win32":
            import ctypes
            ctypes.windll.user32.ShowWindow(
                ctypes.windll.kernel32.GetConsoleWindow(), 0)

        main()
