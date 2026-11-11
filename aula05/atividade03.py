compra = float(input('Valor da Compra: '))
cliente_frequente = input('Programa de Fidelidade? [S/N]: ').lower()[0]
print(cliente_frequente)

FRETE = 25



if compra > 200 or cliente_frequente == 's':
    print(f'Parabéns! Você ganhou frete grátis! \nValor da compra: R$ {compra:.2f} ')
else:
    valor_final = compra + FRETE
    print(f'Valor da compra: R$ {valor_final:.2f}')