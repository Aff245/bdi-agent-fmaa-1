import subprocess

def get_battery_status():
    result = subprocess.run(['termux-battery-status'], capture_output=True, text=True)
    return result.stdout
