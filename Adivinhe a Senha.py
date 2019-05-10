import random  ## import o modulo random que sera usado na funcao abaixo

senha = ""  ## a variavel senha comeca vazia e depois sera preenchida 
num = 5  ## a variavel num auxilia o while abaixo
while num > 0:
    sorteio = random.randint(0, 9)## e usado o randit do modulo random para sotear os numeros                       
    senha = str(sorteio) + str(senha)                 
    num = num - 1                                                     ## o while sorteia a senha

tentativas = 10  ## as duas variaveis auxiliam os comandos abaixo
resultado = []
while tentativas > 0:
    senhaFornecida = input("Digite uma senha numérica de 5 dígitos: ")
    while len(senhaFornecida) != 5:         ## o primeiro e segundo while pede ao usuario que tente adivinhar a senha e limita o usuario para que se possa digitar somente 5 caracteres
        senhaFornecida = input("Digite uma senha numérica de 5 dígitos: ")
    for i in range(len(senhaFornecida)):
        if senhaFornecida[i] in senha:                  
            if senhaFornecida[i] == senha[i]:         ## o for e in mostram ao usuario as dicas para que seja mais possivel o acerto da senha como o -1, 1 e 0
                resultado.append(1)
            else:
                resultado.append(-1)
        else:
            resultado.append(0)
    print(resultado)
    if (resultado[0]) != '1' and (resultado[1]) != '1' and (resultado[2]) != '1' and \
        (resultado[3]) != '1' and (resultado[4]) != '1':
        tentativas = tentativas - 1                                                                                       
        if tentativas == 0:                          ## os ifs indicam o numero de chances que o usuario ainda tem, mostra quando o usuario acertou a senha e também mostra quando as chances acabam e faz a saida do programa
            print("Suas chances acabaram!")                        
        else:
            print("Continue Tentando. Você ainda tem %d chances" % tentativas)
        resultado = []
    elif (resultado[0]) == '1' and (resultado[1]) == '1' and (resultado[2]) == '1' and \
        (resultado[3]) == '1' and (resultado[4]) == '1':
        print("Você acertou! A senha era %s" % senha)
        tentativas = 0

print("Saindo...")
