numero = float(input('Digite um número: '))

match numero:
    case numero if numero > 0:
        print(f'{numero}O número é positivo')

    case numero if numero < 0:
        print(f'{numero} O número é negativo')

    case 0:
        print(f'{numero} O número é zero')