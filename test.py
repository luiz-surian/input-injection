__author__ = 'Luiz Fernando Surian Filho'

from Injector import injector


def hello_world():
    injector.combination(["LWIN", "R"])
    injector.wait(0.2)
    injector.press(["C", "M", "D", "RETURN"])
    injector.wait(0.2)
    injector.press(["I", "P", "C", "O", "N", "F", "I", "G", "RETURN"])


def write_test():
    injector.combination(['LWIN', 'R'])
    injector.wait(0.2)
    injector.ez_type('notepad¶', True)
    injector.wait(0.4)
    injector.ez_type('''Testing application...
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
0123456789
!@#$%&*()_+-={}[]<>¨^~/\|\'",.;:?
àáãâäåèéêëìíîïòóõôöùúûüçñýÿ
ÀÁÃÂÄÅÈÉÊËÌÍÎÏÒÓÕÔÖÙÚÛÜÇÑÝ
æÆøØ¤ÐðßµþÞ×ƒ¶¥®©½¼¾¹²³¿‼ı¡±÷
☺☻♥♦♣♠•◘○◙♂♀♪♫☼►◄↕↨↑↓→←∟↔▲▼⌂«»¦¸·
░▒▓│┤╣║╗╝┐└┴┬┘┌├─┼¯‗╚╔╩╦╠═╬█▄▀■▬


''')
    injector.wait(5)
    injector.ez_type('Closing application in... 3')
    injector.wait(1)
    injector.ez_type('←2', True)
    injector.wait(1)
    injector.ez_type('←1', True)
    injector.wait(1)
    injector.combination(['ALT', 'F4'])
    injector.press(['N'])


def quick_test():
    injector.combination(['LWIN', 'R'])
    injector.wait(0.2)
    injector.ez_type('notepad¶', True)
    injector.wait(0.4)

    injector.ez_type('abc←¶')
    injector.press(['ENTER'])

    injector.ez_type('abc←¶', True)

    injector.ez_type('abc←¶')
    injector.press(['ENTER'])

    injector.ez_type('abc←¶', True)

    injector.ez_type('abc←¶')
    injector.press(['ENTER'])


def press_everything():
    injector.combination(['LWIN', 'R'])
    injector.wait(0.2)
    injector.ez_type('notepad¶', True)
    injector.wait(0.4)
    from Injector import controller_keybinds
    injector.press([k for k in controller_keybinds.ALIAS])


def send_mail(to=__author__):
    injector.combination(['LWIN', '3'])  # Abrir Outlook
    injector.wait(0.2)

    injector.mouse(x=20, y=994)  # Menu Email

    injector.mouse(x=20, y=78)  # Novo Email
    injector.ez_type(to)

    injector.mouse(x=148, y=270)  # Assunto
    injector.ez_type('Isto é um teste!')

    injector.mouse(x=25,  y=306)  # Corpo

    injector.ez_type('''Boa tarde,
Se você consegue ler isto, parabéns! Significa que você não é cego.''')

    injector.move(x=40,  y=194)  # Enviar
    # injector.click()


def animation():
    def init():
        injector.combination(['LWIN', 'R'])
        injector.wait(0.2)
        injector.ez_type('notepad¶', True)
        injector.wait(0.4)

    def clear():
        injector.wait(0.6)
        injector.combination(['LCONTROL', 'A'])
        injector.press(['BACK'])

    def close():
        injector.combination(['ALT', 'F4'])
        injector.press(['N'])

    def frame1():
        injector.ez_type('''Polichinelo!
 o
/|\\
 ║

''')

    def frame2():
        injector.ez_type('''Polichinelo!
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


def loadbar():
    bar = '__________'
    output = f'{bar} 0%'
    
    injector.combination(['LWIN', 'R'])
    injector.wait(0.2)
    
    injector.ez_type('notepad¶', True)
    injector.wait(0.4)
    
    injector.ez_type('Please wait a moment...¶', True)
    injector.ez_type(output)
    injector.wait(0.8)
    
    for i in range(10):
        for _ in range(len(output)):
            injector.press(['BACK'])
        bar = bar.replace('_', '█', 1)
        output = f'{bar} {(i+1)*10}%'
        injector.ez_type(output)
        injector.wait(0.8)
    injector.ez_type('¶Thanks for waiting!', True)


if __name__ == '__main__':
    # hello_world()
    write_test()
    # quick_test()
    # press_everything()
    # send_mail()
    # animation()
    # loadbar()
