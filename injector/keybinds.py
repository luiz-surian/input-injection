# msdn.microsoft.com/en-us/library/dd375731
VK = {
    'LBUTTON': 0x01,  # Left mouse button
    'RBUTTON': 0x02,  # Right mouse button
    'CANCEL': 0x03,  # Control-break processing
    'MBUTTON': 0x04,  # Middle mouse button (three-button mouse)
    'XBUTTON1': 0x05,  # X1 mouse button
    'XBUTTON2': 0x06,  # X2 mouse button
    'BACK': 0x08,  # BACKSPACE key
    'TAB': 0x09,  # TAB key
    'CLEAR': 0x0C,  # CLEAR key
    'RETURN': 0x0D,  # ENTER key
    'SHIFT': 0x10,  # SHIFT key
    'CONTROL': 0x11,  # CTRL key
    'MENU': 0x12,  # ALT key
    'PAUSE': 0x13,  # PAUSE key
    'CAPITAL': 0x14,  # CAPS LOCK key
    'ESCAPE': 0x1B,  # ESC key
    'SPACE': 0x20,  # SPACEBAR
    'PRIOR': 0x21,  # PAGE UP key
    'NEXT': 0x22,  # PAGE DOWN key
    'END': 0x23,  # END key
    'HOME': 0x24,  # HOME key
    'LEFT': 0x25,  # LEFT ARROW key
    'UP': 0x26,  # UP ARROW key
    'RIGHT': 0x27,  # RIGHT ARROW key
    'DOWN': 0x28,  # DOWN ARROW key
    'SELECT': 0x29,  # SELECT key
    'PRINT': 0x2A,  # PRINT key
    'EXECUTE': 0x2B,  # EXECUTE key
    'SNAPSHOT': 0x2C,  # PRINT SCREEN key
    'INSERT': 0x2D,  # INS key
    'DELETE': 0x2E,  # DEL key
    'HELP': 0x2F,  # HELP key
    '0': 0x30,  # 0 key
    '1': 0x31,  # 1 key
    '2': 0x32,  # 2 key
    '3': 0x33,  # 3 key
    '4': 0x34,  # 4 key
    '5': 0x35,  # 5 key
    '6': 0x36,  # 6 key
    '7': 0x37,  # 7 key
    '8': 0x38,  # 8 key
    '9': 0x39,  # 9 key
    'A': 0x41,  # A key
    'B': 0x42,  # B key
    'C': 0x43,  # C key
    'D': 0x44,  # D key
    'E': 0x45,  # E key
    'F': 0x46,  # F key
    'G': 0x47,  # G key
    'H': 0x48,  # H key
    'I': 0x49,  # I key
    'J': 0x4A,  # J key
    'K': 0x4B,  # K key
    'L': 0x4C,  # L key
    'M': 0x4D,  # M key
    'N': 0x4E,  # N key
    'O': 0x4F,  # O key
    'P': 0x50,  # P key
    'Q': 0x51,  # Q key
    'R': 0x52,  # R key
    'S': 0x53,  # S key
    'T': 0x54,  # T key
    'U': 0x55,  # U key
    'V': 0x56,  # V key
    'W': 0x57,  # W key
    'X': 0x58,  # X key
    'Y': 0x59,  # Y key
    'Z': 0x5A,  # Z key
    'LWIN': 0x5B,  # Left Windows key (Natural keyboard)
    'RWIN': 0x5C,  # Right Windows key (Natural keyboard)
    'APPS': 0x5D,  # Applications key (Natural keyboard)
    'SLEEP': 0x5F,  # Computer Sleep key
    'NUMPAD0': 0x60,  # Numeric keypad 0 key
    'NUMPAD1': 0x61,  # Numeric keypad 1 key
    'NUMPAD2': 0x62,  # Numeric keypad 2 key
    'NUMPAD3': 0x63,  # Numeric keypad 3 key
    'NUMPAD4': 0x64,  # Numeric keypad 4 key
    'NUMPAD5': 0x65,  # Numeric keypad 5 key
    'NUMPAD6': 0x66,  # Numeric keypad 6 key
    'NUMPAD7': 0x67,  # Numeric keypad 7 key
    'NUMPAD8': 0x68,  # Numeric keypad 8 key
    'NUMPAD9': 0x69,  # Numeric keypad 9 key
    'MULTIPLY': 0x6A,  # Multiply key (*)
    'ADD': 0x6B,  # Add key (+)
    'SEPARATOR': 0x6C,  # Separator key (.)
    'SUBTRACT': 0x6D,  # Subtract key (-)
    'DECIMAL': 0x6E,  # Decimal key (,)
    'DIVIDE': 0x6F,  # Divide key (/)
    'F1': 0x70,  # F1 key
    'F2': 0x71,  # F2 key
    'F3': 0x72,  # F3 key
    'F4': 0x73,  # F4 key
    'F5': 0x74,  # F5 key
    'F6': 0x75,  # F6 key
    'F7': 0x76,  # F7 key
    'F8': 0x77,  # F8 key
    'F9': 0x78,  # F9 key
    'F10': 0x79,  # F10 key
    'F11': 0x7A,  # F11 key
    'F12': 0x7B,  # F12 key
    'F13': 0x7C,  # F13 key
    'F14': 0x7D,  # F14 key
    'F15': 0x7E,  # F15 key
    'F16': 0x7F,  # F16 key
    'F17': 0x80,  # F17 key
    'F18': 0x81,  # F18 key
    'F19': 0x82,  # F19 key
    'F20': 0x83,  # F20 key
    'F21': 0x84,  # F21 key
    'F22': 0x85,  # F22 key
    'F23': 0x86,  # F23 key
    'F24': 0x87,  # F24 key
    'NUMLOCK': 0x90,  # NUM LOCK key
    'SCROLL': 0x91,  # SCROLL LOCK key
    'LSHIFT': 0xA0,  # Left SHIFT key
    'RSHIFT': 0xA1,  # Right SHIFT key
    'LCONTROL': 0xA2,  # Left CONTROL key
    'RCONTROL': 0xA3,  # Right CONTROL key
    'LMENU': 0xA4,  # Left MENU key
    'RMENU': 0xA5,  # Right MENU key
    'BROWSER_BACK': 0xA6,  # Browser Back key
    'BROWSER_FORWARD': 0xA7,  # Browser Forward key
    'BROWSER_REFRESH': 0xA8,  # Browser Refresh key
    'BROWSER_STOP': 0xA9,  # Browser Stop key
    'BROWSER_SEARCH': 0xAA,  # Browser Search key
    'BROWSER_FAVORITES': 0xAB,  # Browser Favorites key
    'BROWSER_HOME': 0xAC,  # Browser Start and Home key
    'VOLUME_MUTE': 0xAD,  # Volume Mute key
    'VOLUME_DOWN': 0xAE,  # Volume Down key
    'VOLUME_UP': 0xAF,  # Volume Up key
    'MEDIA_NEXT_TRACK': 0xB0,  # Next Track key
    'MEDIA_PREV_TRACK': 0xB1,  # Previous Track key
    'MEDIA_STOP': 0xB2,  # Stop Media key
    'MEDIA_PLAY_PAUSE': 0xB3,  # Play/Pause Media key
    'LAUNCH_MAIL': 0xB4,  # Start Mail key
    'LAUNCH_MEDIA_SELECT': 0xB5,  # Select Media key
    'LAUNCH_APP1': 0xB6,  # Start Application 1 key
    'LAUNCH_APP2': 0xB7,  # Start Application 2 key
    # The codes below are used for miscellaneous characters,
    # they can vary by keyboard country/region.
    'OEM_1': 0xBA,  # For the US standard keyboard, the ';:' key
    'OEM_PLUS': 0xBB,  # For any country/region, the '+' key
    'OEM_COMMA': 0xBC,  # For any country/region, the ',' key
    'OEM_MINUS': 0xBD,  # For any country/region, the '-' key
    'OEM_PERIOD': 0xBE,  # For any country/region, the '.' key
    'OEM_2': 0xBF,  # For the US standard keyboard, the '/?' key
    'OEM_3': 0xC0,  # For the US standard keyboard, the '`~' key
    'OEM_4': 0xDB,  # For the US standard keyboard, the '[{' key
    'OEM_5': 0xDC,  # For the US standard keyboard, the '\|' key
    'OEM_6': 0xDD,  # For the US standard keyboard, the ']}' key
    'OEM_7': 0xDE,  # For the US standard keyboard,
                    # the 'single-quote/double-quote' key
    'OEM_8': 0xDF,  # it can vary by keyboard.
    'OEM_102': 0xE2,  # Either the angle bracket key or the
                      # backslash key on the RT 102-key keyboard
}

