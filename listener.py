# Import required modules from pynput.keyboard and time
from pynput.keyboard import Key, Listener
import time

# Define the output file name
outputFile = "output.txt"

def formatKey(key):
    dict_key = {
    "\x08": "Backspace",       # Backspace character
    "\x09": "Tab",             # Tab character
    "\x0A": "Line Feed",       # Line Feed character (newline)
    "\x0D": "Carriage Return", # Carriage Return character
    "\x1B": "Escape",          # Escape character
    "\x20": "Space",           # Space character
    "\x21": "!",               # Exclamation Mark character
    "\x22": '"',               # Double Quote character
    "\x23": "#",               # Hash character
    "\x24": "$",               # Dollar character
    "\x25": "%",               # Percent character
    "\x26": "&",               # Ampersand character
    "\x27": "'",               # Single Quote character
    "\x28": "(",               # Left Parenthesis character
    "\x29": ")",               # Right Parenthesis character
    "\x2A": "*",               # Asterisk character
    "\x2B": "+",               # Plus character
    "\x2C": ",",               # Comma character
    "\x2D": "-",               # Minus character
    "\x2E": ".",               # Period character
    "\x2F": "/",               # Slash character
    "\x3A": ":",               # Colon character
    "\x3B": ";",               # Semicolon character
    "\x3C": "<",               # Less Than character
    "\x3D": "=",               # Equal character
    "\x3E": ">",               # Greater Than character
    "\x3F": "?",               # Question Mark character
    "\x40": "@",               # At character
    "\x5B": "[",               # Left Square Bracket character
    "\x5C": "\\",              # Backslash character
    "\x5D": "]",               # Right Square Bracket character
    "\x5E": "^",               # Caret character
    "\x5F": "_",               # Underscore character
    "\x60": "`",               # Grave Accent character
    "\x7B": "{",               # Left Curly Brace character
    "\x7C": "|",               # Vertical Bar character
    "\x7D": "}",               # Right Curly Brace character
    "\x7E": "~",               # Tilde character
    "\x7F": "Delete",          # Delete character
    "\x1A": "Ctrl + Z",        # Ctrl + Z key combination
    "\x03": "Ctrl + C",        # Ctrl + C key combination
    "\x04": "Ctrl + D"         # Ctrl + D key combination
    }
    if key in dict_key:
        return dict_key[key]
    else:
        return key

# Function to handle key press events
def onKeyPress(key):
    char = key
    currentTime = time.strftime("%H:%M:%S") # Get current time in 24-Hour format
    print(f'Press: {formatKey(char)} \t at {currentTime}') # Print the formatted key and timestamp in the console
    with open(outputFile, "a+") as file:
        file.write(f'{formatKey(char)} \t at {currentTime}\n') # Write the formatted key and timestamp to the output file

# Function to handle key release events
def onKeyRelease(key):
    print(f'Release: {formatKey(key)}')    # Print the released key to the console
    if formatKey(key) == Key.esc:
        return False    # Stop the listener if ESC is pressed

# Set up listener for keyboard events
with Listener(on_press = onKeyPress, on_release = onKeyRelease) as listener:
    listener.join() # Start the listener and wait for events