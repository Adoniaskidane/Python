from tkinter import*
def sphere_area(num):
    ob=Tk()
    canvasob=Canvas(ob,width=600,height=500)
    canvasob.create_arc(50,50,400,400,extent=359.9,fill='orange')
    
    canvasob.create_arc(85,75,365,175,extent=180,style=ARC)
    canvasob.create_arc(57,125,393,225,extent=180,style=ARC)
    canvasob.create_arc(50,175,400,275,extent=180,style=ARC)
    canvasob.create_arc(55,225,395,325,extent=180,style=ARC)
    canvasob.create_arc(80,275,370,375,extent=180,style=ARC)
    canvasob.create_arc(110,330,340,400,extent=180,style=ARC)
    canvasob.create_arc(150,360,300,415,extent=180,style=ARC)
    canvasob.create_text(300,450,text="The surfacearea of sphere is: "+str(num),font=("Times",20))
    canvasob.pack()

    ob.mainloop()
def sphere_volume(num):
    ob=Tk()
    canvasob=Canvas(ob,width=600,height=500)
    canvasob.create_arc(50,50,400,400,extent=359.9,fill='orange')


    canvasob.create_arc(85,75,365,175,extent=180,style=ARC)
    canvasob.create_arc(57,125,393,225,extent=180,style=ARC)
    canvasob.create_arc(50,175,400,275,extent=180,style=ARC)
    canvasob.create_arc(55,225,395,325,extent=180,style=ARC)
    canvasob.create_arc(80,275,370,375,extent=180,style=ARC)
    canvasob.create_arc(110,330,340,400,extent=180,style=ARC)
    canvasob.create_arc(150,360,300,415,extent=180,style=ARC)
    canvasob.create_text(300,450,text="The Volume of sphere is: "+str(num),font=("Times",20))
    canvasob.pack()

    ob.mainloop()
