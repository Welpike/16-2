## Erreur rencontree : 

>Traceback (most recent call last):
>  File "<string>", line 178, in run_nodebug
>  File "<module1>", line 17, in <module>
>TypeError: unsupported operand type(s) for +=: 'int' and 'str'
  
## code

for i in range(len(hexa)):
    char = hexa[i]
    print(char)
    print(i)
    if char in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        hex_to_dec += char * 16**i # here
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
  
Il s'agissait d'un conflit entre deux types de variables.
En effet, __char__ est <str> et on a essayé d'ajouter des éléments de type <int>.

## code réparé
  
for i in range(len(hexa)):
    char = hexa[i]
    print(char)
    print(i)
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
