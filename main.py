import time
from modules import wifi, inject, system
from rich.console import Console


index = int(time.time())
console = Console()

try:
    # wifi.get_wifi_report(index)
    # system.get_system_info(index)
    inject.start()
except Exception:
    console.print_exception(show_locals=True)
