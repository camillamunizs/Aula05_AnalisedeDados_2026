nota_final = float(input('Informe a nota final: '))
frequencia = float(input('Informe frequencia: '))
mensalidade = 1500



if nota_final >= 7 and frequencia >= 75:
    bolsa = mensalidade * 0.20
    print(f'Sua mensalidade é R$ {mensalidade:.2f} \nParabéns! Você ganhou uma bolsa de R$ {bolsa:.2f}')

else:
    print(f'Não tem direito a bolsa!')
