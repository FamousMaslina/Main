import os
import time
global sond
from importlib import import_module
try:
    from idgpu import gpu
    import idgpu as shd
    module_name3 = gpu.replace('.py', '')
    gpu_module = import_module(module_name3)
    gpuC = True
except ImportError:
   gpuC = False
   pass
try:
    from idsound import sound
    module_name6 = sound.replace('.py', '')
    son_module = import_module(module_name6)
    sond = True
except ImportError as sounderror:
    sond = False
    pass
try:
    from idmod import modem
    module_name4 = modem.replace('.py', '')
    md_module = import_module(module_name4)
    mdC = True
except ImportError as e:
   mdC = False
   pass
try:
    from bios import main
except ImportError as e:
    while True:
        print(e)
        input("SYSTEM HALTED")

from idcpu import cpu
from idmb import mb
from idhd import hd
from idkey import key
from idmon import mon
global intern
intern = 0
module_name = cpu.replace('.py', '')  # Remove the .py extension
module_name2 = mb.replace('.py', '')
cpu_module = import_module(module_name)
mb_module = import_module(module_name2)
module_name3 = hd.replace('.py', '')
hd_module = import_module(module_name3)
module_name4 = key.replace('.py', '')
key_module = import_module(module_name4)
module_name5 = mon.replace('.py', '')
mon_module = import_module(module_name5)
from op2api import *
subprocess.run(["python", "op2api.py"])
time.sleep(0.1)
import re
clear()
freesp = hd_module.hddspace - space
freesp = round(freesp, 2)
if cpu_module.cFreq < 4.7:
    print("Your CPU, does not meet the minnimum requirments!")
    print("Expected Atleast 4.77Mhz! Idendtified:", cpu_module.cFreqS)
    input("Press enter to exit...")
    exit()
def find_python_files(directory):
  """Finds all Python files in the specified directory."""
  files = os.listdir(directory)
  python_files = []
  for file in files:
    if file.endswith(".py"):
      python_files.append(os.path.join(directory, file))
  return python_files


    
import op2v
osName = "PTOS"
osVersion = op2v.op2VER
clear()
check()
clear()




init(autoreset=True)

def api():
   check()

def restart():
    time.sleep(sleep_timeAppL)
    os.system("ptos.py")
    exit()
config = ConfigParser()
global ex
ex = False
if os.path.exists('ptos.ini'):
    ex = True
else:
    ex = False
def configuration():
    conf = 'ptos.ini'
    if ex == False:
        while True:
            print(conf, "not found. Create new one? Y/N ")
            bioscr = input("")
            bioscr = bioscr.lower()
            if bioscr == "y":
                config.add_section('user')
                config.set('user', 'computer_name', 'DEFAULT')
                with open("ptos.ini", 'w') as configfile:
                    config.write(configfile)
                print("Closing to apply changes. Created", conf)
                time.sleep(3.5)
                restart()
            else:
                while True:
                    print("Invalid command/ config file operation canceled.")
                    time.sleep(2)
                    break          
    else:
        while True:
            print(conf, "already present. Operation Canceled.")
            time.sleep(2)
            break
if ex == True:
    try:
        config.read("ptos.ini")
        settings = config["user"]
        ex = True
    except FileNotFoundError:
        ex = False
        pass
else:
    pass
def cls():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def open_text(file_name):
    
    if os.path.isfile(file_name):
        time.sleep(sleep_timeAppL)
        subprocess.run(["type", file_name], shell=True)
        print()
    else:
        print(f"File '{file_name}' not found.")


def nameO():
    print(osName, osVersion)




#def audio():
    

def info():
    print()
    nameO()
    time.sleep(sleep_timeIAppL)
    print("Build", op2v.op2VERSTRING)
    print("Built on OP2 Kernel")
    print("Kernel Version:", op2v.op2VERI)
    time.sleep(sleep_timeIAppL)
    if ex == True:
        print("Computer name: {}".format(settings["computer_name"]))
    else:
        pass
    time.sleep(sleep_timeIAppL)
    print(cpu_module.cName, "running at", cpu_module.cFreqS+cpu_module.cFreqUnit)
    print()




def help():
    time.sleep(sleep_timeAppL)
    print()
    print("Commands:")
    linebr(20)
    print("OS Related:")
    print("  info - Display information about the OS")
    print("  cls - Clear the screen")
    print("  configuration - Create the configuration file for PTOS")
    print("  settings - Change settings from the configuration file")
    print("  restart - Restart PTOS")
    print("  exit - Exit the OS and the CMD")
    linebr2(20)
    print("File/Directory Managment:")
    print("  run [FILENAME.EXTENSION] - Run other files (Only Python files work)")
    print("  open [FILENAME.EXTENSION] - Open other files to read their contents (Any files work)")
    print("  dir - Show files in the current working directory (CWD)")
    print("  del [FILENAME.EXTENSION] - Delete Files")
    linebr2(20)
    print("Applications (some of them cannot exist, due to your install options or version/build):")
    print("  calc - Calculator")
    linebr2(20)
    print("Hardware Related:")
    print("  hardware - Identify GPUs, Modems, Sound Cards")
    print("  dvcman - Current Installed Hardware")
    linebr2(20)
    print("API Related:") 
    print("  api - Check API version")
    print("  api /? - Check API's help")
    linebr2(20)
    print("Advanced:") 
    print("  bios - Enter the BIOS")
    linebr(20)
    print()

def hardware():
   try:
        subprocess.run(["python", 'hardwiz.py'])
   except FileNotFoundError:
      pass
