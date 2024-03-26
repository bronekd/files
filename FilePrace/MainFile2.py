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

def task1(source, output_name):
