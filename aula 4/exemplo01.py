# ex01
# uma instituicao de ensino precisa calcular a media bimestral dos alunos.
# a avaliacao é composta por teste e prova. 
# crie um algoritmo que solicie as duas notas ao usuario, calcule a media e imprima o resultado 

teste = float (input('insira a nota do teste: '))
prova = float (input('insira a nota da prova: '))


soma_teste_prova = teste + prova
media_bimestre = soma_teste_prova  / 2 

print(f'nota final do bimestre: {media_bimestre}')

