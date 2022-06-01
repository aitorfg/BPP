lista = [3,4,8,5,5,22,13]

def es_primo(num):
        cont = 0
        for i in range(1,num):
            if(num%i==0):
                cont+=1
                if cont > 1:
                    return False
        return True
         
primos = list(filter(es_primo, lista))
print("Los números primos de la lista son: ", primos)