ALIAS = {
    'CAPSLOCK': 'CAPITAL',
    'ESC': 'ESCAPE',
    'PAGE_UP': 'PRIOR',
    'PAGE_DOWN': 'NEXT',
    'PRINT_SCREEN': 'SNAPSHOT',
    'ALT': 'LMENU',
    'ALT_GR': 'RMENU',
    'ENTER': 'RETURN',
    '\n': 'RETURN',
    ' ': 'SPACE',
    '*': 'MULTIPLY',
    '/': 'DIVIDE',
    # 'Ç': 'OEM_1',
    '=': 'OEM_PLUS',  # SHIFT +
    ',': 'OEM_COMMA',  # SHIFT <
    '-': 'OEM_MINUS',  # SHIFT _
    '.': 'OEM_PERIOD',  # SHIFT >
    ';': 'OEM_2',  # SHIFT :
    '\'': 'OEM_3',  # SHIFT "
    # '´': 'OEM_4',  # SHIFT `
    ']': 'OEM_5',  # SHIFT }
    '[': 'OEM_6',  # SHIFT {
    # '~': 'OEM_7',  # SHIFT ^
    '\\': 'OEM_102',  # SHIFT |
    # SPECIALS
    '?': ['ALT_GR', 'W'],
    '+': ['LSHIFT', '='],
    '<': ['LSHIFT', ','],
    '_': ['LSHIFT', '-'],
    '>': ['LSHIFT', '.'],
    ':': ['LSHIFT', ';'],
    '"': ['LSHIFT', '\''],
    # '`': ['LSHIFT', '´'],
    '}': ['LSHIFT', ']'],
    '{': ['LSHIFT', '['],
    '^': ['LSHIFT', '~'],
    '|': ['LSHIFT', '\\'],
    '!': ['LSHIFT', '1'],
    '@': ['LSHIFT', '2'],
    '#': ['LSHIFT', '3'],
    '$': ['LSHIFT', '4'],
    '%': ['LSHIFT', '5'],
    '&': ['LSHIFT', '7'],
    '(': ['LSHIFT', '9'],
    ')': ['LSHIFT', '0'],
    # '¹': ['ALT_GR', '1'],
    # '²': ['ALT_GR', '2'],
    # '³': ['ALT_GR', '3'],
    # '£': ['ALT_GR', '4'],
    # '¢': ['ALT_GR', '5'],
    # '¬': ['ALT_GR', '6'],
    # '§': ['ALT_GR', '='],
    # 'ª': ['ALT_GR', '['],
    # 'º': ['ALT_GR', ']'],
    # '°': ['ALT_GR', '/'],
    '☺': {'function': 'alt_code', 'value': 1},
    '☻': {'function': 'alt_code', 'value': 2},
    '♥': {'function': 'alt_code', 'value': 3},
    '♦': {'function': 'alt_code', 'value': 4},
    '♣': {'function': 'alt_code', 'value': 5},
    '♠': {'function': 'alt_code', 'value': 6},
    '•': {'function': 'alt_code', 'value': 7},
    '◘': {'function': 'alt_code', 'value': 8},
    '○': {'function': 'alt_code', 'value': 9},
    '◙': {'function': 'alt_code', 'value': 10},
    '♂': {'function': 'alt_code', 'value': 11},
    '♀': {'function': 'alt_code', 'value': 12},
    '♪': {'function': 'alt_code', 'value': 13},
    '♫': {'function': 'alt_code', 'value': 14},
    '☼': {'function': 'alt_code', 'value': 15},
    '►': {'function': 'alt_code', 'value': 16},
    '◄': {'function': 'alt_code', 'value': 17},
    '↕': {'function': 'alt_code', 'value': 18},
    '‼': {'function': 'alt_code', 'value': 19},
    '¶': {'function': 'alt_code', 'value': 20},
    '§': {'function': 'alt_code', 'value': 21},
    '▬': {'function': 'alt_code', 'value': 22},
    '↨': {'function': 'alt_code', 'value': 23},
    '↑': {'function': 'alt_code', 'value': 24},
    '↓': {'function': 'alt_code', 'value': 25},
    '→': {'function': 'alt_code', 'value': 26},
    '←': {'function': 'alt_code', 'value': 27},
    '∟': {'function': 'alt_code', 'value': 28},
    '↔': {'function': 'alt_code', 'value': 29},
    '▲': {'function': 'alt_code', 'value': 30},
    '▼': {'function': 'alt_code', 'value': 31},
    '`': {'function': 'alt_code', 'value': 96},
    '~': {'function': 'alt_code', 'value': 126},
    '⌂': {'function': 'alt_code', 'value': 127},
    'Ç': {'function': 'alt_code', 'value': 128},
    'ü': {'function': 'alt_code', 'value': 129},
    'é': {'function': 'alt_code', 'value': 130},
    'â': {'function': 'alt_code', 'value': 131},
    'ä': {'function': 'alt_code', 'value': 132},
    'à': {'function': 'alt_code', 'value': 133},
    'å': {'function': 'alt_code', 'value': 134},
    'ç': {'function': 'alt_code', 'value': 135},
    'ê': {'function': 'alt_code', 'value': 136},
    'ë': {'function': 'alt_code', 'value': 137},
    'è': {'function': 'alt_code', 'value': 138},
    'ï': {'function': 'alt_code', 'value': 139},
    'î': {'function': 'alt_code', 'value': 140},
    'ì': {'function': 'alt_code', 'value': 141},
    'Ä': {'function': 'alt_code', 'value': 142},
    'Å': {'function': 'alt_code', 'value': 143},
    'É': {'function': 'alt_code', 'value': 144},
    'æ': {'function': 'alt_code', 'value': 145},
    'Æ': {'function': 'alt_code', 'value': 146},
    'ô': {'function': 'alt_code', 'value': 147},
    'ö': {'function': 'alt_code', 'value': 148},
    'ò': {'function': 'alt_code', 'value': 149},
    'û': {'function': 'alt_code', 'value': 150},
    'ù': {'function': 'alt_code', 'value': 151},
    'ÿ': {'function': 'alt_code', 'value': 152},
    'Ö': {'function': 'alt_code', 'value': 153},
    'Ü': {'function': 'alt_code', 'value': 154},
    'ø': {'function': 'alt_code', 'value': 155},
    '£': {'function': 'alt_code', 'value': 156},
    'Ø': {'function': 'alt_code', 'value': 157},
    '×': {'function': 'alt_code', 'value': 158},
    'ƒ': {'function': 'alt_code', 'value': 159},
    'á': {'function': 'alt_code', 'value': 160},
    'í': {'function': 'alt_code', 'value': 161},
    'ó': {'function': 'alt_code', 'value': 162},
    'ú': {'function': 'alt_code', 'value': 163},
    'ñ': {'function': 'alt_code', 'value': 164},
    'Ñ': {'function': 'alt_code', 'value': 165},
    'ª': {'function': 'alt_code', 'value': 166},
    'º': {'function': 'alt_code', 'value': 167},
    '¿': {'function': 'alt_code', 'value': 168},
    '®': {'function': 'alt_code', 'value': 169},
    '¬': {'function': 'alt_code', 'value': 170},
    '½': {'function': 'alt_code', 'value': 171},
    '¼': {'function': 'alt_code', 'value': 172},
    '¡': {'function': 'alt_code', 'value': 173},
    '«': {'function': 'alt_code', 'value': 174},
    '»': {'function': 'alt_code', 'value': 175},
    '░': {'function': 'alt_code', 'value': 176},
    '▒': {'function': 'alt_code', 'value': 177},
    '▓': {'function': 'alt_code', 'value': 178},
    '│': {'function': 'alt_code', 'value': 179},
    '┤': {'function': 'alt_code', 'value': 180},
    'Á': {'function': 'alt_code', 'value': 181},
    'Â': {'function': 'alt_code', 'value': 182},
    'À': {'function': 'alt_code', 'value': 183},
    '©': {'function': 'alt_code', 'value': 184},
    '╣': {'function': 'alt_code', 'value': 185},
    '║': {'function': 'alt_code', 'value': 186},
    '╗': {'function': 'alt_code', 'value': 187},
    '╝': {'function': 'alt_code', 'value': 188},
    '¢': {'function': 'alt_code', 'value': 189},
    '¥': {'function': 'alt_code', 'value': 190},
    '┐': {'function': 'alt_code', 'value': 191},
    '└': {'function': 'alt_code', 'value': 192},
    '┴': {'function': 'alt_code', 'value': 193},
    '┬': {'function': 'alt_code', 'value': 194},
    '├': {'function': 'alt_code', 'value': 195},
    '─': {'function': 'alt_code', 'value': 196},
    '┼': {'function': 'alt_code', 'value': 197},
    'ã': {'function': 'alt_code', 'value': 198},
    'Ã': {'function': 'alt_code', 'value': 199},
    '╚': {'function': 'alt_code', 'value': 200},
    '╔': {'function': 'alt_code', 'value': 201},
    '╩': {'function': 'alt_code', 'value': 202},
    '╦': {'function': 'alt_code', 'value': 203},
    '╠': {'function': 'alt_code', 'value': 204},
    '═': {'function': 'alt_code', 'value': 205},
    '╬': {'function': 'alt_code', 'value': 206},
    '¤': {'function': 'alt_code', 'value': 207},
    'ð': {'function': 'alt_code', 'value': 208},
    'Ð': {'function': 'alt_code', 'value': 209},
    'Ê': {'function': 'alt_code', 'value': 210},
    'Ë': {'function': 'alt_code', 'value': 211},
    'È': {'function': 'alt_code', 'value': 212},
    'ı': {'function': 'alt_code', 'value': 213},
    'Í': {'function': 'alt_code', 'value': 214},
    'Î': {'function': 'alt_code', 'value': 215},
    'Ï': {'function': 'alt_code', 'value': 216},
    '┘': {'function': 'alt_code', 'value': 217},
    '┌': {'function': 'alt_code', 'value': 218},
    '█': {'function': 'alt_code', 'value': 219},
    '▄': {'function': 'alt_code', 'value': 220},
    '¦': {'function': 'alt_code', 'value': 221},
    'Ì': {'function': 'alt_code', 'value': 222},
    '▀': {'function': 'alt_code', 'value': 223},
    'Ó': {'function': 'alt_code', 'value': 224},
    'ß': {'function': 'alt_code', 'value': 225},
    'Ô': {'function': 'alt_code', 'value': 226},
    'Ò': {'function': 'alt_code', 'value': 227},
    'õ': {'function': 'alt_code', 'value': 228},
    'Õ': {'function': 'alt_code', 'value': 229},
    'µ': {'function': 'alt_code', 'value': 230},
    'þ': {'function': 'alt_code', 'value': 231},
    'Þ': {'function': 'alt_code', 'value': 232},
    'Ú': {'function': 'alt_code', 'value': 233},
    'Û': {'function': 'alt_code', 'value': 234},
    'Ù': {'function': 'alt_code', 'value': 235},
    'ý': {'function': 'alt_code', 'value': 236},
    'Ý': {'function': 'alt_code', 'value': 237},
    '¯': {'function': 'alt_code', 'value': 238},
    '´': {'function': 'alt_code', 'value': 239},
    '±': {'function': 'alt_code', 'value': 241},
    '‗': {'function': 'alt_code', 'value': 242},
    '¾': {'function': 'alt_code', 'value': 243},
    # '¶': {'function': 'alt_code', 'value': 244},
    # '§': {'function': 'alt_code', 'value': 245},
    '÷': {'function': 'alt_code', 'value': 246},
    '¸': {'function': 'alt_code', 'value': 247},
    '°': {'function': 'alt_code', 'value': 248},
    '¨': {'function': 'alt_code', 'value': 249},
    '·': {'function': 'alt_code', 'value': 250},
    '¹': {'function': 'alt_code', 'value': 251},
    '³': {'function': 'alt_code', 'value': 252},
    '²': {'function': 'alt_code', 'value': 253},
    '■': {'function': 'alt_code', 'value': 254},
}

QUICK = {
    '←': 'BACK',
    '¶': 'RETURN',
}
