count = 0
import time
from prettytable import PrettyTable
from playsound import playsound
#for the cpudoom
count1 = 0
count2 = 0
import random
upperL = "ABCDEFGHIJKLMNOPQRSTUVXYWZ"
lowerL = upperL.lower()
digits = "0123456789"
symbols = ",<>./?;':"
#ends here
print("Copyright 1982-1995 Python Star")
print("===============================")
time.sleep(1)
print("Starting PS Check...")
time.sleep(0.2)
print("16MB Ram OK")
time.sleep(0.5)
mytable = PrettyTable(["CPU", "GPU", "MODEM", "SOUNDCARD"])

mytable.add_rows([
    ["i486", "BUILT-IN", "UNKONW", "Audio Blast"],
    ["32-Bit", "-", "-", "16-bit DAC"],
    ["16 MHz", "-", "-", "89 kHZ Play_back"],
])
print(mytable)

time.sleep(0.5)
print("Normal KeyBoard... Detected")
time.sleep(1)
print("Checking HDD Free Space...")
time.sleep(1.5)
print("3 MB Free")
time.sleep(0.5)

print("Booting...")
print()
print("Type help to get started!")
while count < 5:   
    os = input("P:Python\ ")
    if os == "about":
        print()
        print("Py OS 2 | Built on 'Count Technology V1'")
        print("1.0")
        print()
    elif os == "ulog":
        print()
        print("1.0 Updates:")
        print("Added 'overclock' to overclock you CPU")
        print("Added 'write' to learn english")
        print("Added 'credit'")
        print("Added 'tkill' to force close programs")
        print("Added 'format' to format a drive")
        print("Added the Py SDK!")
        print()
    elif os == "is it infinite?":
        print("Yes, brother..")
    elif os == "cpudoom.py":
        while count1 < 5:
            upper, lower, nums, syms = True, True, True, True
            all = ""
            if upper:
                all += upperL
            if lower:
                all += lowerL
            if nums:
                all += digits
            if syms:
                all += symbols
            lenght = 70
            amount = 50

            for x in range(amount):
                password = "".join(random.sample(all, lenght))
                print(password)
        
    elif os == "virusscanner":
        print("scanning...")
        time.sleep(1)
        print("System Clean!")
    elif os == "help":
        print()
        print("'ulog' to see the update log")
        print("'about' to see about Py OS 2")
        print("'virusscanner' to scan your system")
        print("'dir' to see the contetns of a folder (not availabile on P: Drive. Available on other drives D:, A:, C:, etc. Just type C: dir)")
        print("'pybrowser' to acces the internet!")
        print("'drives' to see the connected drives")
        print("'rating' to see how powerful your hardware is")
        print("'overclock' to overclock your CPU")
        print("'write' to write and open .txt files")
        print("'tkill (program name)' or 'tkill -f (program name)' to close a program")
        print("'format (drive letter)' or 'format -f (drive letter)' to format a drive")
        print()
        print("-F letters")
        print("In tkill commands those f's just mean 'force'")
        print("Otherwise in format means 'fast'")
        print()
    elif os == "dir":
        print("Not available on P: Drive")
    elif os == "pybrowser":
        print("Can't acces the internet")
        print("Reason: No Modem Found")
        modem = input("Want to search for a modem again? (y=yes n=no")
        if modem == "y":
            print("Detecting..")
            time.sleep(2)
            print("Not Found!")
            m2 = input("Want to select one from the list manually? (y=yes n=no)")
            if m2 == "y":
                modems = input("1=Py Modem, 2=Standart Modem, 3=Other")
                if modems == "1":
                    print("Seraching...")
                    print("Not Found!")
                    print("Internet setup canceld.")
                elif modems == "2":
                    print("Seraching...")
                    print("Not Found!")
                    print("Internet setup canceld.")
                elif modems == "2":
                    print("Seraching...")
                    print("Not Found!")
                    print("Internet setup canceld.")
                else:
                    print("Internet setup canceld.")
            elif m2 == "2":
                print("Internet setup canceld.")
            else:
                print("Internet setup canceld.")
        elif modem == "n":
            print("Internet setup canceld.")
        else:
            print("Internet setup canceld.")
    
    elif os == "defrag":
        print("starting defraging P:...")
        while count2 < 5:
            upper, lower, nums, syms = True, True, True, True
            all = ""
            if upper:
                all += upperL
            if lower:
                all += lowerL
            if nums:
                all += digits
            if syms:
                all += symbols
            lenght = 10
            amount = 1

            for x in range(amount):
                password = "".join(random.sample(all, lenght))
                print(password)
                print("1%...")
            upper, lower, nums, syms = True, True, True, True
            all = ""
            if upper:
                all += upperL
            if lower:
                all += lowerL
            if nums:
                all += digits
            if syms:
                all += symbols
            lenght = 70
            amount = 50

            for x in range(amount):
                password = "".join(random.sample(all, lenght))
                print(password)
                print("?%...")
    elif os == "techhelp":
     upper, lower, nums, syms = True, True, True, True
     all = ""
     if upper:
         all += upperL
     if lower:
         all += lowerL
     if nums:
         all += digits
     if syms:
         all += symbols
     lenght = 70
     amount = 1

     for x in range(amount):
         password = "".join(random.sample(all, lenght))
         print(password)
        
         print("Is a System Parameter that uses to load apps from hdd")
         print("If this shows no your screen then something is not good!")
    elif os == "D:":
         print("Contents of D: setup.py, readme.txt")
         d = input("D: ")
         if d == "setup":
             print()
             print("Windows 95 Setup")
             print()
             print("Installing Windows 95...")
             print("Transforming system.py to system.exe")
             print("The installation was unsuccsesfull")
         elif d == "readme":
             print("Cant open the file")
    elif os == "drives":
        print("Connected drives: P: D:")
    elif os == "rating":
        print("Intialnizing PS Hardware Rating Module...")
        time.sleep(1)
        print("CPU = 8/10")
        time.sleep(1)
        print("GPU = 5/10")
        time.sleep(1)
        print("RAM = 10/10")
        time.sleep(1)
        print("MODEM = ?")
        time.sleep(1)
        print("SOUNDCARD = 9/10")
        print("Overall rating: 6.5")
    elif os == "overclock":
        sure = input("Are you sure you want to overclock? ")
        if sure == "y":
            print("WARNING! THE OVERCLOCKING IS LOUD!")
            print("Starting CPU Overclocking...")
            playsound('over.mp3')
    elif os == "write":
        print("Start typing something: Please note that anything will not be saved")
        print("Even if you type save will not be saved. Wired...")
        print("When you are done type 'save'")
        print()
        print()
        playerChoice = input("")
        print()
        print()
        write = input("Write ")
        if write == "save":
            print("Saved!")
        elif write == "dont save":
            print("Not Saved!")
        else:
            print("Not Saved!")
    elif os == "credit":
        print()
        print("=====The Team=====")
        print()
        print("Programmer - ArielAutomat")
        print("Table - PrettyTable Module")
        print("Sound Effects - YouTube, ChromeExperiments, PlaySound Module")
        print("Inspiration: MS-Dos")
        print("For some commands: ma_joc_minecraft on Tiktok")
        print("Thank You!")
        print()

    elif os == "tkill system.py":
        print("Cannot kill a system program")
    elif os == "tkill -f system.py":
        print("Cannot kill a system program")
    elif os == "format P:":
        print("Cannot format the main drive")
       
    elif os == "format -f P:":
        print("Formating...")
        time.sleep(1)
        print("Cannot Format P: Drive.")
        print("Reason: driveinfo.cf file reported that P: is primary")
        print("Reason: A file is being used: system.py. Close the program in order to continue")
    elif os == "format -f D:":
        print("Formating...")
        time.sleep(1)
        print("Done!")
    elif os == "format D:":
        print("Formating...")
        time.sleep(5)
        print("Done!")
    else:
        print("Unknow Command")
