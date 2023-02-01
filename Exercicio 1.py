import re

def limpar_modalidades(modalidades):

    pattern = r"[^a-zA-Z0-9 ]"
    
    modalidades_limpas = [re.sub(pattern, "", mod) for mod in modalidades]
    
    return modalidades_limpas

# Exemplo de uso
modalidades = ["DINHEIRO.", ".A VISTA,", "PARCELADO-", "DBT%", "CRÉDITO A VISTA", "DH.", "CREDITO PARCELADO%"]
modalidades_limpas = limpar_modalidades(modalidades)


print(modalidades_limpas)