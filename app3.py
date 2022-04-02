a = int(input('Primeira nota: '))
if a > 10:
    a = int(input('Voce digitou errado! Primeira nota: '))
b = int(input('Segunda nota: '))
if b > 10:
    b = int(input('Voce digitou errado! Segunda nota: '))
c = int(input('Terceira nota: '))
if c > 10:
    c = int(input('Voce digitou errado! Terceiro nota: '))
d = int(input('Quarta nota: '))
if d > 10:
    d = int(input('Voce digitou errado! Quarta nota: '))

media = (a + b + c + d)/4
print('Media: {}'.format(media))
#if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#    print('media: {}'.format(media))
#else:
#    print('Alguma nota foi digitada de forma errada!')    