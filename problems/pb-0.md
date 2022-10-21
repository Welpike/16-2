## Erreur rencontree : 

>Traceback (most recent call last):  
>&nbsp;&nbsp;File "<string>", line 178, in run_nodebug  
>&nbsp;&nbsp;File "<module1>", line 17, in <module>  
>TypeError: unsupported operand type(s) for +=: 'int' and 'str'  
  
## code

for i in range(len(hexa)):  
&nbsp;&nbsp;&nbsp;&nbsp;char = hexa[i]  
&nbsp;&nbsp;&nbsp;&nbsp;print(char)  
&nbsp;&nbsp;&nbsp;&nbsp;print(i)  
&nbsp;&nbsp;&nbsp;&nbsp;if char in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hex_to_dec += char * 16**i # here  
&nbsp;&nbsp;&nbsp;&nbsp;elif char in ["A", "B", "C", "D", "E", "F"]:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if char == "A":  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hex_to_dec += 10 * 16**i  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;elif char == "B":  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hex_to_dec += 11 * 16**i  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;elif char == "C":  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hex_to_dec += 12 * 16**i  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;elif char == "D":  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hex_to_dec += 13 * 16**i  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;elif char == "E":  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hex_to_dec += 14 * 16**i  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;elif char == "F":  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hex_to_dec += 15 * 16**i  
    
Il s'agissait d'un conflit entre deux types de variables.  
En effet, __char__ est str et on a essayé d'ajouter des éléments de type int.  

## code réparé
  
for i in range(len(hexa)):  
&nbsp;&nbsp;&nbsp;&nbsp;char = hexa[i]  
&nbsp;&nbsp;&nbsp;&nbsp;print(char)  
&nbsp;&nbsp;&nbsp;&nbsp;if char in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hex_to_dec += int(char) * 16**i  
&nbsp;&nbsp;&nbsp;&nbsp;elif char in ["A", "B", "C", "D", "E", "F"]:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if char == "A":  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hex_to_dec += 10 * 16**i  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;elif char == "B":  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hex_to_dec += 11 * 16**i  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;elif char == "C":  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hex_to_dec += 12 * 16**i  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;elif char == "D":  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hex_to_dec += 13 * 16**i  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;elif char == "E":  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hex_to_dec += 14 * 16**i  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;elif char == "F":  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hex_to_dec += 15 * 16**i  
 
## N.B : nous avons procédé à un changement important de la structure du code depuis.
  
