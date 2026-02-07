expressao= str(input('Digíte alguma expressão:'))
pilha= []
for simb in expressao:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha)>0: # Tem algum prato (parêntese aberto) na pilha?
            pilha.pop() # "Beleza! Achei o par de quem abriu. Vou tirar o prato da pilha."
        else:
            pilha.append(')') # "Eita! Fechei um parêntese mas não tinha nenhum aberto!"
            break  # "Erro fatal! Pode parar tudo, a expressão já está errada."
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')