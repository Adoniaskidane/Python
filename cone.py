from tkinter import*
def callback():
    exit()
def conefigue_surface(num):
    ob=Tk()
    canvas=Canvas(width=400,height=400)
    canvas.pack()
    canvas.create_polygon(200,50,50,300,350,300,outline="#476042",fill='orange')
    canvas.create_arc(50,275,350,325,extent=359.9,fill="black")
    Answer=Label(ob,text="The surface are of the Cone is: "+str(num),font=("Times",20))
    Answer.pack()
    button=Button(ob,text="BACK-TO-OPTIONS",command=callback)
    button.pack()
    ob.mainloop()

def conefigue_volume(num):
    ob=Tk()
    canvas=Canvas(width=400,height=400)
    canvas.pack()
    canvas.create_polygon(200,50,50,300,350,300,outline="#476042",fill='orange')
    canvas.create_arc(50,275,350,325,extent=359.9,fill="black")
    Answer=Label(ob,text="The volume of the Cone is: "+str(num),font=("Times",20))
    Answer.pack()
    button=Button(ob,text="BACK-TO-OPTIONS",command=callback)
    button.pack()
    ob.mainloop()
