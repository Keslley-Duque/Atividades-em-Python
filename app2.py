a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
#c = int(input('Terceiro valor: '))

resto_a = a % 2
resto_b = b % 2

if resto_a == 0 or not resto_b > 0:
    print('Foi digitado um numero par')
else:
    print('Nenhum numero par foi digitado')

#resto = a % 2
#if resto == 0:
#    print('Numero é par')
#else:
#    print('Numero é impar')

#if a > b and a > c:
#    print('\nO maior numero eh: {}'.format(a))
#elif b > a and b > c:
#    print('\nO maior numero eh: {}'.format(b))
#else:
#    print('\nO maior numero eh: {}'.format(c))

