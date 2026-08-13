# uma empresa possui uma politica de reajuste salarial de acordo com o setor e o tempo de casa do funcionario. 
# crie um algoritmo que solicite o tempo de casa, o salario e o setor do funcionario e calculo o novo salario.

#considere que: 
# funcionarios do setor A com pelo menos 3 anos de empresa recebem reajuste de 18%
# os demais recebem reajuste de 9%

#ao final informe o valor do aumnto, percentual de reajuste e o salario reajustado 

tempo = float (input('tempo de casa: '))
salario = float (input('salario: '))
setor = (input('setor: ')).upper()

if setor == 'A' and tempo >= 3: 
    aumento = salario * 0.18

else:
    aumento = salario * 0.09

novo_salario = salario + aumento

print('\n===========RESULTADO===========')
print(f'aumento de {salario}')
print(f'salario reajustado: {novo_salario}')
