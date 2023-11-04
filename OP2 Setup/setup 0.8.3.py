import time
import requests
import os
def cls():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
def linebr(number):
   print("=" * number)
def linebr2(number):
   print("-" * number)
name2 = "Opti P2"
op2vers = "0.8.3"
prsent = "Press enter to continue..."
print("Welcome to the Opti P2 Setup!")
print("Version", op2vers)
linebr(30)
input(prsent)
cls()
print("This will install OP2 on your system.")
input(prsent)
cls()
global apps
global om
global hardw
apps = True
om = True
hardw = True
while True:
    cls()
    print("Install options")
    linebr(30)
    print("True = Yes, False = No")
    linebr2(30)
    print("1 - Install Apps (write, nguess, encryp)", apps)
    #print("2 - Install Documentation", docss)
    #print("2 - Install Opti Messanger V0.1", om)
    #print("3 - Install Hardware", hardw)
    print("2 - Confirm Choices")
    linebr(30)
    ch = input("> ")
    if ch == "1":
        if apps == False:
            apps = True
        else:
            apps = False
    #elif ch == "2":
    #    if docss == False:
    #        docss = True
    #    else:
     #       docss = False
    #elif ch == "2":
    #    if om == False:
    #        om = True
    #    else:
    #        om = False
    #elif ch == "3":
    #    if hardw == False:
    #        hardw = True
    #    else:
    #        hardw = False
    elif ch == "2":
        cls()
        break

print("Setup will begin installing...")
print()
time.sleep(2)
u1 = "https://raw.githubusercontent.com/FamousMaslina/Main/main/Opti%20P/Opti%20P2%200.8.3/op2.py"
response = requests.get(u1)
print("op2.py...")
print()
with open("op2.py", "wb") as f:
    f.write(response.content)
    f.close()


u1 = "https://raw.githubusercontent.com/FamousMaslina/Main/main/Opti%20P/Opti%20P2%200.8.3/386basic.py"
response = requests.get(u1)
print("386basic.py...")
print()
with open("386basic.py", "wb") as f:
    f.write(response.content)
    f.close()

u1 = "https://raw.githubusercontent.com/FamousMaslina/Main/main/Opti%20P/Opti%20P2%200.8.3/Intel%20i486SX-66.py"
response = requests.get(u1)
print("Intel i486SX-66.py...")
print()
with open("Intel i486SX-66.py", "wb") as f:
    f.write(response.content)
    f.close()


u1 = "https://raw.githubusercontent.com/FamousMaslina/Main/main/Opti%20P/Opti%20P2%200.8.3/bios.ini"
response = requests.get(u1)
print("bios.ini...")
print()
with open("bios.ini", "wb") as f:
    f.write(response.content)
    f.close()


u1 = "https://raw.githubusercontent.com/FamousMaslina/Main/main/Opti%20P/Opti%20P2%200.8.3/bios.py"
response = requests.get(u1)
print("bios.py...")
print()
with open("bios.py", "wb") as f:
    f.write(response.content)
    f.close()


u1 = "https://github.com/FamousMaslina/Main/blob/main/Opti%20P/Opti%20P2%200.8.3/dial.mp3"
response = requests.get(u1)
print("dial.mp3...")
print()
with open("dial.mp3", "wb") as f:
    f.write(response.content)
    f.close()


u1 = "https://raw.githubusercontent.com/FamousMaslina/Main/main/Opti%20P/Opti%20P2%200.8.3/hard64.py"
response = requests.get(u1)
print("hard64.py...")
print()
with open("hard 64.py", "wb") as f:
    f.write(response.content)
    f.close()

##
u1 = "https://raw.githubusercontent.com/FamousMaslina/Main/main/Opti%20P/Opti%20P2%200.8.3/hardwiz.py"
response = requests.get(u1)
print("hardwiz.py...")
print()
with open("hardwiz.py", "wb") as f:
    f.write(response.content)
    f.close()


u1 = "https://raw.githubusercontent.com/FamousMaslina/Main/main/Opti%20P/Opti%20P2%200.8.3/op2.ini"
response = requests.get(u1)
print("op2.ini...")
print()
with open("op2.ini", "wb") as f:
    f.write(response.content)
    f.close()


u1 = "https://raw.githubusercontent.com/FamousMaslina/Main/main/Opti%20P/Opti%20P2%200.8.3/op2api.py"
response = requests.get(u1)
print("op2api.py...")
print()
with open("op2api.py", "wb") as f:
    f.write(response.content)
    f.close()


u1 = "https://raw.githubusercontent.com/FamousMaslina/Main/main/Opti%20P/Opti%20P2%200.8.3/op2v.py"
response = requests.get(u1)
print("op2v.py...")
print()
with open("op2v.py", "wb") as f:
    f.write(response.content)
    f.close()


u1 = "https://raw.githubusercontent.com/FamousMaslina/Main/main/Opti%20P/Opti%20P2%200.8.3/ps2keyboard.py"
response = requests.get(u1)
print("ps2keyboard.py...")
print()
with open("ps2keyboard.py", "wb") as f:
    f.write(response.content)
    f.close()


u1 = "https://raw.githubusercontent.com/FamousMaslina/Main/main/Opti%20P/Opti%20P2%200.8.3/vgamonitor.py"
response = requests.get(u1)
print("vgamonitor.py...")
print()
with open("vgamonitor.py", "wb") as f:
    f.write(response.content)
    f.close()

if apps == False:
    pass
elif apps == True:
    u1 = "https://raw.githubusercontent.com/FamousMaslina/Main/main/Opti%20P/Opti%20P2%200.8.3/encryp.py"
    response = requests.get(u1)
    print("encryp.py...")
    print()
    with open("encryp.py", "wb") as f:
        f.write(response.content)
        f.close()
    u1 = "https://raw.githubusercontent.com/FamousMaslina/Main/main/Opti%20P/Opti%20P2%200.8.3/nguess.py"
    response = requests.get(u1)
    print("nguess.py...")
    print()
    with open("nguess.py", "wb") as f:
        f.write(response.content)
        f.close()
    u1 = "https://raw.githubusercontent.com/FamousMaslina/Main/main/Opti%20P/Opti%20P2%200.8.3/write.py"
    response = requests.get(u1)
    print("write.py...")
    print()
    with open("write.py", "wb") as f:
        f.write(response.content)
        f.close()
#elif om == False:
    #pass
#elif om == True:
#    u1 = "https://raw.githubusercontent.com/FamousMaslina/Main/main/Opti%20P/Opti%20Messeages/client.py"
#    response = requests.get(u1)
#    print("Installing Opti Messages...")
#    print()
#    with open("client.py", "wb") as f:
#        f.write(response.content)
#        f.close()
 #   u1 = "https://raw.githubusercontent.com/FamousMaslina/Main/main/Opti%20P/Opti%20Messeages/server.py"
 #   response = requests.get(u1)
 #   with open("server.py", "wb") as f:
 #       f.write(response.content)
 #       f.close()
print("If you want more hardware, go here: https://github.com/FamousMaslina/Main/tree/main/Opti%20P/Opti%20P2%200.8.3")

