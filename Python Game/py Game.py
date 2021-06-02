from SavedData import *
stop = "no"

#Save to SavedData.py
def save():
    f = open("SavedData.py", "w")
    f.write("health = " + str(health) + "\n")
    f.write("money = " + str(money) + "\n")
    f.close()

while stop == str(input("no")):
    stop(str(input("""
Quit and save? (yes / no)
>>> """)))
