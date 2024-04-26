
# ! Versão 1 da resposta
# ! Fatorial 
def fatorial(numero, verificarPositivo) :
    if (verificarPositivo == True) :
        resultado = 1
        for cont in range (1, numero, +1) :
            resultado += resultado * cont
        return resultado
    else :
        resultado = "Número inválido!"
        return resultado

# ! Verificação Positivo
def positivo(numero) :
    if (numero < 0) :
        result = False
        return result
    else :
        result = True
        return result
    

# ! Chamadas
numero = int(input("Digite um número: "))                   # ! Pede p/ digitar o número
verificarPositivo = positivo(numero)                        # ! Verifica se o número é positivo
resultadoFatorial = fatorial(numero, verificarPositivo)     # ! Calcula o fatorial do número
print(f"{resultadoFatorial}")                               # ! Exibe o resultado
