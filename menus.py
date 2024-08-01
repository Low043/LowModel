from utils import Pointer, centerText, colored, os
from pynput.keyboard import Key, Listener
import win32gui

CURRENT_CONSOLE = win32gui.GetForegroundWindow()#Program Application Console

class MenuOption:
    def __init__(self,text:str):
        '''Create MenuOption. Set with addEnterFunction()/addTypeableVar()'''
        self.text = text
        self.enterFunction = None
        self.typeableVar : Pointer = None

    def interact(self,key):
        '''Uses Key passed by Menu to do something'''
        if key == Key.enter and self.enterFunction:
            self.enterFunction()
        if type(key) == str and self.typeableVar:
            self.typeableVar.add(key)

    def addEnterFunction(self,func):
        '''Append Function to do when press Enter'''
        self.enterFunction = func

    def addTypeableVar(self,pointer:Pointer):
        '''Synchronize values with Pointer'''
        self.typeableVar = pointer

    def __str__(self):
        return self.text

class Menu:
    def __init__(self,title:str,subtitle=''):
        '''Create Menu. Use addOption() and start() to init'''
        self.title = title
        self.subtitle = subtitle
        self.options : list[MenuOption] = []
        self.keyCloseMenu = Key.esc
        self.optionSelected = 0

    def start(self):
        '''Enters in Main Menu Loop (Start Keyboard Listener to Interactions)'''
        self.show()
        with Listener(on_press=self.interact) as listener:
            listener.join()

    def interact(self,key):
        '''Get key press and do something (Unless console is not Focused Window)'''
        if self.windowOnFocus():
            self.navigate(key)
            self.options[self.optionSelected].interact(key)
            self.show()
            if key == self.keyCloseMenu:
                return False

    def navigate(self,key):
        '''Up or Down Option Selected based on Key Pressed'''
        self.optionSelected += (key == Key.down) - (key == Key.up)
        self.optionSelected = self.optionSelected % len(self.options)#Restricts OptionSelected to RangeOptions

    def addOption(self,option:MenuOption):
        '''Appends MenuOption to OptionList'''
        self.options.append(option)

    def show(self):
        '''Show Menu Interface'''
        os.system('cls')
        print(centerText(self.title))
        print(centerText(self.subtitle))
        
        for optionIndex,option in enumerate(self.options):
            print(f' >' if optionIndex == self.optionSelected else '  ',option)

    def windowOnFocus(self):
        '''Returns if Console is On Focus (And block interactions to None Options Menu)'''
        return win32gui.GetForegroundWindow() == CURRENT_CONSOLE and self.options != []
    
menu = Menu(f'aaa {colored("bbb","red",attrs=["blink","underline"])} ccc')
menu.addOption(MenuOption('aaa'))
menu.addOption(MenuOption('bbb'))
menu.addOption(MenuOption('ccc'))
menu.start()