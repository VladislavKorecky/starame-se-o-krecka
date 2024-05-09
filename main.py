from time import time

hunger = 0
start_time = time()

f = open("save.txt", "w")
f.write(str(start_time))
f.close()

while True:
    input()
    end_time = time()

    hunger = (end_time - start_time) / 2

    print(int(hunger))