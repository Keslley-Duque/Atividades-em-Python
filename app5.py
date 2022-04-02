lista = [1, 3, 5, 7, 2]
lista_animal = ['cachorro', 'gato', 'papagaio', 'lobo']

lista_animal[0] = 'mamaco'
print(lista_animal)

tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(tupla[3])

print(len(tupla))
print(len(lista_animal))

tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)

#lista.sort()
#lista_animal.sort()
#print(lista)
#print(lista_animal)

#lista_animal.reverse()
#print(lista_animal)

#print(sum(lista))
#print(max(lista_animal))
#print(min(lista_animal))

#if 'lobo' in lista_animal:
#    print('Existe um lobo na lista')
#else:
#    print('Não existe na lista!')
#    lista_animal.append('lobo')
#    print(lista_animal)

#lista_animal.pop()
#print(lista_animal)    

#lista_animal.pop(2)
#print(lista_animal)

#lista_animal.remove('gato')
#print(lista_animal)


#nova_lista = lista_animal * 3
#print(nova_lista)    

#print(lista_animal[1])
#soma = 0
#for x in lista:
#    print(x)
#    soma += x
#print(soma)    