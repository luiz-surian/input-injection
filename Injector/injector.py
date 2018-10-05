__author__ = 'Luiz Fernando Surian Filho'

import time
import re

try:
    from Injector import controller_mouse, \
                         controller_keyboard, controller_keybinds
except ImportError:
    import controller_mouse
    import controller_keyboard
    import controller_keybinds


wait = time.sleep

# Mouse Functions


def move(x=0, y=0):
    controller_mouse.set_pos(x, y)


def click():
    controller_mouse.click()


def mouse(x=0, y=0, t=0.2):
    move(x, y)
    click()
    wait(t)


# Keyboard Functions

_quick_enabled = False


def _get_key(key):
    _alias = dict(controller_keybinds.ALIAS)
    if _quick_enabled:
        _alias.update(controller_keybinds.QUICK)

    try:
        return controller_keybinds.VK[key]
    except KeyError:
        bind = _alias[key]
        try:
            return controller_keybinds.VK[bind]
        except TypeError:
            if type(bind) is dict:
                if bind['function'] == 'alt_code':
                    alt_code(bind['value'])
                else:
                    print('undefined')
            else:
                combination(bind)
            return False


def press(keys=[]):
    for k in keys:
        key = _get_key(k)
        controller_keyboard.press_key(key)
        controller_keyboard.release_key(key)


def combination(keys=[]):
    for k in keys:
        controller_keyboard.press_key(_get_key(k))
    for k in keys:
        controller_keyboard.release_key(_get_key(k))


def ez_type(string, quick=False):
    global _quick_enabled
    _quick_enabled = quick

    for letter in string:
        if re.match("^[A-Z]*$", letter):
            combination(['LSHIFT', letter])
        elif re.match("^[a-z]*$", letter):
            press([letter.upper()])
        else:
            press([letter])

    _quick_enabled = False


def alt_code(number):
    controller_keyboard.press_key(_get_key('ALT'))
    keys = []
    for k in str(number):
        keys.append(f'NUMPAD{k}')
    press(keys)
    controller_keyboard.release_key(_get_key('ALT'))
