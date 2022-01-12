import subprocess
from rich import print


def get_system_info(folder):

    print("[bold green]Exporting systeminfo ...[/bold green]")
    results = subprocess.check_output('systeminfo')
    results = results.decode('cp866')
    results = results.replace('\r', '')

    file = open('./reports/{0}_systeminfo.log'.format(folder), 'w')
    file.write(results)
    file.close()
