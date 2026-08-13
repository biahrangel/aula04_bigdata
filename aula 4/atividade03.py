#bonus por vendas

#uma empresa oferece um bonus aos funcionarios de acordo com o valor de suas vendas no mes.
#crie um algoritmo qe solicite o salario e o valor das vendas e informe o salario final de acordo com o desempenho

# considere que
# a partir de 5000 em vendas, o funcionario recebe um bonus de 500
# a partir de 3000 em vendas, o funcionario recebe bonus de 250
# abaixo de 3000 em vendas, nao ha bonus 

salario = float (input('Qual o salario? R$'))
vendas = float (input('vendas: '))

if vendas >= 5000:
    salario += 500
    print (f'o total do seu salario sera: R$ {salario}')

elif vendas >= 3000:
    salario += 250
    print (f'o total do seu salario sera: R$ {salario}')

else:
    print(f'voce nao tera bonus! seu salario sera: R$ {salario}')
