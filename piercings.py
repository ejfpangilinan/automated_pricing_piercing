import os
from tkinter import *
from PIL import ImageTk, Image


class Fill_up(object):
    def __init__(self, canvas, color, label):
        self.canvas = canvas
        self.frame = Frame(self.canvas, bg=color)

        label = Label(self.frame, text=label, width=15, bg=color, foreground='white', font=("Arial Bold", 10))
        label.pack(side=LEFT, padx=5,pady=5,anchor='n')
        entry= Entry(self.frame)
        entry.pack(fill=X, padx=5,pady=5,expand=True,anchor='n')
        
        self.frame.pack(fill=X,padx=5)




class SignUp(object):
    def __init__(self, root):
        self.root = root
        # self.root.resizable(height=0,width=0)
        self.canvas = Canvas(self.root, bg = '#ea8a8a')


        img = Image.open('ravana.png')
        img = img.resize((100, 50))
        img = ImageTk.PhotoImage(img)
        panel = Label(self.canvas, image = img,bg='#ea8a8a')
        panel.image = img
        panel.pack(padx=5,pady=15,anchor='center')

        Title = Label(self.canvas, text="Sign Up", bg='#ea8a8a', foreground='beige',font=("Arial Bold", 15))
        Title.pack(side=TOP, padx=5, pady=10, anchor='n')

        Name = Fill_up(self.canvas,'#ea8a8a','Name')
        IG = Fill_up(self.canvas,'#ea8a8a','IG username')
        Age = Fill_up(self.canvas,'#ea8a8a','Age')
        Contact_number = Fill_up(self.canvas,'#ea8a8a','Contact number')
        Email = Fill_up(self.canvas,'#ea8a8a','Email Address')

        #button
        self.Next= Button(self.canvas, anchor='center', text='Continue', bg='#ef999c', foreground='white',font=("Arial Bold", 10),width=30)
        self.Next.bind("<Enter>", self.on_enter)
        self.Next.bind("<Leave>", self.on_leave)

        self.Next.pack(side=BOTTOM,padx=5, pady=30, anchor='center')
        #needed date and time to dbs
        
    def on_enter(self,e):
            e.widget['background'] = '#ea8a8a'
            e.widget['foreground'] = 'white'
    def on_leave(self,e):
        e.widget['background'] = '#ef999c'
        e.widget['foreground'] = 'beige'


        

class APrice(object):
    def __init__(self, root):
        self.root = root
        self.canvas = Canvas(self.root, bg='gray')

class Confirm(object):
    def __init__(self, root, signup, aprice):
        self.root = root
        self.canvas = Canvas(self.root, bg='gray')


class Init(object):
    def __init__(self):
        self.root = Tk()
        self.root.title("PIERCINGS.RAVANA") #title of system
        y, x = (self.root.winfo_screenheight()//2)-200 , (self.root.winfo_screenwidth()//2)-200
        self.root.geometry("400x400+"+str(x)+"+"+str(y))
        
        #info needed
        self.SignUp = SignUp(self.root)
        self.APrice = APrice(self.root)
        self.Confirm = Confirm(self.root, self.SignUp, self.APrice)

        self.SignUp.canvas.pack(fill=BOTH,pady=5, padx=5, expand=True, anchor='center')

        self.root.mainloop()

def launch():
	Init()

if __name__ == '__main__': launch()