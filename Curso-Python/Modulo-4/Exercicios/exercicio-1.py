def borda(palavra) :
    palavralen = len(palavra)
    print("+","-" * palavralen,"+")
    print("|",palavra,"|")
    print("+","-" * palavralen,"+")

palavra = input("Digite uma palavra: ")
borda(palavra)
