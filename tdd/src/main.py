import math as m
class iniciar:
    def login(username,password):
        if((username=="hradmin")and(password=="hrtest")):
            return True
        else:
            return False


class validar:
    def comprobar(numero):
        while numero == str(numero):
            try:
                return False
            except:
                pass
        return numero


class calcular():
    def logaritmo(numero):
        return m.log10(numero)
    
    def cubo(numero):
        return numero * numero * numero

    def k(numero):
        numero = 1+3.332*m.log10(numero)
        if(int(numero) % 2 ==0 ):
            numero += 1
        elif(int(numero) % 2==1):
            numero = 1
        else:
            numero -= 1

        return int(numero)
    
    def factorial(numero):
        for i in range(1,numero):
            numero *= i
        return numero
