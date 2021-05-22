import os
from tkinter import *
from PIL import ImageTk, Image
import time
from datetime import datetime

GLOBAL_USER = {}
USER_CNT = 0

class Fill_up(object):
    def __init__(self, canvas, color, label):
        self.canvas = canvas
        self.textvar = ''
        self.frame = Frame(self.canvas, bg=color)

        self.label = Label(self.frame, text=label, width=15, bg=color, foreground='white', font=("Arial Bold", 10))
        self.label.pack(side=LEFT, padx=5,pady=5,anchor='n')
        self.entry= Entry(self.frame,textvariable=self.textvar)
        self.entry.pack(fill=X, padx=5,pady=5,expand=True,anchor='n')
        
        self.frame.pack(fill=X,padx=5)

    def get_text(self):
        ret = self.entry.get()
        self.entry.delete(0,END)
        self.canvas.update()
        return ret
        



class APrice(object):
    def __init__(self):
        self.root = Tk()
        y, x = (self.root.winfo_screenheight()//2)-510 , (self.root.winfo_screenwidth()//2)-400
        self.root.geometry("800x1000+"+str(x)+"+"+str(y))
        self.canvas = Canvas(self.root, bg='gray')

        

class Confirm(object):
    def __init__(self, root, signup, aprice):
        self.root = root
        self.canvas = Canvas(self.root, bg='gray')


class SignUp(object):
    def __init__(self):
        self.root = Tk()
        self.root.title("PIERCINGS.RAVANA") #title of system
        y, x = (self.root.winfo_screenheight()//2)-200 , (self.root.winfo_screenwidth()//2)-200
        self.root.geometry("400x400+"+str(x)+"+"+str(y))
        self.canvas = Canvas(self.root, bg = '#ea8a8a')


        img = Image.open(r'automated_pricing_piercing\ravana.png')
        img = img.resize((100, 50))
        img = ImageTk.PhotoImage(img)
        panel = Label(self.canvas, image = img,bg='#ea8a8a')
        panel.image = img
        panel.pack(padx=5,pady=15,anchor='center')

        self.Title = Label(self.canvas, text="Sign Up", bg='#ea8a8a', foreground='beige',font=("Arial Bold", 15))
        self.Title.pack(side=TOP, padx=5, pady=10, anchor='n')

        self.Name = Fill_up(self.canvas,'#ea8a8a','Name')
        self.IG = Fill_up(self.canvas,'#ea8a8a','IG username')
        self.Age = Fill_up(self.canvas,'#ea8a8a','Age')
        self.Contact_number = Fill_up(self.canvas,'#ea8a8a','Contact number')
        self.Email = Fill_up(self.canvas,'#ea8a8a','Email Address')

        #button
        self.Next= Button(self.canvas, anchor='center', text='Continue', bg='#ef999c', foreground='white',font=("Arial Bold", 10),width=30, command=self.next_page)
        self.Next.bind("<Enter>", self.on_enter)
        self.Next.bind("<Leave>", self.on_leave)

        self.Next.pack(side=BOTTOM,padx=5, pady=30, anchor='center')
        #needed date and time to dbs

        self.canvas.pack(fill=BOTH,pady=5, padx=5, expand=True, anchor='center')

        self.root.mainloop()




    def on_enter(self,e):
            e.widget['background'] = '#ea8a8a'
            e.widget['foreground'] = 'white'
    def on_leave(self,e):
        e.widget['background'] = '#ef999c'
        e.widget['foreground'] = 'beige'

    def next_page(self):
        global GLOBAL_USER, USER_CNT

        user_ind = []
        #checking before exit
        # print(self.Name.get_text()) #sample
        # time.sleep(0.5)

        #Nochecking Test
        user_ind.append(self.Name.get_text())
        user_ind.append(self.IG.get_text())
        user_ind.append(self.Age.get_text())
        user_ind.append(self.Contact_number.get_text())
        user_ind.append(self.Email.get_text())
        #DateTime
        user_ind.append(str(datetime.now()))

        GLOBAL_USER[str(datetime.date(datetime.now()))+"-"+str(USER_CNT)] = user_ind
        USER_CNT+=1

        self.root.destroy()
        APrice()



def launch():
	SignUp()

if __name__ == '__main__': launch()