def bios():
    time.sleep(sleep_timeAppL)
    clear()
    from bios import main
    main()


def run_file(file_name):
    try:
        time.sleep(sleep_timeAppL)
        subprocess.run(["python", file_name])
    except FileNotFoundError:
        print("File not found.")
    except subprocess.CalledProcessError as e:
        print("An error occurred:", e)
def del_file(file_name):
    try:
        time.sleep(sleep_timeAppL)
        os.remove(file_name)
    except FileNotFoundError:
        print("File not found.")

def calc():
  clear()
  print("Type '0000' to exit.")
  while True:
    calci = input("P:/int/> ")
    result = eval(calci)
    if result == 0000:
       clear()
       break
    else:
        print("=", result)
    print()




def mainOS():
    clear()
    nameO()
    while True:
        inp = input(f"P:/> ")
        inp = inp.lower()
        if inp in ('bios', 'info', 'cls', 'exit', 'restart', 'api','calc', 'configuration', 'help', 'hardware'):
            eval(inp)()
        elif inp.startswith('run '):
            run_file(inp[4:])
        elif inp.startswith('del '):
            del_file(inp[4:])
        elif inp == 'dir':
            time.sleep(sleep_timeAppL)
            print("Current directory: P:\\")
            files = os.listdir(".")
            for f in files:
                file_type = os.path.isfile(f) and "File" or "Folder"
                size = os.path.getsize(f)
                print(f"{file_type:8s} {f:20s} {size:8,d}")
        elif inp.startswith('open '):
            open_text(inp[5:])
        elif inp == "api.interface":
           interface()
        elif inp == "api /?":
           apihelp()
        elif inp == "dvcman":
            time.sleep(sleep_timeAppL)
            print()
            print("Identified Hardware:")
            linebr(20)
            time.sleep(sleep_timeIAppL)
            print("ACPI Based Computer:")
            time.sleep(sleep_timeIAppL)
            print("  Motherboard - "+mb_module.mName)
            time.sleep(sleep_timeIAppL)
            print("  Physical Memory - "+mb_module.mMemS)
            time.sleep(sleep_timeIAppL)
            linebr2(20)

            print("Processors:")
            time.sleep(sleep_timeIAppL)
            print("  Processor - "+cpu_module.cName)
            time.sleep(sleep_timeIAppL)
            print("  Processor Speed - "+cpu_module.cFreqS+cpu_module.cFreqUnit)
            time.sleep(sleep_timeIAppL)
            linebr2(20)

            print("Storage Devices:")
            time.sleep(sleep_timeIAppL)
            print("  Hard Disk - "+hd_module.hddnameS)
            time.sleep(sleep_timeIAppL)
            print("  Hard Disk Storage - "+hd_module.hddspaceS)
            time.sleep(sleep_timeIAppL)
            print("  Free Hard Disk Storage -",freesp, "KB")
            linebr2(20)

            if gpuC == False:
                pass
            else:
                print("Graphics Adapters:")
                time.sleep(sleep_timeIAppL)
                print("  Graphic Processor - "+gpu_module.gName)
                time.sleep(sleep_timeIAppL)
                print("  Graphic Memory -",gpu_module.gVram, "MB")
                time.sleep(sleep_timeIAppL)
                linebr2(20)
            if sond == False:
                pass
            else:
                print("Sound Devices:")
                time.sleep(sleep_timeIAppL)
                print("  Sound Processor - "+son_module.soundName)
                time.sleep(sleep_timeIAppL)
                print("  Sound Chip -",son_module.soundChip)
                time.sleep(sleep_timeIAppL)
                print("  Sound Digital Format -",son_module.soundDF)
                time.sleep(sleep_timeIAppL)
                print("  Stereo Capable -",son_module.stereo)
                time.sleep(sleep_timeIAppL)
                linebr2(20)
            if mdC == False:
                pass
            else:
                print("Internet Devices:")
                time.sleep(sleep_timeIAppL)
                print("  Modem - "+md_module.modemname, "at "+md_module.modemspeeds)
                time.sleep(sleep_timeIAppL)
                print("  Dial-Up Adapter -",md_module.dialupadp)
                time.sleep(sleep_timeIAppL)
                linebr2(20)
            print("Display Adapters:")
            time.sleep(sleep_timeIAppL)
            print("  Monitor Resolution - "+mon_module.monitorRes, mon_module.monitorHz)
            linebr2(20)
            print("  Operating System - "+osName, osVersion)
            linebr(20)
            print()
        elif inp == "var":
           print("osName", osName)
           print("osVersion", osVersion)
           print("config", config)
           print("gpuC", gpuC)
           print("intern", intern)
           print("VERSTRING:", op2v.op2VERSTRING)
           print("sond", sond)
        elif inp == "settings":
            if ex == True:
                cls()
                while True:
                    cls()
                    print("What do you wanna change?")
                    linebr(20)
                    print("1 - Computer Name")
                    print("2 - Exit")
                    linebr(20)
                    ch = input("> ")
                    if ch == "1":
                        new = input("Type in your desired name: ")
                        settings['computer_name'] = new
                        with open('op2.ini', 'w') as a:
                            config.write(a)
                        print("SET!")
                        break
                    elif ch == "2":
                        break
        else:
            print("Unknown command")

try:
    import op2api
    if apiverI < 0.5:
        print("Cannot load: Too low API version. Expected Version 0.5")
        input("")
    elif apiverI == 0.5 or apiverI > 0.5:
        if __name__ == "__main__":
            pass
except ImportError:
    print("API not found/ not working")
