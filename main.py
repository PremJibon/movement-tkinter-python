from tkinter import *

root = Tk()

root.title("Movement")

x = 600/2
y = 400/2

my_canvas = Canvas(root,width=600,height=400,bg='white')
my_canvas.pack(pady=20)

img = PhotoImage(file='alien-cyan.png')
img = img.subsample(2,2)


my_image = my_canvas.create_image(200,100,anchor=NW,image=img)

def left(event):
    x = -10
    y = 0
    my_canvas.move(my_image,x,y)

def right(event):
    x = 10
    y = 0
    my_canvas.move(my_image,x,y)

def up(event):
    x = 0
    y = -10
    my_canvas.move(my_image,x,y)

def down(event):
    x = 0
    y = 10
    my_canvas.move(my_image,x,y)


root.bind("<Left>",left)
root.bind("<Right>",right)
root.bind("<Up>",up)
root.bind("<Down>",down)

root.mainloop()