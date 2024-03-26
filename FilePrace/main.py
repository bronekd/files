# soubory
# ukládání změn v aplikací ukládám data. Teď bude jak uložit data a načíst data.
# nezáleží na koncovce nemusí být txt ale třeba me, můžu si vytvořit valstní typ přípony

file = open("first_file.me","w")
file.write("Test text")
file.close()

# Při čtení musí soubor existovat
file = open("first_file.me", "r")
data = file.read()
file.close()
print(data)


file = open("first_file.me","a")
file.write("\ndruhy radek")
file.close()



