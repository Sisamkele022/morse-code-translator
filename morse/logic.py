MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',

    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ' ': '/'
}

REVERSE_MORSE_CODE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}


def text_to_morse(text):
    return ' '.join(MORSE_CODE_DICT.get(char.upper(), '') for char in text if char.upper() in MORSE_CODE_DICT)


def morse_to_text(morse_code):
    """
    Decode Morse code string into readable text.
    Words are separated by '/' or ' / '
    Letters are separated by spaces.
    """
    text = []
    words = morse_code.strip().split(' / ') if ' / ' in morse_code else morse_code.strip().split('/')
    for word in words:
        letters = word.strip().split()
        decoded_word = ''.join(REVERSE_MORSE_CODE_DICT.get(letter, '') for letter in letters)
        text.append(decoded_word)
    return ' '.join(text)
