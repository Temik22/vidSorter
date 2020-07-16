import models
import collection as c
from tkinter import *
from tkinter import filedialog as fd


class App(Frame):
    source = []
    update = False

    def __init__(self, parent, col):
        Frame.__init__(self, parent)
        self.parent = parent
        self.col = col
        self.initUI()

    def addFile(self, txt):
        file = fd.askopenfilename(initialdir="/")
        s = str(file)
        left = s.rfind('/')
        right = s.rfind('.')
        name = s[left + 1:right]
        self.col.add(models.Video(name, path=file))
        self.listUpdate(txt)

    def removeFile(self, txt):
        index = txt.curselection()
        if len(index) != 0:
            index = index[0]
            if self.update:
                index = self.source[index]
            else:
                index = self.col.getIndexFromList(index)
            vid = self.col.data[index]
            self.col.remove(index)
            print('File {} was removed.'.format(vid.name))
            self.listUpdate(txt)
        else:
            print("File was not specified.")

    def runFromList(self, txt):
        index = txt.curselection()
        if len(index) != 0:
            print('Running current file...')
            index = index[0]
            if self.update:
                vid = self.col.data[self.source[index]]
            else:
                vid = self.col.data[self.col.getIndexFromList(index)]
            vid.seen = True
            vid.run()
            self.listUpdate(txt)
        else:
            print("File was not specified.")

    def searchWindow(self, txt):
        s = Toplevel()
        s.geometry('250x150+900+300')
        s.title("Search")

        fr1 = Frame(s)
        fr1.pack(fill=Y, side=LEFT, anchor=N)

        fr2 = Frame(s, height=10)
        fr2.pack(fill=X, side=BOTTOM)

        fr3 = Frame(s)
        fr3.pack(fill=X, side=RIGHT, anchor=N)

        clearButton = Button(fr2, text="Clear Fields", width=8)
        clearButton.pack(side=RIGHT, padx=5, pady=5)

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

        ent1Var = StringVar()
        ent1 = Entry(fr3, width=50, textvariable=ent1Var)
        ent1.pack(side=TOP, anchor=N, pady=5)

        ent2Var = StringVar()
        ent2 = Entry(fr3, width=50, textvariable=ent2Var)
        ent2.pack(side=TOP, pady=5)

        ent3Var = StringVar()
        ent3 = Entry(fr3, width=50, textvariable=ent3Var)
        ent3.pack(side=TOP, pady=5)

        ent4Var = BooleanVar()
        ent4 = Checkbutton(fr3, variable=ent4Var)
        ent4.pack(side=LEFT, pady=3)

        entrs = [ent1Var, ent2Var, ent3Var, ent4Var]

        okButton.bind(
            '<Button-1>', lambda event: self.makeSearch(txt, entrs))
        clearButton.bind('<Button-1>', lambda event: self.clearFields(entrs))

    def clearFields(self, entrs):
        for i in range(3):
            entrs[i].set('')
        entrs[3].set(False)

    def makeSearch(self, txt, entrs):
        result = []
        reqs = {0: "name", 1: "genre", 2: "rate", 3: "seen"}
        for i in range(4):
            text = entrs[i].get()
            if text != '':
                result.append(c.searchRequest(reqs[i], text))

        self.update = True
        self.source = self.col.search(result)
        self.listUpdate(txt)

    def resetFilter(self, txt):
        self.update = False
        self.source.clear()
        self.listUpdate(txt)

    def initUI(self):
        self.parent.title("App")
        self.pack(fill=BOTH, expand=True)

        frame1 = Frame(self, width=100)
        frame1.pack(fill=Y, side=RIGHT)

        btn1 = Button(frame1, text="Add", width=6)
        btn1.pack(side=TOP, anchor=N, padx=5, pady=5)

        btn2 = Button(frame1, text='Remove', width=6)
        btn2.pack(side=TOP, padx=5, pady=5)

        btn3 = Button(frame1, text='Edit File', width=6)
        btn3.pack(side=TOP, padx=5, pady=5)

        btn4 = Button(frame1, text="Run", width=6)
        btn4.pack(side=TOP, padx=5, pady=5)

        btn5 = Button(frame1, text="Search", width=6)
        btn5.pack(side=TOP, padx=5, pady=5)

        btn6 = Button(frame1, text='Reset Filter', width=8)
        btn6.pack(side=TOP, padx=5, pady=5)

        frame2 = Frame(self, width=500)
        frame2.pack(fill=BOTH, side=LEFT, expand=True)

        txt = Listbox(frame2, selectmode=SINGLE)
        txt.pack(fill=BOTH, pady=5, padx=5, expand=True)
        self.listUpdate(txt)

        btn1.bind('<Button-1>', lambda event: self.addFile(txt))
        btn2.bind('<Button-1>', lambda event: self.removeFile(txt))
        btn4.bind('<Button-1>', lambda event: self.runFromList(txt))
        btn5.bind('<Button-1>', lambda event: self.searchWindow(txt))
        btn6.bind('<Button-1>', lambda event: self.resetFilter(txt))

    def listUpdate(self, txt):
        txt.delete(0, END)
        if self.update:
            temp = []
            for k in self.source:
                temp.append(str(self.col.data[k]))
        else:
            temp = self.col.generateList()
        for el in temp:
            txt.insert(END, el)


def main(col):
    root = Tk()
    root.geometry("600x400+300+300")
    app = App(root, col)
    root.mainloop()
