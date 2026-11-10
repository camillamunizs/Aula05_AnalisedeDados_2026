valor_do_pedido = float(input('Informe o valor do pedido: R$  '))
distancia = float(input('Informe a distância: '))
frete = 8

if valor_do_pedido > 50 and distancia <= 3:
    valor_final =  valor_do_pedido
    print(f'Oba! Você ganhou frete grátis! ')

else: 
    valor_final = valor_do_pedido + 8
    print(f'Frete de R$ {frete}')
    print(f'Valor final: R$ {valor_final:.2f}')

