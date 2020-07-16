import models
from tkinter import *
from tkinter import filedialog as fd


class App(Frame):
    def __init__(self, parent, col):
        Frame.__init__(self, parent)
        self.parent = parent
        self.col = col
        self.initUI()

    def addFile(self, event, txt):
        file = fd.askopenfilename(initialdir="/")
        s = str(file)
        l = s.rfind('/')
        r = s.rfind('.')
        name = s[l + 1:r]
        self.col.add(models.Video(name, path=file))
        self.listUpdate(txt)

    def runFromList(self, event, txt):
        print('Running file...')
        index = txt.curselection()[0]
        vid = self.col.getFromList(index)
        vid.seen = True
        vid.run()
        self.listUpdate(txt)


    def initUI(self):
        self.parent.title("Review")
        self.pack(fill=BOTH, expand=True)

        frame1 = Frame(self, width=100)
        frame1.pack(fill=Y, side=RIGHT)

        btn1 = Button(frame1, text="Add", width=6)
        btn1.pack(side=TOP, anchor=N, padx=5, pady=5)

        btn2 = Button(frame1, text="Run", width=6)
        btn2.pack(side=TOP, padx=5, pady=5)

        frame2 = Frame(self, width=500)
        frame2.pack(fill=BOTH, side=LEFT, expand=True)

        txt = Listbox(frame2, selectmode=SINGLE)
        txt.pack(fill=BOTH, pady=5, padx=5, expand=True)

        btn1.bind('<Button-1>', lambda event: self.addFile(event, txt))
        btn2.bind('<Button-1>', lambda event: self.runFromList(event, txt))

    def listUpdate(self, txt):
        txt.delete(0, END)
        temp = self.col.generateList()
        for el in temp:
            txt.insert(END, el)


def main(col):
    root = Tk()
    root.geometry("600x400+300+300")
    app = App(root, col)
    root.mainloop()
