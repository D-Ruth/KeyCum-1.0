# Start Of Development(First_Version)- 7/29/2023 - 6.47am
# Start Of Development(1.0-Release)- 7/30/2023 - 7.15am
# Libraries
import os
import time
# Combinations Of Yes
Y = "Y"
y = "y"
YES = "YES"
yes = "yes"
Yes = "Yes"
yEs = "yEs"
yeS = "yeS"
YEs = "YEs"
yES = "yES"
YeS = "YeS"
# Combinations Of No
N = "N"
n = "n"
NO = "NO"
no = "no"
No = "No"
nO = "nO"
# Variables Associated When Accepting Conditions
Accepted = 0
Unaccepted = 0
# Variables Representing Menu Choices
Your_Order_Please = 0
# Variables When Generating Combinations
Default_Path = r"C:\Users\Public\Documents\KeyCum-Combinations"
Str_Default_Path = str(Default_Path)
# Number One
Count = 0
Combination = 999
Possible_Combinations = 9000
# Introduction
os.system("cls")
print(" ")
print(" ")
print(" ")
print(" ")
print("         111        111        0000")
print("         111       111       000")
print("         111      111       000")
print("         111     111       000")
print("         1111111111       000")
print("         1111111111       000")
print("         111     111       000")
print("         111      111       000")
print("         111       111       000")
print("         111        111        0000                                                                   by:D.Ruth")
print(" ")
print(" ")
print(" ")
print(" ")
print("Some Conditions:")
print("                        -Non-Legal stuff done with the program will not be given responsibility by the creator.")
print(" ")
print("                        -This program is not promoting illegal activities.")
print(" ")
print("                        -Modifications made to the program to bypass Terms Of Service will still mean you have")
print("                         the full responsibility of the modification.")
print(" ")
print("                        -Responsibility for any modifications in the program will be taken by the creator of")
print("                         modification.")
print(" ")
print(" ")
print("Requests:")
print("                         -If you are using this opensource program in any external application, I would highly")
print("                          appreciate if you leave some credit, took me some time you know?")
print(" ")
print("                         -Have fun bros :D")
print(" ")
print(" ")
print(" ")
AcceptTOS = input("Do you accept the above conditions (y/n)- ")
# If Statements To Check If User Accepted The Conditions
if AcceptTOS == Y:
    Accepted = Accepted+1
if AcceptTOS == y:
    Accepted = Accepted+1
if AcceptTOS == YES:
    Accepted = Accepted+1
if AcceptTOS == yes:
    Accepted = Accepted+1
if AcceptTOS == Yes:
    Accepted = Accepted+1
if AcceptTOS == yEs:
    Accepted = Accepted+1
if AcceptTOS == yeS:
    Accepted = Accepted+1
if AcceptTOS == YEs:
    Accepted = Accepted+1
if AcceptTOS == yES:
    Accepted = Accepted+1
if AcceptTOS == YeS:
    Accepted = Accepted+1
if AcceptTOS == N:
    Accepted = Accepted+0
if Accepted == n:
    Accepted = Accepted+0
if Accepted == NO:
    Accepted = Accepted+0
if Accepted == no:
    Accepted = Accepted+0
if Accepted == No:
    Accepted = Accepted+0
if Accepted == nO:
    Accepted = Accepted+0
if Accepted == 0:
    os.system("cls")
    print(" ")
    print("Conditions Not Accepted")
    quit()
if Accepted == 1:
    os.system("cls")
    print(" ")
    print("Conditions Accepted")
    time.sleep(1)
    # Main Menu
    os.system("cls")
    print(" ")
    print("Input the number of the combination you want to generate:")
    print(" ")
    print("0- Quit The Program")
    print("1- Four Digit Numerical Passwords")
    print(" ")
    print(" ")
    # Special Message
    print("- The default location where your combinations will be generated is in [",Str_Default_Path,"]")
    print("   you can change the folder by changing [Line 30] in the python file KeyCum.py, which is the")
    print("   file you have currently opened.")
    print(" ")
    print(" ")
    # Generator Selector
    selection = input("Enter Number- ")
    # Selection Checker
    os.system("cls")
    selection_Check = str(selection)
    # Number Zero
    if selection_Check == "0":
        print(" ")
        print("Thank You For Using KeyCum...")
        quit()
    # Number One
    if selection_Check == "1":
        if not os.path.exists(Default_Path):
            os.makedirs(Default_Path)
        os.chdir(Default_Path)
        Text_File_Name = input("What do you want to name your text file? Make sure to not put already existing filenames- ")
        start = time.time()
        while Count < 9000:
            Combination = Combination+1
            S_Combination = str(Combination)+"\n"
            File = open(str(Text_File_Name), "a")
            File.write(S_Combination)
            Count = Count+1
            Percent_Completed = (Count/Possible_Combinations)*100
            Str_Percent_Completed = str(Percent_Completed)
            Completed_Msg = (Str_Percent_Completed+"% Completed")
            print(" ")
            print(" ")
            print(Completed_Msg)
            print(" ")
        end = time.time()
        time_taken = end - start
        str_time_taken = str(time_taken)
        print("All Possible Combinations Have Been Generated In An Estimated Time Of ", str_time_taken, " Seconds.")
# End Of Development(1.0-Release)- 7/30/2023 - 10.04pm
# End Of Development(First_Version)- 7/30/2023 - 7.05pm
