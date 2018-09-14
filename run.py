from __init__ import *

def helloWorld():
    combination(["LWIN", "R"])
    wait(0.2)
    press(["C", "M", "D", "RETURN"])
    wait(0.2)
    press(["I", "P", "C", "O", "N", "F", "I", "G", "RETURN"])

def primitive():
    combination(["LWIN", "3"]) # Abrir Outlook
    wait(0.2)
    move(x=20, y=78) # Novo Email
    click()
    press(["A", "G", "A", "T", "A", "N", "G", "E", "L", "O", "TAB"])
    wait(0.2)
    move(x=148, y=270) # Assunto
    click()
    press(["P", "A", "R", "A", "SPACE", "C", "O", "N", "H", "E", "C", "I", "M", "E", "N", "T", "O"])
    wait(0.2)
    move(x=25,  y=306) # Corpo
    click()
    press(["B", "O", "A", "SPACE", "T", "A", "R", "D", "E", "OEM_COMMA", "RETURN"])
    press(["S", "E", "G", "U", "E", "SPACE", "I", "N", "F", "O", "R", "M", "A", "OEM_1", "OEM_8", "O", "E", "S", "SPACE", "S", "I", "G", "I", "L", "O", "S", "A", "S"])

def writeTest():
    exec_()
    wait(0.2)
    ezType('notepad¶', True)
    wait(0.4)
    ezType('''Testing application...
abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*()_+-={}[]^?~/,.;<>:\|\'"
☺☻♥♦♣♠•◘○◙♂♀♪♫☼►◄↕‼¶▬↨↑↓→←∟↔▲▼⌂üéâäàåçêëèïîìÄÅÉæÆôöòûùÿÖÜøØ×ƒáíóúñÑ¿®½¼¡«»░▒▓│┤ÁÂÀ©╣║╗╝¥┐└┴┬├─┼ãÃ╚╔╩╦╠═╬¤ðÐÊËÈıÍÎÏ┘┌█▄¦Ì▀ÓßÔÒõÕµþÞÚÛÙýÝ¯±‗¾÷¸¨·■


''')
    wait(5)
    ezType('Closing application in... 3')
    wait(1)
    ezType('←2', True)
    wait(1)
    ezType('←1', True)
    wait(1)
    close()
    press(['N'])

def quickTest():
    exec_()
    wait(0.2)
    ezType('notepad¶', True)
    wait(0.4)

    ezType('abc←¶')
    enter()
    
    ezType('abc←¶', True)
    
    ezType('abc←¶')
    enter()
    
    ezType('abc←¶', True)
    
    ezType('abc←¶')
    enter()

def pressEverything():
    exec_()
    wait(0.2)
    ezType('notepad¶', True)
    wait(0.4)
    from keybinds import alias
    press([k for k in alias])

def sendMail(to='Luiz Fernando Surian Filho'):
    combination(['LWIN', '3']) # Abrir Outlook
    wait(0.2)
    
    mouse(x=20, y=994) # Menu Email

    mouse(x=20, y=78) # Novo Email
    ezType(to)

    mouse(x=148, y=270) # Assunto
    ezType('Isto é um teste!')
    
    mouse(x=25,  y=306) # Corpo

    ezType('''Boa tarde,
Se você consegue ler isto, parabéns! Significa que você não é cego.''')
    
    move(x=40,  y=194) # Enviar
    #click()

def annimation():
    def init():
        exec_()
        wait(0.2)
        ezType('notepad¶', True)
        wait(0.4)

    def clear():
        wait(0.6)
        combination(['LCONTROL', 'A'])
        press(['BACK'])

    def frame1():
        ezType('''Polichinelo!
 o
/|\\
 ║

''')

    def frame2(): 
        ezType('''Polichinelo!
\\o/
 |
/ \\

''')
        
    init()
    for _ in range(6):
        frame1()
        clear()
        frame2()
        clear()
    close()
    press(['N'])
              
    
if __name__ == '__main__':
    sendMail()
