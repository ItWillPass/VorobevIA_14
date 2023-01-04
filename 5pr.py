#5) Сложить все числа из всех файлов.

dictionary = {}
directory = "Tempory/"
summator = 0

for i in range(25):
    name=f"{i}.txt"

    with open(directory + name, "r", encoding="UTF-8") as file:
        date = file.read()
        summator += sum(list(map(int, date.split(()))))
print(summator)