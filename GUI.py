import models
import collection as c
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
        index = txt.curselection()
        if len(index) != 0:
            print('Running current file...')
            index = index[0]
            vid = self.col.getFromList(index)
            vid.seen = True
            vid.run()
            self.listUpdate(txt)
        else:
            print("File was not specified.")

    def searchWindow(self, event):
        s = Toplevel()
        s.geometry('250x150+900+300')
        s.title("Search")

        fr1 = Frame(s)
        fr1.pack(fill=Y, side=LEFT, anchor=N)

        fr2 = Frame(s, height=10)
        fr2.pack(fill=X, side=BOTTOM)

        fr3 = Frame(s)
        fr3.pack(fill=X, side=RIGHT, anchor=N)

        closeButton = Button(fr2, text="Close", width=6)
        closeButton.pack(side=RIGHT, padx=5, pady=5)

        okButton = Button(fr2, text="OK", width=6)
        okButton.pack(side=RIGHT)

        lbl1 = Label(fr1, text="Name")
        lbl1.pack(side=TOP, anchor=N, pady=5)

        lbl2 = Label(fr1, text="Genre")
        lbl2.pack(side=TOP, pady=3)

        lbl3 = Label(fr1, text="Rating")
        lbl3.pack(side=TOP, pady=3)

        lbl4 = Label(fr1, text="Seen")
        lbl4.pack(side=TOP, pady=4)

        ent1 = Entry(fr3, width=50)
        ent1.pack(side=TOP, anchor=N, pady=5)

        ent2 = Entry(fr3, width=50)
        ent2.pack(side=TOP, pady=5)

        ent3 = Entry(fr3, width=50)
        ent3.pack(side=TOP, pady=5)

        ent4 = Checkbutton(fr3)
        ent4.pack(side=LEFT, pady=3)

        entrs = [ent1, ent2, ent3, ent4]

        okButton.bind(
            '<Button-1>', lambda event: self.makeSearch(event, entrs))

    def makeSearch(self, event, entrs):
        result = []
        reqs = {0: "name", 1: "genre", 2: "rate", 3: "seen"}
        for i in range(len(entrs)):
            result.append(c.searchRequest(reqs[i], entrs[i].get()))
        search = self.col.search(result)
        result = []
        for v in search.values():
            result.append(str(v))
        self.listUpdate()

    def initUI(self):
        self.parent.title("App")
        self.pack(fill=BOTH, expand=True)

        frame1 = Frame(self, width=100)
        frame1.pack(fill=Y, side=RIGHT)

        btn1 = Button(frame1, text="Add", width=6)
        btn1.pack(side=TOP, anchor=N, padx=5, pady=5)

        btn2 = Button(frame1, text="Run", width=6)
        btn2.pack(side=TOP, padx=5, pady=5)

        btn3 = Button(frame1, text="Search", width=6)
        btn3.pack(side=TOP, padx=5, pady=5)

        frame2 = Frame(self, width=500)
        frame2.pack(fill=BOTH, side=LEFT, expand=True)

        txt = Listbox(frame2, selectmode=SINGLE)
        txt.pack(fill=BOTH, pady=5, padx=5, expand=True)

        btn1.bind('<Button-1>', lambda event: self.addFile(event, txt))
        btn2.bind('<Button-1>', lambda event: self.runFromList(event, txt))
        btn3.bind('<Button-1>', self.searchWindow)

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
