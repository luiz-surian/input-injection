import re
import time
import keybinds
import keyb_control
import mouse_control

__author__ = 'Luiz Fernando Surian Filho'
wait = time.sleep

# MOUSE -------------------------------------------------- #

def move(x=0, y=0):
    mouse_control.setPos(x, y)

def click():
    mouse_control.Click()

def mouse(x=0, y=0, t=0.2):
    move(x, y)
    click()
    wait(t)

# KEYBOARD -------------------------------------------------- #

_quickEnabled = False

def _getKey(key):
    _alias = dict(keybinds.alias)
    if _quickEnabled:
        _alias.update(keybinds.quick)
    
    try:
        return keybinds.VK[key]
    except:
        bind = _alias[key]
        try:
            return keybinds.VK[bind]
        except:
            if type(bind) is dict:
                if bind['function'] == 'altCode':
                    altCode(bind['value'])
                else:
                    print('undefined')
            else:
                combination(bind)
            return False

def press(keys=[]):
    for k in keys:
        key = _getKey(k)
        keyb_control.PressKey(key)
        keyb_control.ReleaseKey(key)

def combination(keys=[]):
    for k in keys:
        keyb_control.PressKey(_getKey(k))
    for k in keys:
        keyb_control.ReleaseKey(_getKey(k))

def ezType(string, quick=False):
    global _quickEnabled
    _quickEnabled = quick

    for letter in string:
        if re.match("^[A-Z]*$", letter):
            combination(['LSHIFT', letter])
        elif re.match("^[a-z]*$", letter):
            press([letter.upper()])
        else:
            press([letter])

    _quickEnabled = False

def altCode(number):
    keyb_control.PressKey(_getKey('ALT'))
    keys = []
    for k in str(number):
        keys.append(f'NUMPAD{k}')
    press(keys)
    keyb_control.ReleaseKey(_getKey('ALT'))

class Shortkey:
    def __init__(self, keys=[]):
        self.keys = keys
    def __call__(self):
        return combination(self.keys)

enter = Shortkey(['ENTER'])
exec_ = Shortkey(['LWIN', 'R'])
close = Shortkey(['ALT', 'F4'])
