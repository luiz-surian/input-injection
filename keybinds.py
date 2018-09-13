# msdn.microsoft.com/en-us/library/dd375731
VK = {
    'LBUTTON'             : 0x01, # Left mouse button
    'RBUTTON'             : 0x02, # Right mouse button
    'CANCEL'              : 0x03, # Control-break processing
    'MBUTTON'             : 0x04, # Middle mouse button (three-button mouse)
    'XBUTTON1'            : 0x05, # X1 mouse button
    'XBUTTON2'            : 0x06, # X2 mouse button
    'BACK'                : 0x08, # BACKSPACE key
    'TAB'                 : 0x09, # TAB key
    'CLEAR'               : 0x0C, # CLEAR key
    'RETURN'              : 0x0D, # ENTER key
    'SHIFT'               : 0x10, # SHIFT key
    'CONTROL'             : 0x11, # CTRL key
    'MENU'                : 0x12, # ALT key
    'PAUSE'               : 0x13, # PAUSE key
    'CAPITAL'             : 0x14, # CAPS LOCK key
    'ESCAPE'              : 0x1B, # ESC key
    'SPACE'               : 0x20, # SPACEBAR
    'PRIOR'               : 0x21, # PAGE UP key
    'NEXT'                : 0x22, # PAGE DOWN key
    'END'                 : 0x23, # END key
    'HOME'                : 0x24, # HOME key
    'LEFT'                : 0x25, # LEFT ARROW key
    'UP'                  : 0x26, # UP ARROW key
    'RIGHT'               : 0x27, # RIGHT ARROW key
    'DOWN'                : 0x28, # DOWN ARROW key
    'SELECT'              : 0x29, # SELECT key
    'PRINT'               : 0x2A, # PRINT key
    'EXECUTE'             : 0x2B, # EXECUTE key
    'SNAPSHOT'            : 0x2C, # PRINT SCREEN key
    'INSERT'              : 0x2D, # INS key
    'DELETE'              : 0x2E, # DEL key
    'HELP'                : 0x2F, # HELP key
    '0'                   : 0x30, # 0 key
    '1'                   : 0x31, # 1 key
    '2'                   : 0x32, # 2 key
    '3'                   : 0x33, # 3 key
    '4'                   : 0x34, # 4 key
    '5'                   : 0x35, # 5 key
    '6'                   : 0x36, # 6 key
    '7'                   : 0x37, # 7 key
    '8'                   : 0x38, # 8 key
    '9'                   : 0x39, # 9 key
    'A'                   : 0x41, # A key
    'B'                   : 0x42, # B key
    'C'                   : 0x43, # C key
    'D'                   : 0x44, # D key
    'E'                   : 0x45, # E key
    'F'                   : 0x46, # F key
    'G'                   : 0x47, # G key
    'H'                   : 0x48, # H key
    'I'                   : 0x49, # I key
    'J'                   : 0x4A, # J key
    'K'                   : 0x4B, # K key
    'L'                   : 0x4C, # L key
    'M'                   : 0x4D, # M key
    'N'                   : 0x4E, # N key
    'O'                   : 0x4F, # O key
    'P'                   : 0x50, # P key
    'Q'                   : 0x51, # Q key
    'R'                   : 0x52, # R key
    'S'                   : 0x53, # S key
    'T'                   : 0x54, # T key
    'U'                   : 0x55, # U key
    'V'                   : 0x56, # V key
    'W'                   : 0x57, # W key
    'X'                   : 0x58, # X key
    'Y'                   : 0x59, # Y key
    'Z'                   : 0x5A, # Z key
    'LWIN'                : 0x5B, # Left Windows key (Natural keyboard) 
    'RWIN'                : 0x5C, # Right Windows key (Natural keyboard)
    'APPS'                : 0x5D, # Applications key (Natural keyboard)
    'SLEEP'               : 0x5F, # Computer Sleep key
    'NUMPAD0'             : 0x60, # Numeric keypad 0 key
    'NUMPAD1'             : 0x61, # Numeric keypad 1 key
    'NUMPAD2'             : 0x62, # Numeric keypad 2 key
    'NUMPAD3'             : 0x63, # Numeric keypad 3 key
    'NUMPAD4'             : 0x64, # Numeric keypad 4 key
    'NUMPAD5'             : 0x65, # Numeric keypad 5 key
    'NUMPAD6'             : 0x66, # Numeric keypad 6 key
    'NUMPAD7'             : 0x67, # Numeric keypad 7 key
    'NUMPAD8'             : 0x68, # Numeric keypad 8 key
    'NUMPAD9'             : 0x69, # Numeric keypad 9 key
    'MULTIPLY'            : 0x6A, # Multiply key (*)
    'ADD'                 : 0x6B, # Add key (+)
    'SEPARATOR'           : 0x6C, # Separator key (.)
    'SUBTRACT'            : 0x6D, # Subtract key (-)
    'DECIMAL'             : 0x6E, # Decimal key (,)
    'DIVIDE'              : 0x6F, # Divide key (/)
    'F1'                  : 0x70, # F1 key
    'F2'                  : 0x71, # F2 key
    'F3'                  : 0x72, # F3 key
    'F4'                  : 0x73, # F4 key
    'F5'                  : 0x74, # F5 key
    'F6'                  : 0x75, # F6 key
    'F7'                  : 0x76, # F7 key
    'F8'                  : 0x77, # F8 key
    'F9'                  : 0x78, # F9 key
    'F10'                 : 0x79, # F10 key
    'F11'                 : 0x7A, # F11 key
    'F12'                 : 0x7B, # F12 key
    'F13'                 : 0x7C, # F13 key
    'F14'                 : 0x7D, # F14 key
    'F15'                 : 0x7E, # F15 key
    'F16'                 : 0x7F, # F16 key
    'F17'                 : 0x80, # F17 key
    'F18'                 : 0x81, # F18 key
    'F19'                 : 0x82, # F19 key
    'F20'                 : 0x83, # F20 key
    'F21'                 : 0x84, # F21 key
    'F22'                 : 0x85, # F22 key
    'F23'                 : 0x86, # F23 key
    'F24'                 : 0x87, # F24 key
    'NUMLOCK'             : 0x90, # NUM LOCK key
    'SCROLL'              : 0x91, # SCROLL LOCK key
    'LSHIFT'              : 0xA0, # Left SHIFT key
    'RSHIFT'              : 0xA1, # Right SHIFT key
    'LCONTROL'            : 0xA2, # Left CONTROL key
    'RCONTROL'            : 0xA3, # Right CONTROL key
    'LMENU'               : 0xA4, # Left MENU key
    'RMENU'               : 0xA5, # Right MENU key
    'BROWSER_BACK'        : 0xA6, # Browser Back key
    'BROWSER_FORWARD'     : 0xA7, # Browser Forward key
    'BROWSER_REFRESH'     : 0xA8, # Browser Refresh key
    'BROWSER_STOP'        : 0xA9, # Browser Stop key
    'BROWSER_SEARCH'      : 0xAA, # Browser Search key 
    'BROWSER_FAVORITES'   : 0xAB, # Browser Favorites key
    'BROWSER_HOME'        : 0xAC, # Browser Start and Home key
    'VOLUME_MUTE'         : 0xAD, # Volume Mute key
    'VOLUME_DOWN'         : 0xAE, # Volume Down key
    'VOLUME_UP'           : 0xAF, # Volume Up key
    'MEDIA_NEXT_TRACK'    : 0xB0, # Next Track key
    'MEDIA_PREV_TRACK'    : 0xB1, # Previous Track key
    'MEDIA_STOP'          : 0xB2, # Stop Media key
    'MEDIA_PLAY_PAUSE'    : 0xB3, # Play/Pause Media key
    'LAUNCH_MAIL'         : 0xB4, # Start Mail key
    'LAUNCH_MEDIA_SELECT' : 0xB5, # Select Media key
    'LAUNCH_APP1'         : 0xB6, # Start Application 1 key
    'LAUNCH_APP2'         : 0xB7, # Start Application 2 key
    'OEM_1'               : 0xBA, # Used for miscellaneous characters; it can vary by keyboard. For the US standard keyboard, the ';:' key 
    'OEM_PLUS'            : 0xBB, # For any country/region, the '+' key
    'OEM_COMMA'           : 0xBC, # For any country/region, the ',' key
    'OEM_MINUS'           : 0xBD, # For any country/region, the '-' key
    'OEM_PERIOD'          : 0xBE, # For any country/region, the '.' key
    'OEM_2'               : 0xBF, # Used for miscellaneous characters; it can vary by keyboard. For the US standard keyboard, the '/?' key 
    'OEM_3'               : 0xC0, # Used for miscellaneous characters; it can vary by keyboard. For the US standard keyboard, the '`~' key
    'OEM_4'               : 0xDB, # Used for miscellaneous characters; it can vary by keyboard. For the US standard keyboard, the '[{' key
    'OEM_5'               : 0xDC, # Used for miscellaneous characters; it can vary by keyboard. For the US standard keyboard, the '\|' key
    'OEM_6'               : 0xDD, # Used for miscellaneous characters; it can vary by keyboard. For the US standard keyboard, the ']}' key
    'OEM_7'               : 0xDE, # Used for miscellaneous characters; it can vary by keyboard. For the US standard keyboard, the 'single-quote/double-quote' key
    'OEM_8'               : 0xDF, # Used for miscellaneous characters; it can vary by keyboard.
    'OEM_102'             : 0xE2, # Either the angle bracket key or the backslash key on the RT 102-key keyboard
}

