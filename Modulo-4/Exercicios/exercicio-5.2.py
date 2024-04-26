
# ! Versão 2 da resposta
# ! Fatorial 
def fatorial(numero) :
    resultado = 1
    for cont in range (1, numero, +1) :
        resultado += resultado * cont
    return resultado

# ! Verificação Positivo
def positivo(numero) :
    if (numero < 0) :
        numero = int(input("Digite um número: "))
        while (numero < 0) :
            numero = int(input("Digite um número: "))
        return numero
    

# ! Chamadas
numero = int(input("Digite um número: ")) # ! Pede p/ digitar o número
verificarPositivo = positivo(numero)      # ! Verifica se o número é positivo, 
                                          # ! enquanto não for pede para continuar digitando
resultadoFatorial = fatorial(numero)      # ! Calcula o fatorial do número
print(f"{resultadoFatorial}")             # ! Exibe o resultado
