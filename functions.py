def cylinder():
    import math
    print("The user must enter the following measured value to calculate: ")
    r=float(input("Enter the cylinder radius: "))
    h=float(input("Enter the cylinder height: "))



    def surfacearea():
        import cylinder
        A=(2*math.pi*h)+(2*math.pi*r**2)
        cylinder.cylinderfigue_surface(A)
    def volume():
        import cylinder
        V=math.pi*r**2*h
        cylinder.cylinderfigue_volume(V)
    
    while True:
        print("\t******************OPTION************************")
        print("\t|What would you like to calculate:             |")           
        print("\t|Press '1' for Surface area.                   |")
        print("\t|Press '2' for Volume.                         |")
        print("\t|Press '3' for both surface area and volume.   |")
        print("\t|press '4' to get back to main menu            |")
        print("\t|press '5' to terminate(exit) the program.     |")
        print("\t************************************************")
        option = int(input("OPTION NUMBER: "))
        if option==1:
            surfacearea()
            '''
            print("-----------------------------------------------------")
            print("The surface are of the cylinder is: ",surfacearea())
            print("-----------------------------------------------------")
            '''
            input("'To continue: 'Press<enter>") 
        elif option==2:
            volume()
            '''
            print("-----------------------------------------------------")
            print("The volume of the cylinder is: ",volume())
            print("-----------------------------------------------------")
            '''
            input("'To continue: 'Press<enter>")
        elif option==3:
            surfacearea()
            volume()
            '''
            print("-----------------------------------------------------")
            print("The surface are of the cylinder is: ",surfacearea())
            print("The volume of the cylinder is: ",volume())
            print("-----------------------------------------------------")
            '''
            input("'To continue: 'Press<enter>")
        elif option==4:
            break
        elif option==5:
            exit()
        else:
            print("you have entered wrong option!!")

def sphere():
    import math
    print("The user must enter the following measured value to calculate: ")
    r=float(input("Enter the sphere radius: "))
    
    def surfacearea():
        import sphere
        A=4*math.pi*r**3
        sphere.sphere_area(A)
        #return A
    def volume():
        import sphere
        V=(4/3)*math.pi*r**3
        sphere.sphere_volume(V)
        #return V
    while True:
        print("\t******************OPTION************************")
        print("\t|What would you like to calculate:             |")           
        print("\t|Press '1' for Surface area.                   |")
        print("\t|Press '2' for Volume.                         |")
        print("\t|Press '3' for both surface area and volume.   |")
        print("\t|press '4' to get back to main menu            |")
        print("\t|press '5' to terminate(exit) the program.     |")
        print("\t************************************************")
        option = int(input("OPTION NUMBER: "))
        if option==1:
            surfacearea()
            '''
            print("-----------------------------------------------------")
            print("The surface are of the Sphere is: ",surfacearea())
            print("-----------------------------------------------------")
            '''
            input("'To continue: 'Press<enter>")
        elif option==2:
            volume()
            '''
            print("-----------------------------------------------------")
            print("The volume of the Sphere is: ",volume())
            print("-----------------------------------------------------")
            '''
            input("'To continue: 'Press<enter>")
        elif option==3:
            surfacearea()
            volume()
            '''
            print("-----------------------------------------------------")
            print("The surface are of the Sphere is: ",surfacearea())
            print("The volume of the Sphere is: ",volume())
            print("-----------------------------------------------------")
            '''
            input("'To continue: 'Press<enter>")
        elif option==4:
            break
        elif option==5:
            exit()
        else:
            print("you have entered wrong option!!")
def cone():
    import math
    print("The user must enter the following measured value to calculate: ")
    r=float(input("Enter the Cone radius: "))
    h=float(input("Enter the Cone height: "))
    def surfacearea():
        import cone
        s=0.5*h*r
        A=math.pi * r**2 + math.pi * r * s
        cone.conefigue_surface(A)
    def volume():
        import cone
        V=(1/3)* math.pi * r**2 * h
        cone.conefigue_volume(V)
    
    while True:
        print("\t******************OPTION************************")
        print("\t|What would you like to calculate:             |")           
        print("\t|Press '1' for Surface area.                   |")
        print("\t|Press '2' for Volume.                         |")
        print("\t|Press '3' for both surface area and volume.   |")
        print("\t|press '4' to get back to main menu            |")
        print("\t|press '5' to terminate(exit) the program.     |")
        print("\t************************************************")
        option = int(input("OPTION NUMBER: "))
        if option==1:
            surfacearea()
            #print("-----------------------------------------------------")
            #print("The surface are of the Cone is: ",surfacearea())
            #print("-----------------------------------------------------")
            input("'To continue: 'Press<enter>")
            
        elif option==2:
            volume()
            #print("-----------------------------------------------------")
            #print("The volume of the Cone is: ",volume())
            #print("-----------------------------------------------------")
            input("'To continue: 'Press<enter>")
        elif option==3:
            surfacearea()
            volume()
            #print("-----------------------------------------------------")
            #print("The surface are of the Cone is: ",surfacearea())
            #print("The volume of the Cone is: ",volume())
            #print("-----------------------------------------------------")
            input("'To continue: 'Press<enter>")
        elif option==4:
            break
        elif option==5:
            exit()
        else:
            print("you have entered wrong option!!")



