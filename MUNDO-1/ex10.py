# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

din_total = float(input("Informe quanto dinheiro você tem na sua carteira: R$: "))
dolar_hoje = 5.66

dol_valor = din_total / dolar_hoje

print("Sabendo que o dólar atual está no valor de R${}. O total de dólares que você pode comprar com R${} reais é R${:.2f} dólares".format(dolar_hoje, din_total, dol_valor ))