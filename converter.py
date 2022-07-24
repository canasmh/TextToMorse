intro_text = """
Welcome to TextToMorse!

The easy-to-use python converter that converts a string of characters into Morse code.

Morse code is composed of dots '.' and dashes '-'. Dots have a time value of one unit whereas dashes have a value of
three units. Space between parts of the same letter is one unit, space between letters is three units, and space 
between words is seven units. 

For purposes of this script, letters are separated by a three empty characters (i.e., "   ") and words are separated by
a new line. There is no spaces between parts of the same letter\n"""

char_to_morse = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "10": "-----"
}


def convert_to_morse(input_text):
    converted_text = ""
    for char in input_text:
        try:
            char_to_morse[char]
        except KeyError:
            if char == " ":
                converted_text += "\n"
            else:
                continue
        else:
            converted_text += char_to_morse[char]
            converted_text += "   "

    return converted_text

