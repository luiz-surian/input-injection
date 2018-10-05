import ctypes


# see http://msdn.microsoft.com/en-us/library/ms646260(VS.85).aspx for details
user32 = ctypes.windll.user32


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


if __name__ == "__main__":
    print(get_pos())
