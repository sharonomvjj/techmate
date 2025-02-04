import subprocess
import platform
import ctypes
from datetime import datetime

class TechMate:
    def __init__(self):
        self.os_name = platform.system()

    def is_admin(self):
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    def synchronize_time(self):
        if self.os_name != "Windows":
            print("This program only supports Windows operating system.")
            return

        if not self.is_admin():
            print("Please run this program as an administrator.")
            return

        try:
            print("Synchronizing system clock with internet time servers...")
            subprocess.check_call(["w32tm", "/resync"])
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"System time synchronized successfully. Current time is {current_time}.")
        except subprocess.CalledProcessError as e:
            print("Failed to synchronize time. Please ensure your internet connection is active and try again.")
            print("Error:", e)

if __name__ == "__main__":
    techmate = TechMate()
    techmate.synchronize_time()