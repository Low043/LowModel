import customtkinter as ctk
from PIL import Image as PilImage

class Menu(ctk.CTk):
    def __init__(self,title:str,geometry:str,icon=None,resizable=False):
        super().__init__()
        self.title(title)
        self.geometry(geometry)
        self.resizable(resizable,resizable)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.windows = []

        self.bind_all("<Button-1>", lambda event: event.widget.focus_set())#Click outside close Entry
        if icon:
            self.iconbitmap(icon)
    
    def addWindow(self,window):
        self.windows.append(window)
        window.grid(row=0,column=0,sticky='nsew')
        self.changeToWindow(0)

    def changeToWindow(self,index):
        self.windows[index].tkraise()

class Window(ctk.CTkFrame):
    def __init__(self,menu,columns,rows):
        super().__init__(menu,corner_radius=0)
        self.grid_columnconfigure(list(range(columns)),weight=1,uniform='fred')
        self.grid_rowconfigure(list(range(rows)),weight=1,uniform='fred')

    def addElement(self,element,x=0,y=0,spanx=1,spany=1,padx=0,pady=0,expandTo='nsew'):
        element.grid(column=x,row=y,padx=padx,pady=pady,columnspan=spanx,rowspan=spany,sticky=expandTo)

class Button(ctk.CTkButton):
    def __init__(self,window,text='Button',func=None,width=140,height=28,corner=7,color='#1e539e',textColor='white',hoverColor='#133666',borderColor='black',hover=True,border=0,image=None):
        var = None if type(text) != ctk.StringVar else text
        super().__init__(window,width,height,corner,border,2,'transparent',color,hoverColor,borderColor,textColor,None,None,True,True,text,None,var,image,'normal',hover,func)

class Input(ctk.CTkEntry):
    def __init__(self,window,placeHolder=None,password=False,width=140,height=28,corner=7,color='#343638',textColor='white',borderColor='#565b5e',border=2,justify='center',limitChar=13):
        self.limitChar = limitChar
        show = '●' if password == True else ''
        super().__init__(window,width,height,corner,border,'transparent',color,borderColor,textColor,'#808587',None,placeHolder,justify=justify,show=show)
        self.configure(validate='key',validatecommand=(window.register(self.validate),'%P'))

    def changeViewPassword(self):
        if self.cget('show') == '●':
            self.configure(show='')
        else:
            self.configure(show='●')

    def validate(self,currentEntry):
        return len(currentEntry) < self.limitChar

class CheckBox(ctk.CTkCheckBox):
    def __init__(self,window,text='',size=24,width=0,height=0,corner=6,border=3,color='#1e539e',textColor='white',hoverColor='#343638',borderColor='#565b5e',clickFunc=None):
        super().__init__(window,width,height,size,size,corner,border,'transparent',color,hoverColor,borderColor,None,textColor,None,text,command=clickFunc)

class Image(ctk.CTkImage):
    def __init__(self,src:str,size=(20,20)):
        image = PilImage.open(src)
        super().__init__(image,image,size)

class Container(ctk.CTkLabel):
    def __init__(self,window,width=0,height=28,corner=0,color='transparent',textColor='white',text='',image=None):
        super().__init__(window,width,height,corner,'transparent',color,textColor,None,text,None,image)

class ViewPassButton(Button):
    def __init__(self,window,passwordInput:Input,images:tuple[Image]):
        super().__init__(window,'',self.changeView,0,0,0,'transparent',hover=False,image=images[0])
        self.passwordInput = passwordInput
        self.images = images
        self.img = 1

    def changeView(self):
        self.passwordInput.changeViewPassword()
        self.configure(image=self.images[self.img])
        self.img = 1 - self.img

