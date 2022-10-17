# here put the production code

hexa = input("Entrez un nombre en hexadécimal à convertir en binaire : ")

hex_to_dec = 0

dec_to_bin = ""

for i in range(len(hexa)):
    char = hexa[i]
    if char in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        hex_to_dec += int(char) * 16**i
    elif char in ["A", "B", "C", "D", "E", "F"]:
        if char == "A":
            hex_to_dec += 10 * 16**i
        elif char == "B":
            hex_to_dec += 11 * 16**i
        elif char == "C":
            hex_to_dec += 12 * 16**i
        elif char == "D":
            hex_to_dec += 13 * 16**i
        elif char == "E":
            hex_to_dec += 14 * 16**i
        elif char == "F":
            hex_to_dec += 15 * 16**i
print(f"Le décimal de {hexa} est {hex_to_dec}")

while (hex_to_dec / 2 != 0) or (hex_to_dec / 2 != 1):
    division = hex_to_dec / 2
    print(div)
    dec_to_bin += str(division)

print(f"Le binaire de {hexa} est {dec_to_bin}")
