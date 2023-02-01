import requests

def extrai_dados_venda(url):

    #Resquest do link 
    response = requests.get(url)
    dados = response.text

    #formata tabela em variavel separando linhas
    linhas = dados.split("\n")

    valores_venda = []
    parcelas = []

    #laço
    for linha in linhas:
        if linha.startswith("1"):
            valor_venda = float(linha[84:95])
            valores_venda.append(valor_venda)

            
            qtd_parcelas = int(linha[172:175])
            parcelas.append(qtd_parcelas)

    return valores_venda, parcelas

url = "https://raw.githubusercontent.com/f360-dev/provas/master/ExtratoEletronicoGetNet.txt"
valores_venda, parcelas = extrai_dados_venda(url)
print("Valores de venda:", valores_venda)
print("Parcelas:", parcelas)
