import keyboard
import time

keys_dict = {
    # 'cmd': 'cmd',
    # 'shift': 'shift',
    'space': 'space',
    # 'tab': 'tab',
    # 'alt_l': 'alt',
    # 'down': 'down',
    # 'esc': 'esc',
    # 'home': 'home',
    # 'ctrl_l': 'ctrl',
    # 'caps_lock': 'caps_lock',
    'backspace': 'backspace',
    'enter': 'enter',
}

def parse_file(filename):
    time.sleep(3)
    with open(filename, 'r') as log:
        for line in log:
            key = line[29:].strip()
            if ~key.find("\'"):
                if ~key.find('\\x'):
                    print(key[1:-1])
                else:
                    keyboard.press_and_release(key[1])
            else:
                if key[4:] in keys_dict:
                    keyboard.press_and_release(keys_dict[key[4:]])
    return unique


def main():
    output = parse_file('example.txt')
    print(output)

if __name__ == "__main__":
    main()
