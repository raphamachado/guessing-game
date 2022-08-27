def jogar():
  #jogo de advinhação
  print('*********************************')
  print('***Bem-vindo ao jogo da forca!***')
  print('*********************************')

  number=12
  tentativas=0
  acertou=False

  dificuldade_input=int(input("Escolha o nível de dificuldade: \n 1 (20 tentativas) \n 2 (10 tentativas) \n 3 (5 tentativas)"))

  if dificuldade_input==1:
    max_tentativas = 20
  if dificuldade_input==2:
    max_tentativas = 10
  elif dificuldade_input==3:
    max_tentativas = 5

  while (acertou==False and tentativas<max_tentativas):
  
    number_input=int(input("Digite um número \n"))
    tentativas+=1

    acertou=number_input==number
    maior=number_input>number
    menor=number_input<number

    if acertou:
      print("Você acertou!")
      print("Tentativas totais {}".format(str(tentativas)))
    elif menor:
      print("Você errou! O chute foi menor que o número secreto")
      print("Restam {} tentativas".format(str(max_tentativas-tentativas)))
    elif maior:
      print("Você errou! O chute foi maior que o número secreto")
      print("Restam {} tentativas".format(str(max_tentativas-tentativas)))

  print("Fim do Jogo")

jogar()