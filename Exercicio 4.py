#exercicio 4:
import re
def media_mediana():
    numeros = input("Escreva seus numeros separando com uma virgula: ").split(",")
    numeros = [int(num) for num in numeros]
    numeros.sort()
    tamanho = len(numeros)
    media = sum(numeros) / tamanho
    if tamanho % 2 == 0:
        mediana = (numeros[tamanho//2] + numeros[tamanho//2 - 1]) / 2
    else:
        mediana = numeros[tamanho//2]
    return media, mediana, numeros


media, mediana, numeros = media_mediana()
print("Média:", media)
print("Mediana:", mediana)
