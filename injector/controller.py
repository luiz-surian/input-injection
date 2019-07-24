#!/usr/bin/python
# -*- coding: utf-8 -*-

import ctypes
from ctypes import wintypes

user32 = ctypes.windll.user32

INPUT_MOUSE = 0
INPUT_KEYBOARD = 1
INPUT_HARDWARE = 2
KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP = 0x0002
KEYEVENTF_UNICODE = 0x0004
KEYEVENTF_SCANCODE = 0x0008
MAPVK_VK_TO_VSC = 0
ULONG_PTR = wintypes.WPARAM


class MouseInput(ctypes.Structure):
    _fields_ = (
        ("dx", wintypes.LONG),
        ("dy", wintypes.LONG),
        ("mouseData", wintypes.DWORD),
        ("dwFlags", wintypes.DWORD),
        ("time", wintypes.DWORD),
        ("dwExtraInfo", ULONG_PTR),
    )


class KeyboardInput(ctypes.Structure):
    _fields_ = (
        ("wVk", wintypes.WORD),
        ("wScan", wintypes.WORD),
        ("dwFlags", wintypes.DWORD),
        ("time", wintypes.DWORD),
        ("dwExtraInfo", ULONG_PTR),
    )

    def __init__(self, *args, **kwargs):
        super(KeyboardInput, self).__init__(*args, **kwargs)
        # Alguns programas usam o "Scan Code" mesmo se o parâmetro "KEYEVENTF_SCANCODE"
        # não estiver definido em "dwFflags", então tenta mapear o código correto.
        if not self.dwFlags & KEYEVENTF_UNICODE:
            self.wScan = user32.MapVirtualKeyExW(self.wVk, MAPVK_VK_TO_VSC, 0)


class HardwareInput(ctypes.Structure):
    _fields_ = (
        ("uMsg", wintypes.DWORD),
        ("wParamL", wintypes.WORD),
        ("wParamH", wintypes.WORD),
    )


class INPUT(ctypes.Structure):
    class _INPUT(ctypes.Union):
        _fields_ = (
            ("ki", KeyboardInput),
            ("mi", MouseInput),
            ("hi", HardwareInput)
        )
    _anonymous_ = ("_input",)
    _fields_ = (
        ("type", wintypes.DWORD),
        ("_input", _INPUT)
    )


def _check_count(result, func, args):
    if result == 0:
        raise ctypes.WinError(ctypes.get_last_error())
    return args


user32.SendInput.errcheck = _check_count
user32.SendInput.argtypes = (
    wintypes.UINT,  # nInputs
    ctypes.POINTER(INPUT),  # pInputs
    ctypes.c_int  # cbSize
)


def press_key(hex_key_code):
    x = INPUT(
        type=INPUT_KEYBOARD,
        ki=KeyboardInput(wVk=hex_key_code)
    )
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))


def release_key(hex_key_code):
    x = INPUT(
        type=INPUT_KEYBOARD,
        ki=KeyboardInput(wVk=hex_key_code, dwFlags=KEYEVENTF_KEYUP)
    )
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))


def get_caps_lock_state():
    return user32.GetKeyState(0x14)


# Mouse Input
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]


def get_pos():
    pt = POINT()
    user32.GetCursorPos(ctypes.byref(pt))
    return f'mouse(x={pt.x}, y={pt.y})'


def set_pos(x, y):
    user32.SetCursorPos(x, y)


def click():
    user32.mouse_event(2, 0, 0, 0, 0)  # left down
    user32.mouse_event(4, 0, 0, 0, 0)  # left up


if __name__ == '__main__':
    print(get_pos())

