#načtení po řádcích a zapis řádků:
def task2(source_name, output_name):
    f_source = open(source_name, "r")
    f_output = open(output_name, "a+")
    for line in f_source:
        f_output.write(line)

    f_source.close()
    f_output.close()

#task2("TextTask3.txt", "OutputTask3.txt")

# task 3
# You have a text file. Write its lines to another file. The order of lines in the second file must be inverse.
# Máte textový soubor. Zapište jeho řádky do jiného souboru. Pořadí řádků ve druhém souboru musí být inverzní.
import re

def task3(source_name, output_name):
    #načíst
    f_handler = open("TextTask3.txt", "r")
    data = f_handler.readlines()
    f_handler.close()
    
    #task 2 má lepší řešení přes a+
    f_handler = open(output_name, "w")
    f_handler.close()

    #uprava poslednich dat a mezere
    if data[-1][-1] != "\n":
        data[-1] = data[-1] + "\n"

    #prohodit
    f_handler = open(output_name, "a")
    for i in range(len(data) - 1, -1, -1):
        f_handler.write(data[i])
    f_handler.close()

#task3("TextTask3.txt", "OutputTask3.txt")


#task v2 contex manager

def task3v2(source_name, output_name):
   with open(source_name, "r") as file_handler:
    data = file_handler.readlines()

    # task 2 má lepší řešení přes a+
    f_handler = open(output_name, "w")
    f_handler.close()

    # uprava poslednich dat a mezere
    if data[-1][-1] != "\n":
        data[-1] = data[-1] + "\n"

    # prohodit
    f_handler = open(output_name, "a")
    for i in range(len(data) - 1, -1, -1):
        f_handler.write(data[i])
    f_handler.close()

task3v2("TextTask3.txt", "OutputTask3.txt")
