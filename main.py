from time import time
from os.path import isfile
from os import remove
from math import floor


hunger = 0
food = 0
start_time = time()

if isfile("save.txt"):
    f = open("save.txt", "r")
    content = f.read().split("\n")
    start_time = float(content[0])
    food = int(content[1])
    f.close()


def save():
    f = open("save.txt", "w")
    content = f"{start_time}\n{food}"
    f.write(content)
    f.close()


save()


while True:
    prikaz = input()

    if prikaz == "brambora":
        food = food + 5
        save()

    end_time = time()

    s = round(end_time - start_time)

    if prikaz == "vek":
        m = floor(s / 60)
        s_r = s % 60

        h = floor(m / 60)
        m_r = m % 60

        print(f"{h}h {m_r}min {s_r}s")

    hunger = s / 2 - food

    if hunger > 100:
        print("Křeček vyhladověl!")
        remove("save.txt")
        exit()
    
    if hunger < 0:
        print("Křeček je překrmen!")
        remove("save.txt")
        exit()

    print(int(hunger))