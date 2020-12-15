import tkinter
from PIL import Image
from tkinter import simpledialog

window = tkinter.Tk()
window.geometry("200x100")
window.title("Png to Icon converter")
window.iconbitmap('pyqt.ico')

text ="""
PNG TO ICON CONVERTER    
"""

def dialogin():
    inpath = simpledialog.askstring("Converter", "Enter .png file path:")
    return inpath



def dialogout():
    outpath = simpledialog.askstring("Converter", "Enter output Name:")
    return outpath

def finaloutput(Outputstring, color="#04B404"):
    Ueberschrift = tkinter.Label(window, text=text)
    Ueberschrift.pack()
    Stringout = tkinter.Label(window, text=Outputstring, fg=color)
    Stringout.pack()
    label2 = tkinter.Label(window, text="by Lukas Z")
    label2.pack()






def convert(output):
    try:
        img.save(str(output) + ".ico",format = 'ICO', sizes=[(32,32)])
    except:
        print("output compyling error")

inpath = dialogin()
outpath = dialogout()

try:

    img = Image.open(inpath)
    convert(outpath)
    finaloutput("Process successfully finished")
except:
    finaloutput("Process failed, File does not exist", color="#DF0101")

window.mainloop()

