class Calculadora:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def soma(self):
        return self.a + self.b

    def subtracao(self):
        return self.a - self.b

    def multiplicacao(self):
        return self.a * self.b

    def divisao(self):
        return self.a / self.b
    
    #def divisao(a, b):
    #    return a - b

calculadora = Calculadora(10, 2)
print(calculadora.b)
print(calculadora.soma())
print(calculadora.subtracao())
print(calculadora.divisao())
print(calculadora.multiplicacao())