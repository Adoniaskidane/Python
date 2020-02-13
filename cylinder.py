from tkinter import*
def callback():
    exit()
def cylinderfigue_surface(num):
    ob=Tk()
    canvas=Canvas(ob,width=500,height=500)
    canvas.create_arc(50,50,400,100, extent=359.9, fill='orange')
    canvas.create_line(50,75,50,375)
    canvas.create_line(400,75,400,380)
    canvas.create_arc(50,350,400,400, extent=359.9, fill='orange')
    
    Answer=Label(ob,text="The surface are of the Cylinder is: " + str(num),font=("Times",20))
    Answer.pack()
    canvas.pack()
    button=Button(ob,text="KILL THE PROGRAM",bg="red",fg="white",command=callback)
    button.pack()
    
    ob.mainloop()
def cylinderfigue_volume(num):
    ob=Tk()
    canvas=Canvas(ob,width=500,height=500)
    canvas.create_arc(50,50,400,100, extent=359.9, fill='orange')
    canvas.create_line(50,75,50,375)
    canvas.create_line(400,75,400,380)
    canvas.create_arc(50,350,400,400, extent=359.9, fill='orange')
    
    Answer=Label(ob,text="The volume of a the Cylnder is: " + str(num),font=("Times",20))
    Answer.pack()
    canvas.pack()
    button=Button(ob,text="KILL THE PROGRAM",bg="red",fg="white",command=callback)
    button.pack()
    
    ob.mainloop()
        
