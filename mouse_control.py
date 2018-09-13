import ctypes

user32 = ctypes.windll.user32

GetCursorPos = user32.GetCursorPos
SetCursorPos = user32.SetCursorPos

# see http://msdn.microsoft.com/en-us/library/ms646260(VS.85).aspx for details
mouse_event = user32.mouse_event

# Get screen resolution
maxWidth = user32.GetSystemMetrics(0)
maxHeight = user32.GetSystemMetrics(1)

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]

def getPos():
    pt = POINT()
    user32.GetCursorPos(ctypes.byref(pt))
    return {"x": pt.x, "y": pt.y}

def setPos(x, y):
    SetCursorPos(x, y)

def Click():
    mouse_event(2, 0, 0, 0, 0) # left down
    mouse_event(4, 0, 0, 0, 0) # left up
    

if __name__ == "__main__":
    print(getPos())
