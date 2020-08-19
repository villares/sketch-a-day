palavra = "Heineken"
palavra_invertida = "" # começa vazia
for letra in palavra:
    # soma letra da palavra uma por uma
    # formando string invertido
    palavra_invertida = letra + palavra_invertida
    
print(palavra_invertida)

print(reversed(palavra))