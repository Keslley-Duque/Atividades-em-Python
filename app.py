print("meu primeiro programa em Python")

a = int(input("Digite o primeiro valor"))
b = int(input("Digite o segundo valor"))

soma = a + b
print('soma: ' + str(soma))

sub = a - b
print('subtração: ' + str(sub))

div = a/b
print('divisão: ' + str(div))

mult = a * b
print('multiplicação: ' + str(mult))

rest = a % b
print('resto: ' + str(rest))

print('\nsoma: {}. subtração: {}. divisão: {}. multiplicação: {}. resto: {}.'.format(soma,sub,div,mult,rest))