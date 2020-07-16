from tkinter import *
from tkinter import filedialog as fd

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent
        self.initUI()
    
    def insertText(self, txt):
    	file = fd.askopenfilename(initialdir = "/")
    	f = open(file)
    	s = f.read().split(' ')
    	#txt.delete(1.0, END)
    	for i in s:
    		txt.insert(END, i)
    	f.close()

    def initUI(self):
        self.parent.title("Review")
        self.pack(fill=BOTH, expand=True)
        
        frame1 = Frame(self, width = 100)
        frame1.pack(fill=Y, side = RIGHT)         
        # frame1.grid(column=1, columnspan=5)

        btn1 = Button(frame1, text="Add", width=6)
        btn1.pack(side=TOP, anchor = N, padx=5, pady=5) 
        

        btn2 = Button(frame1, text="Run", width=6)
        btn2.pack(side=TOP, padx=5, pady=5)
        
        frame2 = Frame(self, width = 500)
        frame2.pack(fill=BOTH, side = LEFT, expand = True)
        # frame2.grid(column=2)

        txt = Listbox(frame2)
        txt.pack(fill=BOTH, pady=5, padx=5, expand=True)

        btn1.bind('<Button-1>', lambda event, t = txt: self.insertText(t))
 
root = Tk()
root.geometry("600x400+300+300")
app = Example(root)
root.mainloop() 