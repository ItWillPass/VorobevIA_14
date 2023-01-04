#3) Создать 25 файлов и заполнить их 10 случайными числами.

import random

directory = "DevOpsPraktika4/"
for i in range(25):
    name = f"{i}.txt"
    output = open(directory + name, 'x')

    for j in range(10):
        output.write(f"{random.randint(0, 10)} ")