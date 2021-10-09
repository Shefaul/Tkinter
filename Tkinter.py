from tkinter import *

def hi():
    print('hi')
    


root = Tk()
root.title("Visuals ^ ^")
root.maxsize(900, 600)
root.config(bg='black')

Label(root, text='Shh', bg= 'cyan').grid(row = 0, column = 0, padx= 5, pady= 5, sticky= W)
Label(root, text='Shh', bg= 'cyan').grid(row = 0, column = 1, padx= 0, pady= 5, sticky= W)
Button(root, text='Print Hi', bg= 'cyan', command= hi).grid(row = 1, column = 0, padx= 5, pady= 5)


root.mainloop()
