from functions import*
from calculator import*
from cylinder import*
import os

while True:
    os.system('cls')
    print("\t---------------------------------------------------------------")
    print("\t                         Menu                                  ")
    print("\t---------------------------------------------------------------")
    print("\t                 press '1' to use a calculator                 ")
    print("\t                 press '2' to calculate for cone               ")
    print("\t                 press '3' to calculate for sphere             ")
    print("\t                 press '4' to calculate for Cylinder           ") 
    print("\t---------------------------------------------------------------")
    option=int(input("Enter your option: "))
    if option==1:
        calculator()
    elif option==2:
        cone()
    elif option==3:
        sphere()
    elif option==4:
        cylinder()
    else:
        print("no option")
