compra = float(input('Valor da Compra: '))
cliente_frequente = input('Programa de Fidelidade? [S/N]: ').lower()[0]
print(cliente_frequente)



if compra > 200 or cliente_frequente == 's':
    print(f'Parabéns! Você ganhou frete grátis! \nValor da compra: R$ {compra:.2f} ')
else:
    frete = compra + 25
    print(f'Valor da compra: R$ {frete:.2f}')