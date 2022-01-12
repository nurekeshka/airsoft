import subprocess
from rich import print


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
