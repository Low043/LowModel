import os, re
from termcolor import colored
from unidecode import unidecode
from difflib import SequenceMatcher

def centerText(text:str,fillChar:chr=' '):
    '''Center text on terminal (Accept Font Effects)'''
    uncoloredText = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]').sub('',text)
    centeredText = uncoloredText.center(os.get_terminal_size()[0],fillChar)
    currentChar = centeredText.find(uncoloredText)#Begin of text in centered text
    for char in text:
        if char != centeredText[currentChar]:#add chars not found to centered text
            centeredText = centeredText[:currentChar] + char + centeredText[currentChar:]
        currentChar += 1
    return centeredText

def simplifyText(text:str):
    '''Remove Accents and Upper Chars'''
    return unidecode(text.lower())

def textSimilarity(text1:str,text2:str):
    '''Returns decimal value to percentage of similarity between two strings'''
    return SequenceMatcher(None, text1, text2).ratio()

def numToMonth(num,upper=True):
    '''Converts Number to Portuguese Months'''
    months = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
    if int(num) >= 1 and int(num) <= 12:
        return months[int(num)-1].upper() if upper else months[int(num)-1]

def numToMoney(num):
    text = f'{num:.2f}'.replace('.','')
    if len(text) >= 3:
        text = text[:-2] + ',' + text[-2:]

    for i in range(100):
        if len(text) > 6+4*i:
            text = text[:-6-4*i] + '.' + text[-6-4*i:]
        else:
            break

    return 'R$ ' + text

def moneyToNum(text):
    text = text.replace('R$ ','')
    if text[-3:] == ',00':
        text = text[:-3]
    return float(text.replace(',','.').replace('.',''))

class Pointer:
    #Ponteiros são espécies de "locais na memória compartilhados"
    #No momento que um ponteiro recebe outro ponteiro como valor eles são conectados
    #Uma vez conectados os ponteiros compartilham sempre o mesmo valor, alterar um resulta na alteração do outro

    def __init__(self,value=None):#Transforma um valor em um ponteiror
        self.list = [value]

    def get(self):#Retorna o valor do ponteiro
        if type(self.list[0]) == Pointer:
            return self.list[0].get()
        return self.list[0]
    
    def set(self,value):#Edita o valor do ponteiro
        if type(self.list[0]) == Pointer:
            self.list[0].set(value)
        else:
            self.list = [value]
    
    def add(self,value):#Adiciona ao valor atual do ponteiro um novo valor (pode somar strings numéricas)
        if type(self.get()) == str and self.get().isnumeric():
            self.set(str(int(self.get())+value))
            return 0
        self.set(self.get()+value)

    def append(self,value):#Caso o ponteiro aponte para uma lista, insere um novo elemento na última posição
        if type(self.get()) == list:
            oldList = self.get()
            oldList.append(value)
            self.set(oldList)

    def insert(self,index,value):#Caso o ponteiro aponte para uma lista, insere um novo elemento na posição index
        if type(self.get()) == list:
            oldList = self.get()
            if index == -1:
                oldList.append(value)
            else:
                oldList.insert(index,value)
            self.set(oldList)

    def remove(self,value):#Caso o ponteiro aponte para uma lista, remove um elemento por seu valor
        if type(self.get()) == list:
            oldList = self.get()
            oldList.remove(value)
            self.set(oldList)

    def pop(self,index=-1):#Caso o ponteiro aponte para uma lista, remove um elemento pela sua posição
        if type(self.get()) == list:
            oldList = self.get()
            oldList.pop(index)
            self.set(oldList)

    def sort(self,reverse=False,key=None):#Caso o ponteiro aponte para uma lista, organiza
        #Uma key é uma função que recebe um valor e retorna um valor numérico, a lista será organizada com base neste valor
        if type(self.get()) == list:
            oldList = self.get()
            oldList.sort(reverse,key)
            self.set(oldList)

    def __str__(self):#Permite que ponteiros sejam tratados como string
        return str(self.get())
