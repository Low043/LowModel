import os, re
from termcolor import colored
from unidecode import unidecode
from difflib import SequenceMatcher

def center(text:str,fillChar=' '):
    '''Center text on terminal (Accept Font Effects)'''
    uncoloredText = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]').sub('',text)#Remove text colors and attrs
    centeredText = uncoloredText.center(os.get_terminal_size()[0],fillChar)#Center uncolored text
    currentChar = centeredText.find(uncoloredText)#Begin of text in centered text
    for char in text:
        if char != centeredText[currentChar]:#add removed chars (colors and attrs) to centered text
            centeredText = centeredText[:currentChar] + char + centeredText[currentChar:]
        currentChar += 1
    return centeredText

def simplifyText(text:str):
    '''Lower text and remove accents'''
    return unidecode(text.lower())

def numToMonth(num,upper=True):
    '''Returns BR months by Num'''
    months = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
    num = int(num) - 1
    if num >= 0 and num < len(months):
        return months[num].upper() if upper else months[num]

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

def textSimilarity(text1:str,text2:str):
    '''Returns similarity percentage between two strings'''
    return SequenceMatcher(None, text1, text2).ratio()