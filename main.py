from time import time
from os.path import isfile


hunger = 0
food = 0
start_time = time()

if isfile("save.txt"):
    f = open("save.txt", "r")
    content = f.read().split("\n")
    start_time = float(content[0])
    food = int(content[1])


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

    hunger = (end_time - start_time) / 2 - food

    print(int(hunger))