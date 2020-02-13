from tkinter import*
def calculator():
    ob=Tk()
    #ob.geometry("250x300")

    current=""
    insert=StringVar()
     
    insert.set("Enter number:")
    display=Label(ob,textvariable=insert,font=("Times",40))
    display.grid(row=0,columnspan=4)


    def evaluating(num):
        global current
        print(current)
        current=current+str(num)
        insert.set(current)
    def total():
        global current
        print(current)
        current=eval(current)
        current=str(current)
        insert.set(current)
    def clearing():
        global current
        current=""
        insert.set(current)
        
       

    b1=Button(None,text="       AC       ",fg="Black",bg="white",command=clearing,font=("Times",25))
    b1.grid(row=1,columnspan=2)
    b3=Button(None,text="  % ",fg="Black",bg="white",command=lambda:evaluating("%"),font=("Times",25))
    b3.grid(row=1,column=2)
    b4=Button(None,text="  /   ",fg="white",bg="orange",command=lambda:evaluating("/"),font=("Times",25))
    b4.grid(row=1,column=3)
    b5=Button(None,text="  x  ",fg="white",bg="orange",command=lambda:evaluating("*"),font=("Times",25))
    b5.grid(row=2,column=3)
    b6=Button(None,text="   -  ",fg="white",bg="orange",command=lambda:evaluating("-"),font=("Times",25))
    b6.grid(row=3,column=3)
    b7=Button(None,text="  +  ",fg="white",bg="orange",command=lambda:evaluating("+"),font=("Times",25))
    b7.grid(row=4,column=3)
    b9=Button(None,text="  =  ",fg="white",bg="orange",command=lambda:total(),font=("Times",25))
    b9.grid(row=5,column=3)


    button1=Button(None,text="   1   ",fg="white",bg="black",command=lambda:evaluating(1),font=("Times",25))
    button1.grid(row=2,column=0)
    button2=Button(None,text="   2   ",fg="white",bg="black",command=lambda:evaluating(2),font=("Times",25))
    button2.grid(row=2,column=1)
    button3=Button(None,text="  3  ",fg="white",bg="black",command=lambda:evaluating(3),font=("Times",25))
    button3.grid(row=2,column=2)


    button4=Button(None,text="   4   ",fg="white",bg="black",command=lambda:evaluating(4),font=("Times",25))
    button4.grid(row=3,column=0)
    button5=Button(None,text="   5   ",fg="white",bg="black",command=lambda:evaluating(5),font=("Times",25))
    button5.grid(row=3,column=1)
    button6=Button(None,text="  6  ",fg="white",bg="black",command=lambda:evaluating(6),font=("Times",25))
    button6.grid(row=3,column=2)


    button7=Button(None,text="   7   ",fg="white",bg="black",command=lambda:evaluating(7),font=("Times",25))
    button7.grid(row=4,column=0)
    button8=Button(None,text="   8   ",fg="white",bg="black",command=lambda:evaluating(8),font=("Times",25))
    button8.grid(row=4,column=1)
    button9=Button(None,text="  9  ",fg="white",bg="black",command=lambda:evaluating(9),font=("Times",25))
    button9.grid(row=4,column=2)


    button0=Button(None,text="         0         ",fg="white",bg="black",command=lambda:evaluating(0),font=("Times",25))
    button0.grid(row=5,columnspan=2)
    b8=Button(None,text="  .   ",fg="white",bg="black",command=lambda:evaluating("."),font=("Times",25))
    b8.grid(row=5,column=2)


    ob.mainloop()
