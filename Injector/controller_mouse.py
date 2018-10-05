import ctypes


user32 = ctypes.windll.user32

get_cursor_pos = user32.GetCursorPos
set_cursor_pos = user32.SetCursorPos

# see http://msdn.microsoft.com/en-us/library/ms646260(VS.85).aspx for details
mouse_event = user32.mouse_event


class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]


def get_pos():
    pt = POINT()
    get_cursor_pos(ctypes.byref(pt))
    return f'mouse(x={pt.x}, y={pt.y})'


def set_pos(x, y):
    set_cursor_pos(x, y)


def click():
    mouse_event(2, 0, 0, 0, 0)  # left down
    mouse_event(4, 0, 0, 0, 0)  # left up


if __name__ == "__main__":
    print(get_pos())
