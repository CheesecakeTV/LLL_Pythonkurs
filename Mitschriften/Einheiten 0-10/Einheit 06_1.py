import os

os.mkdir("discord/LLL")

print(os.path.isdir("discord/LLL"))
print(os.path.exists("Einheit 00.py"))

exit()

with open("Namenliste.txt","r") as f:
    raw = f.read()

with open("test/hallowelt.discordkurs","w") as f:
    f.write("Hallo Discord")

with open("../Ablauf.md","r",encoding="utf-8") as f:
    print(f.read())

# f = open("Namenliste.txt","r")
# raw = f.read()
# f.close()

# f = open("test.txt","w")
# f.write("Hallo\nWelt")
# f.close()

# f = open("test.txt","a")
# f.write("\nHallo Discord")
# f.close()
