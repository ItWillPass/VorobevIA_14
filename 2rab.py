#2) Есть два файла, нужно поменять данные файлов местами.

filenames = ["1.txt", "2.txt", "3.txt"]

if len(filenames)> 1:
    with open(filenames[0], "r", encoding="UTF-8") as file:
        first_file_content = file.read()
    for index in range(len(filenames) - 1):
        filename = filenames[index]
        nex_filename = filenames[index + 1]
        with open(filename, "w", encoding="UTF-8") as output:
            with open(nex_filename, "r", encoding="UTF-8") as file:
                output.write(file.read())
    with open(filenames, "w", encoding="UTF-8") as file:
        file.write(first_file_content)
