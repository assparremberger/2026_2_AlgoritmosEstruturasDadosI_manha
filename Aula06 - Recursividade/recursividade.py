#Função recursiva para somar valores de 1 até o valor informado
def somarAte( n ):
    if n < 1:
        print("Valor não permitido")
        return
    if n == 1:
        return 1
    else:
        return n + somarAte( n - 1 )

def somaPares( n ):
    if n <= 1 :
        return 0
    elif n % 2 == 1:
        return somaPares( n - 1 )
    else:
        return n + somaPares( n - 2 )

def fat( n ):
    if n == 1:
        return 1
    else:
        return n * fat( n-1 )
    
n = int( input("Digite um número: "))
print( "A soma dos pares de 1 até ", n, " é: ", somaPares( n ) )
print( "A soma de 1 até ", n, " é: ", somarAte( n ) )
print( "O fatorial de ", n, " é: ", fat( n ) )

# 1) Implemente uma função recursiva para cálculo de potência
def potencia(base, expoente):
    if expoente == 0:
        return 1
    return base * potencia( base, (expoente-1) )
print( "2 elevado ao expoente ", n , " é: " , potencia(2, n) )

# 2) Implemente um contador regressivo utilizando recursividade
import time
def regressiva( n ):
    time.sleep( 1 )
    if n == 0:
        print("Fim!")
    else:
        print( n, end=" - ", flush=True )
        regressiva( n - 1 )
print("----------------------------")
regressiva(n)

# 3) Implemente uma função recursiva para inverter uma string
# f( "bola" ) -> alob
def inverterString( txt ):
    if len( txt ) == 1:
        return txt
    else:
        return inverterString( txt[ 1 : ] ) + txt[0]
    
texto = input("Digite uma palavra: ")
print( inverterString(texto))

#4) monte uma função que retur tru se a string informada for um palíndromo
def isPalindromo( txt ):
    txt = txt.upper()
    txtInvertido = inverterString( txt )
    if txt == txtInvertido:
        return True
    return False

if isPalindromo( texto ):
    print( texto , " é um palíndromo")
else:
    print( texto , " não é um palíndromo")