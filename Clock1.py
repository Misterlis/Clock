from ast import Return
import tkinter as tk
from cProfile import label
from cgitb import text
from cmath import e
from logging import root
from msilib.schema import Font
from tkinter import *
from tkinter.font import BOLD
from webbrowser import BackgroundBrowser, get
import tkinter as tk
from tkinter.font import Font
from tkinter import *
import tkinter


def convert():
    h = int(T.get())
    m = int(T1.get())



    x = abs((h % 12 * 30 - m * 5.5))
    x = min(x, 360-x)
    #x = float(abs(11 /2 * m - 30 * h))
    #x = (h * 30 + m * 0.5) - (m * 6)
    cnv['text'] = x

root = Tk()
root.title('Угол между часовой и минутной стрелками часов')
root.resizable(width=False, height=False)
root.geometry('800x500')
root["bg"] = "aqua"

V1 = Label(root, text='Введите часы:', font= 'Courier 13', fg='black', bg='aqua')
V1.pack(pady=10)
T = Entry(root, font= 'Courier 15' )
T.pack(pady=10)

V2 = Label(root, text='Введите минуты:', font= 'Courier 13', fg='black', bg='aqua')
V2.pack(pady=10)

T1 = Entry(root, font= 'Courier 15' )
T1.pack(pady=10)

btn = Button(root, text='Рассчитать угол', font= 'Courier 13', padx=5, pady=5, command=convert)
btn.pack(pady=10)

cnv = Label(root, text=' ', font= 'Courier 13', fg='black', bg='aqua')
cnv.pack()

root.mainloop()