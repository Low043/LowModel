import customtkinter as ctk

class Button(ctk.CTkButton):
    def __init__(self,master,text,func,color,column,row,padx,pady,columnSpan,rowSpan,anchor):
        super().__init__(master,text=text,command=func,fg_color=color)
        self.grid(column=column,row=row,padx=padx,pady=pady,columnspan=columnSpan,rowspan=rowSpan,sticky=anchor)

class Frame(ctk.CTkFrame):
    def __init__(self,master,color,column,row,padx,pady,columnSpan,rowSpan,anchor):
        super().__init__(master,fg_color=color)
        self.grid(column=column,row=row,padx=padx,pady=pady,columnspan=columnSpan,rowspan=rowSpan,sticky=anchor)

class App(ctk.CTk):
    def __init__(self,title:str,size:str='400x400',gridHeight=9,gridWidth=9):
        super().__init__()
        self.title(title)
        self.geometry(size)
        self.grid_columnconfigure(tuple(range(gridWidth)), weight=1,uniform='fred')
        self.grid_rowconfigure(tuple(range(gridHeight)), weight=1,uniform='fred')
    
    def addFrame(self,color:str=None,column=0,row=0,padx=0,pady=0,columnSpan=1,rowSpan=1,anchor='nsew'):
        return Frame(self,color,column,row,padx,pady,columnSpan,rowSpan,anchor)
    
    def addButton(self,text='Button',func=lambda:None,color:str=None,column=0,row=0,padx=0,pady=0,columnSpan=1,rowSpan=1,anchor='nsew'):
        return Button(self,text,func,color,column,row,padx,pady,columnSpan,rowSpan,anchor)
    
    def viewGrid(self):
        for i in range(9):
            for j in range(9):
                self.addButton(column=i,row=j,text=f'{i}{j}',padx=1,pady=1)

app = App('Teste')
app.addFrame(column=1,row=1,columnSpan=7,rowSpan=4)
app.addButton(column=3,row=6,columnSpan=3)
app.mainloop()