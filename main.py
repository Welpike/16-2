hexa = input("Entrez un nombre hexadécimal à convertir en binaire : ")
bin = ""

for i in hexa:
    if i == "0":
        bin += "0000"
    elif i == "1":
        bin += "0001"
    elif i == "2":
        bin += "0010"
    elif i == "3":
        bin += "0011"
    elif i == "4":
        bin += "0100"
    elif i == "5":
        bin += "0101"
    elif i == "6":
        bin += "0110"
    elif i == "7":
        bin += "0111"
    elif i == "8":
        bin += "1000"
    elif i == "9":
        bin += "1001"
    elif i == "A" or i == "a":
        bin += "1010"
    elif i == "B" or i == "b":
        bin += "1011"
    elif i == "C" or i == "c":
        bin += "1100"
    elif i == "D" or i == "d":
        bin += "1101"
    elif i == "E" or i == "e":
        bin += "1110"
    elif i == "F" or i == "f":
        bin += "1111"
    else:
        print("Ce caractère n'est pas un caractère de la base 16.")
    bin += " "

print(f"Le binaire de {hexa} est {bin}")
