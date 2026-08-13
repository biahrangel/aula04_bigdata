# ex 02

# uma plataforma de recompensas utiliza uma pontuacao para avaliar o desempenho dos participantes.
# crie um algoritmo que solicite a pontuacao do participante, e de acordo com os pontos obtidos, 
# informe seus desempenho e acrescente um bonus de pontuacao. 

# considere: 
# a partir de 100 pontos, o bonus é de 10 pontos
# a partir de 50 pontos, o bonus é de 5
# abaixo de 50 pontos, nao ha bonus 

pontos = int (input('informe os pontos: '))

if pontos >= 100:
    total_pontos = pontos + 10
    print(f'excelente! voce tem {total_pontos} pontos')

elif pontos >= 50: 
    total_pontos = pontos + 5
    print(f"parabens! seu total de pontos: {total_pontos}")

else: 
    print(f'voce nao tera bonus. Voce tem {pontos} pontos')
