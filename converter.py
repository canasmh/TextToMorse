intro_text = """
Welcome to TextToMorse!

The easy-to-use python converter that converts a string of characters into Morse code.

Morse code is composed of dots '.' and dashes '-'. Dots have a time value of one unit whereas dashes have a value of
three units. Space between parts of the same letter is one unit, space between letters is three units, and space 
between words is seven units. 

For purposes of this script, letters are separated by a single empty character (i.e., " ") and words are separated by
a new line\n"""

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