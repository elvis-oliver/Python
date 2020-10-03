resp = {}

def notas(* num, seq=False):
    '''
    notas(* num, seq=False)
        -> Função para retornar notas, média e situação de alunos
        :param num: uma ou mais notas do aluno
        :param seq: situação do aluno
        :return: retorna o resultado dentro de um dicionario
    '''
    global resp
    contN = 0
    maior = menor = media = 0
    for i, e in enumerate(num):
        if i == 0:
            maior = e
            menor = e
        if e > maior:
            maior = e
        if e < menor:
            menor = e
        contN += e
        media = contN / len(num)
    if media < 3:
        sit = 'REPROVADO'
    elif media < 7:
        sit = 'RECUPERAÇÃO'
    else:
        sit = 'APROVADO'
    if seq:
        return {'maior': maior, 'menor': menor, 'total': contN, 'média': media, 'situação': sit}
    else:
        return {'maior': maior, 'menor': menor, 'total': contN, 'média': media}
# PROGRAMA PRINCIPAL

resp = notas(7, 6, 7, 6, seq=True)
print(resp)
help(notas)