lanche= 'hamburguer', 'refri', 'pizza', 'pudim'

#Sorted igual a ordenado/ordem = coloca em ordem algabetica
print(sorted(lanche))
print(lanche)

#OUTRA IDEIA:
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a+b #Ela junta, pois ficam como "strings" e não como números inteiros
print(c)
print(c.count(5)) #Quantas vezes o número 5 aparece dentro de c
print(c.index(8, 1)) #Em que posição está o 8 a partir da posição 1

#Outra coisa com tuplas
pessoa = ('Gustavo', 39, 'M', 99.88) #Pode ter numeros e letras dentro das tuplas
del pessoa #APAGA A TUPLA INTEIRA
