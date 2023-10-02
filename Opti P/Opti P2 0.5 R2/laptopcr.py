try:
    import op2api as api
except ImportError as e:
    print("API failed to import", e)
    input("Press enter to exit...")
    exit()
global vers
from configparser import ConfigParser
config = ConfigParser()
vers = 0.1
global nbreak
nbreak = "============"
def loadS
def load():
    while True:
        api.clear()
        print("Laptop Creator by ArielAutomat")
        print(nbreak)
        print("1 - Load")
        print("2 - New Game")
        print(nbreak)
        choice = input("> ")
        if choice == "2":
            while True:
                api.clear()
                print("1 - Default Settings")
                print("2 - Custom Settings")
                print(nbreak)
                cho = input("> ")
                if cho == "1":
                    config.add_section('data')
                    config.set('data', 'cn', 'Default')
                    config.set('data', 'matrix_scr', '0')
                    config.set('data', '386cpu', '0')
                    with open("save.ini", 'w') as configfile:
                        config.write(configfile)
                    mon = 550000
                    with open("money.py", 'w') as f:
                        f.write(mon)
def main():
    while True:
        api.clear()
        print("Laptop Creator by ArielAutomat")
        print(nbreak)
        print("1 - Desigin")
        print("2 - Research")
        print(nbreak)

try:
    import op2api as api
    api.check()
    if api.apiverI < 0.2:
        print("Cannot load: Too low API version. Expected Version 0.2")
        input("")
        exit()
    elif api.apiverI == 0.2:
        main()
except ImportError:
    print("API not found/ not working")