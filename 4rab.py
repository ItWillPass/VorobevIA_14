#4) Найти сколько чисел повторилось в 25 файлах из 3-ей задачи.

dictionary = {}
directory = "Tempory/"

for i in range(25):
    name = f"{i}.txt"

    with open(directory + name, "r", encoding="UTF-8") as file:
        data = file.read()
        numbers = list(map(int, data.split(())))

        for number in numbers:
            if number in dictionary.keys():
                dictionary[number] +=1
            else:
                dictionary[number]= 1
        print(dictionary)