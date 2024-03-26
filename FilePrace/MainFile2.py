# Task 1
# otevřít soubor a načíst
# rozsekat data po mezeru pomocí len a pokud je to 7 a víc tak uložím do nového seznamu

#grafická okna přes knihovnu udělá exe soubor. qt python, pygame

"""
# Moje řešení:

file = open("first_task.txt","w")
file.write("Test text ahoj Jmenotrs asdfgtrsf")
file.close()

file = open("first_task.txt", "r")
data = file.read()
file.close()
data.split(" ")

my_world = []
for i in data.split(" "):
    if len(i) > 7:
        my_world.append(i + " ")


file = open("first_tas_outputs.txt", "w")
file.writelines(my_world)
file.close()

print(my_world)
print()
"""
# řešení učitel

import re

def task1(source, output_name, trashold = 7):
    print("cteni dat")
    file_handler = open(source, "r")
    data = file_handler.read()
    file_handler.close()

    print("predzpracovani dat")
    output_data = []
    split_data = re.split(r'\s+|entr',data)
    #print(type(split_data))

    print("filtrace dat")
    for word in split_data:
        if len(word) >= trashold:
            output_data.append(f"{word} ")

    print("Zapis dat")
    file_handler = open(output_name, "w")
    file_handler.writelines(output_data)
    file_handler.close()
    print("Finished")

#task1(source:"source.txt", output_name:"output.txt")
task1("source.txt", "output.txt")


