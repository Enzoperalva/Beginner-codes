lista= []
alunos= dict()
def notas(*notas, sit=False):
    """
    -> FUnção para analisar notas e situações de vários alunos
    :param notas: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    if sit:
        lista.append(notas)
        alunos['total'] = (len(notas))
        alunos['maior'] = max(max(lista))
        alunos['menor'] = min(min(lista))
        alunos['média'] = (sum(max(lista))) / len(notas)
        if alunos['média'] >=7:
            alunos['situação'] = 'BOA'
        elif 6 <= alunos['média'] <7:
            alunos['situação'] = 'RAZOÁVEL'
        else:
            alunos['situação'] = 'RUIM'
    else:
        lista.append(notas)
        alunos['total'] = (len(notas))
        alunos['maior'] = max(max(lista))
        alunos['menor'] = min(min(lista))
        alunos['média'] = (sum(max(lista))) / len(notas)


notas(3.5, 2, 6.5, 2, 7, 4)
print(alunos)
help(notas)

#Resolução Guanabara
def notas(*n, sit=False):
    """
    -> FUnção para analisar notas e situações de vários alunos
    :param notas: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    r= dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


resp = notas(5.5, 2.5, 8.5, sit=True)
print(resp)
help(notas)