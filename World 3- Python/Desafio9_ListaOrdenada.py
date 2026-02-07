valores = [] #Você cria uma fila vazia.
for c in range(0, 5): #Você vai chamar 5 pessoas (uma de cada vez) para entrar na fila.
    n1= int(input(f'Digite um valor na posição {c}: ')) #Você pergunta a altura da pessoa que acabou de chegar.
    if c == 0  or n1 > valores[-1]: #Você é a primeira pessoa da fila? Você é mais alto que a última pessoa que entrou na fila?
        valores.append(n1) #Se a resposta for SIM para qualquer uma dessas perguntas, a pessoa vai direto para o final da fila: valores.append(n1) (O append sempre joga para o final).
    else: #Se a pessoa não for a primeira e não for a mais alta de todas, ela precisa ser encaixada em algum lugar no meio da fila. É aqui que o bicho pega:
        pos=0 #Começamos a olhar a fila desde o primeiro lugar (posição 0)
        while pos<len(valores): #Enquanto não percorrermos a fila toda...
            if n1<= valores[pos]: #Você é menor ou igual à pessoa que está nesta posição?
                valores.insert(pos,n1) #Beleza, então entra aqui na frente dela!
                break #Já achei seu lugar, pode parar de procurar.
            pos+=1 #Não é aqui? Vamos olhar a próxima posição...
print('=-'*20)
print(f'Oa valores digitados em ordem: {valores}')