# Morse Code dictionary
MORSE_CODE_DICT = {
    'A': '.-',     'B': '-...',   'C': '-.-.', 
    'D': '-..',    'E': '.',      'F': '..-.',
    'G': '--.',    'H': '....',   'I': '..',
    'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',
    'S': '...',    'T': '-',      'U': '..-',
    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',
    '0': '-----',  '1': '.----',  '2': '..---',
    '3': '...--',  '4': '....-',  '5': '.....',
    '6': '-....',  '7': '--...',  '8': '---..',
    '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..',
    "'": '.----.', '!': '-.-.--', '/': '-..-.',
    '(': '-.--.',  ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.',  '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
    ' ': '/'  # Use slash for space between words
}

# Reverse lookup
REVERSE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}


def letters_to_morse(text):
    text = text.upper()
    return ' '.join(MORSE_CODE_DICT.get(char, '') for char in text)


def morse_to_letters(code):
    words = code.split(' / ')
    decoded_words = []

    for word in words:
        letters = word.strip().split()
        decoded_letters = [REVERSE_DICT.get(l, '') for l in letters]
        decoded_words.append(''.join(decoded_letters))

    return ' '.join(decoded_words)
