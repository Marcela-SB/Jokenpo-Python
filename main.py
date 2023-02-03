import random
# É um importe de uma configuração de escolha aleatória...

x = 0
while x == 0:
  
  jogadas_possiveis = ["Pedra", "Papel", "Tesoura"]
  computador = random.choice(jogadas_possiveis)
  
  jogador = input("Digite o número de sua jogada escolhida! \n  1-Pedra, 2-Papel, 3-Tesoura \nEu escolho: ")
  
  print("\nComputador: {computador}\n")
  # Esta parte do código "{computador}" faz com que o print substitua o valor que está armazenado neste local da String...
  
  if jogador == "1" and computador == "Tesoura":
    print("Pedra vence da Tesoura!\n")
  
  elif jogador == "2" and computador == "Pedra":
    print("Papel vence da Pedra!\n")
  
  elif jogador == "3" and computador == "Papel":
    print("Tesoura vence da Papel!\n")
  
  elif jogador == "1" and computador == "Pedra":
    print("EMPATE!\n")
  
  elif jogador == "2" and computador == "Papel":
    print("EMPATE!\n")
  
  elif jogador == "3" and computador == "Tesoura":
    print("EMPATE!\n")
  
  else:
    print("VOCÊ PERDEU!\n")

  print("------------------------------------\n")
