from tkinter import *

root = Tk()
root.title("Moving img")
root.geometry("800x600")

w = 600
h = 400
x = w/2
y = h/2

my_canvas = Canvas(root,width=x,height=h,bg='white')
my_canvas.pack(pady=20)

img = PhotoImage(file='alien.png')
img =img.subsample(2, 2)
img = img.subsample(2, 2)
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