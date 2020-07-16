from tkinter import *
from tkinter import filedialog as fd


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def insertText(self, txt):
        file = fd.askopenfilename(initialdir="/")
        f = open(file)
        s = f.read()
        txt.delete(1.0, END)
        txt.insert(END, s)
        f.close()

    def initUI(self):
        self.parent.title("Review")
        self.pack(fill=BOTH, expand=True)

        frame1 = Frame(self)
        frame1.pack(fill=BOTH, expand=True)

        btn1 = Button(frame1, text="Add", width=6)
        btn1.pack(side=RIGHT, anchor=N, padx=5, pady=5)

        txt = Text(frame1)
        txt.pack(fill=BOTH, pady=5, padx=5, expand=True)

        btn1.bind('<Button-1>', lambda event, t=txt: self.insertText(t))


root = Tk()
root.geometry("600x400+300+300")
app = Example(root)
root.mainloop()
