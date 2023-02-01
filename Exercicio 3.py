def calculadora():
  valor = float(input("Digite o valor da venda: "))
  perc = float(input("Digite apenas os numero da porcentagem: "))
  tax = (valor * perc / 100)
  return valor, perc, tax

valor, perc, tax = calculadora()
print("O valor da venda foi {} reais sendo assim o porcentual de adquirente é {:.2f}%, a taxa cobrada foi de R$ {:.2f} Reais".format(valor, perc, tax))
