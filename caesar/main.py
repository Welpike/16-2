# caesar coding [a;z]
z = 122
alphabet_lenght = 26
result = ""

key = int(input("Entrez la clé de chiffrement : "))
text = input("Entrer le texte à chiffrer : ")

for i in text:
    char = ord(i) + key
    if char > z:
        result+=chr(char - alphabet_lenght)
    else:
        result+=chr(char)

print(result)