alias = {
    'CAPSLOCK'      : 'CAPITAL',
    'ESC'           : 'ESCAPE',
    'PAGE_UP'       : 'PRIOR',
    'PAGE_DOWN'     : 'NEXT',
    'PRINT_SCREEN'  : 'SNAPSHOT',
    'ALT'           : 'LMENU',
    'ALT_GR'        : 'RMENU',
    'ENTER'         : 'RETURN',
    '\n': 'RETURN',
    ' ' : 'SPACE',
    '*' : 'MULTIPLY',
    '/' : 'DIVIDE',
    'Ç' : 'OEM_1',
    '=' : 'OEM_PLUS',   # SHIFT +
    ',' : 'OEM_COMMA',  # SHIFT <
    '-' : 'OEM_MINUS',  # SHIFT _
    '.' : 'OEM_PERIOD', # SHIFT >
    ';' : 'OEM_2',      # SHIFT :
    '\'': 'OEM_3',      # SHIFT "
    '´' : 'OEM_4',      # SHIFT `
    ']' : 'OEM_5',      # SHIFT }
    '[' : 'OEM_6',      # SHIFT {
    '~' : 'OEM_7',      # SHIFT ^
    '\\': 'OEM_102',    # SHIFT |
    # SPECIALS
    '?' : ['ALT_GR', 'W'],
    '+' : ['LSHIFT', '='],
    '<' : ['LSHIFT', ','],
    '_' : ['LSHIFT', '-'],
    '>' : ['LSHIFT', '.'],
    ':' : ['LSHIFT', ';'],
    '"' : ['LSHIFT', '\''],
    '`' : ['LSHIFT', '´'],
    '}' : ['LSHIFT', ']'],
    '{' : ['LSHIFT', '['],
    '^' : ['LSHIFT', '~'],
    '|' : ['LSHIFT', '\\'],
    '!' : ['LSHIFT', '1'],
    '@' : ['LSHIFT', '2'],
    '#' : ['LSHIFT', '3'],
    '$' : ['LSHIFT', '4'],
    '%' : ['LSHIFT', '5'],
    '&' : ['LSHIFT', '7'],
    '(' : ['LSHIFT', '9'],
    ')' : ['LSHIFT', '0'],
    '¹' : ['ALT_GR', '1'],
    '²' : ['ALT_GR', '2'],
    '³' : ['ALT_GR', '3'],
    '£' : ['ALT_GR', '4'],
    '¢' : ['ALT_GR', '5'],
    '¬' : ['ALT_GR', '6'],
    '§' : ['ALT_GR', '='],
    'ª' : ['ALT_GR', '['],
    'º' : ['ALT_GR', ']'],
    '°' : ['ALT_GR', '/'],
    '☺' : {'function': 'altCode', 'value': 1},
    '☻' : {'function': 'altCode', 'value': 2},
    '♥' : {'function': 'altCode', 'value': 3},
    '♦' : {'function': 'altCode', 'value': 4},
    '♣' : {'function': 'altCode', 'value': 5},
    '♠' : {'function': 'altCode', 'value': 6},
    '•' : {'function': 'altCode', 'value': 7},
    '◘' : {'function': 'altCode', 'value': 8},
    '○' : {'function': 'altCode', 'value': 9},
    '◙' : {'function': 'altCode', 'value': 10},
    '♂' : {'function': 'altCode', 'value': 11},
    '♀' : {'function': 'altCode', 'value': 12},
    '♪' : {'function': 'altCode', 'value': 13},
    '♫' : {'function': 'altCode', 'value': 14},
    '☼' : {'function': 'altCode', 'value': 15},
    '►' : {'function': 'altCode', 'value': 16},
    '◄' : {'function': 'altCode', 'value': 17},
    '↕' : {'function': 'altCode', 'value': 18},
    '‼' : {'function': 'altCode', 'value': 19},
    '¶' : {'function': 'altCode', 'value': 20},
    '§' : {'function': 'altCode', 'value': 21},
    '▬' : {'function': 'altCode', 'value': 22},
    '↨' : {'function': 'altCode', 'value': 23},
    '↑' : {'function': 'altCode', 'value': 24},
    '↓' : {'function': 'altCode', 'value': 25},
    '→' : {'function': 'altCode', 'value': 26},
    '←' : {'function': 'altCode', 'value': 27},
    '∟' : {'function': 'altCode', 'value': 28},
    '↔' : {'function': 'altCode', 'value': 29},
    '▲' : {'function': 'altCode', 'value': 30},
    '▼' : {'function': 'altCode', 'value': 31},
    '`' : {'function': 'altCode', 'value': 96},
    '~' : {'function': 'altCode', 'value': 126},
    '⌂' : {'function': 'altCode', 'value': 127},
    'Ç' : {'function': 'altCode', 'value': 128},
    'ü' : {'function': 'altCode', 'value': 129},
    'é' : {'function': 'altCode', 'value': 130},
    'â' : {'function': 'altCode', 'value': 131},
    'ä' : {'function': 'altCode', 'value': 132},
    'à' : {'function': 'altCode', 'value': 133},
    'å' : {'function': 'altCode', 'value': 134},
    'ç' : {'function': 'altCode', 'value': 135},
    'ê' : {'function': 'altCode', 'value': 136},
    'ë' : {'function': 'altCode', 'value': 137},
    'è' : {'function': 'altCode', 'value': 138},
    'ï' : {'function': 'altCode', 'value': 139},
    'î' : {'function': 'altCode', 'value': 140},
    'ì' : {'function': 'altCode', 'value': 141},
    'Ä' : {'function': 'altCode', 'value': 142},
    'Å' : {'function': 'altCode', 'value': 143},
    'É' : {'function': 'altCode', 'value': 144},
    'æ' : {'function': 'altCode', 'value': 145},
    'Æ' : {'function': 'altCode', 'value': 146},
    'ô' : {'function': 'altCode', 'value': 147},
    'ö' : {'function': 'altCode', 'value': 148},
    'ò' : {'function': 'altCode', 'value': 149},
    'û' : {'function': 'altCode', 'value': 150},
    'ù' : {'function': 'altCode', 'value': 151},
    'ÿ' : {'function': 'altCode', 'value': 152},
    'Ö' : {'function': 'altCode', 'value': 153},
    'Ü' : {'function': 'altCode', 'value': 154},
    'ø' : {'function': 'altCode', 'value': 155},
    '£' : {'function': 'altCode', 'value': 156},
    'Ø' : {'function': 'altCode', 'value': 157},
    '×' : {'function': 'altCode', 'value': 158},
    'ƒ' : {'function': 'altCode', 'value': 159},
    'á' : {'function': 'altCode', 'value': 160},
    'í' : {'function': 'altCode', 'value': 161},
    'ó' : {'function': 'altCode', 'value': 162},
    'ú' : {'function': 'altCode', 'value': 163},
    'ñ' : {'function': 'altCode', 'value': 164},
    'Ñ' : {'function': 'altCode', 'value': 165},
    'ª' : {'function': 'altCode', 'value': 166},
    'º' : {'function': 'altCode', 'value': 167},
    '¿' : {'function': 'altCode', 'value': 168},
    '®' : {'function': 'altCode', 'value': 169},
    '¬' : {'function': 'altCode', 'value': 170},
    '½' : {'function': 'altCode', 'value': 171},
    '¼' : {'function': 'altCode', 'value': 172},
    '¡' : {'function': 'altCode', 'value': 173},
    '«' : {'function': 'altCode', 'value': 174},
    '»' : {'function': 'altCode', 'value': 175},
    '░' : {'function': 'altCode', 'value': 176},
    '▒' : {'function': 'altCode', 'value': 177},
    '▓' : {'function': 'altCode', 'value': 178},
    '│' : {'function': 'altCode', 'value': 179},
    '┤' : {'function': 'altCode', 'value': 180},
    'Á' : {'function': 'altCode', 'value': 181},
    'Â' : {'function': 'altCode', 'value': 182},
    'À' : {'function': 'altCode', 'value': 183},
    '©' : {'function': 'altCode', 'value': 184},
    '╣' : {'function': 'altCode', 'value': 185},
    '║' : {'function': 'altCode', 'value': 186},
    '╗' : {'function': 'altCode', 'value': 187},
    '╝' : {'function': 'altCode', 'value': 188},
    '¢' : {'function': 'altCode', 'value': 189},
    '¥' : {'function': 'altCode', 'value': 190},
    '┐' : {'function': 'altCode', 'value': 191},
    '└' : {'function': 'altCode', 'value': 192},
    '┴' : {'function': 'altCode', 'value': 193},
    '┬' : {'function': 'altCode', 'value': 194},
    '├' : {'function': 'altCode', 'value': 195},
    '─' : {'function': 'altCode', 'value': 196},
    '┼' : {'function': 'altCode', 'value': 197},
    'ã' : {'function': 'altCode', 'value': 198},
    'Ã' : {'function': 'altCode', 'value': 199},
    '╚' : {'function': 'altCode', 'value': 200},
    '╔' : {'function': 'altCode', 'value': 201},
    '╩' : {'function': 'altCode', 'value': 202},
    '╦' : {'function': 'altCode', 'value': 203},
    '╠' : {'function': 'altCode', 'value': 204},
    '═' : {'function': 'altCode', 'value': 205},
    '╬' : {'function': 'altCode', 'value': 206},
    '¤' : {'function': 'altCode', 'value': 207},
    'ð' : {'function': 'altCode', 'value': 208},
    'Ð' : {'function': 'altCode', 'value': 209},
    'Ê' : {'function': 'altCode', 'value': 210},
    'Ë' : {'function': 'altCode', 'value': 211},
    'È' : {'function': 'altCode', 'value': 212},
    'ı' : {'function': 'altCode', 'value': 213},
    'Í' : {'function': 'altCode', 'value': 214},
    'Î' : {'function': 'altCode', 'value': 215},
    'Ï' : {'function': 'altCode', 'value': 216},
    '┘' : {'function': 'altCode', 'value': 217},
    '┌' : {'function': 'altCode', 'value': 218},
    '█' : {'function': 'altCode', 'value': 219},
    '▄' : {'function': 'altCode', 'value': 220},
    '¦' : {'function': 'altCode', 'value': 221},
    'Ì' : {'function': 'altCode', 'value': 222},
    '▀' : {'function': 'altCode', 'value': 223},
    'Ó' : {'function': 'altCode', 'value': 224},
    'ß' : {'function': 'altCode', 'value': 225},
    'Ô' : {'function': 'altCode', 'value': 226},
    'Ò' : {'function': 'altCode', 'value': 227},
    'õ' : {'function': 'altCode', 'value': 228},
    'Õ' : {'function': 'altCode', 'value': 229},
    'µ' : {'function': 'altCode', 'value': 230},
    'þ' : {'function': 'altCode', 'value': 231},
    'Þ' : {'function': 'altCode', 'value': 232},
    'Ú' : {'function': 'altCode', 'value': 233},
    'Û' : {'function': 'altCode', 'value': 234},
    'Ù' : {'function': 'altCode', 'value': 235},
    'ý' : {'function': 'altCode', 'value': 236},
    'Ý' : {'function': 'altCode', 'value': 237},
    '¯' : {'function': 'altCode', 'value': 238},
    '´' : {'function': 'altCode', 'value': 239},
    '±' : {'function': 'altCode', 'value': 241},
    '‗' : {'function': 'altCode', 'value': 242},
    '¾' : {'function': 'altCode', 'value': 243},
    '¶' : {'function': 'altCode', 'value': 244},
    '§' : {'function': 'altCode', 'value': 245},
    '÷' : {'function': 'altCode', 'value': 246},
    '¸' : {'function': 'altCode', 'value': 247},
    '°' : {'function': 'altCode', 'value': 248},
    '¨' : {'function': 'altCode', 'value': 249},
    '·' : {'function': 'altCode', 'value': 250},
    '¹' : {'function': 'altCode', 'value': 251},
    '³' : {'function': 'altCode', 'value': 252},
    '²' : {'function': 'altCode', 'value': 253},
    '■' : {'function': 'altCode', 'value': 254},
}

quick = {
    '←' : 'BACK',
    '¶' : 'RETURN',
}
