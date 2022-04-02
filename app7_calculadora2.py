class Calculadora:
        
    def soma(self, a , b):
        return a + b

    def subtracao(self, a , b):
        return a - b
    
    def multiplicacao(self, a , b):
        return a * b
    
    def divisao(self, a , b):
        return a / b
    
    #def divisao(a, b):
    #    return a - b

calculadora = Calculadora()
print(calculadora.soma(10, 2))
print(calculadora.subtracao(5, 3))
print(calculadora.divisao(100, 2))
print(calculadora.multiplicacao(10 , 5))