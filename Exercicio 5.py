#exercicio 5

def inverte_com_espaco(s):
    vogais = "aeiouAEIOU"
    nova_string = ""
    for i in range(len(s)-1, -1, -1):
        if s[i] in vogais:
            nova_string += s[i] + " "
        else:
            nova_string += s[i]
    return nova_string

string = str(input("Escreva uma palavra para o espelho refletir: "))
print(inverte_com_espaco(string))
