#Que os jogos comecem :-)

# ---------------------------------------------------------------- IDEIAIS -------------------------------------------------------------------------- #

#Implementar alguma coisa caso a pessoa aperte o numero errado
#Implementar uma senha para cada jogador? Assim evitamos equivocos de nome de jogador.. e nao precisamos ficar confirmando nomes a todo momento
#Implementar um modo root? para poder intervir em qualquer jogador e ter acesso as contas bancarias, para alterar qualquer cagada durante o jogo 
#Lembrar dos sorte ou reves que afetam mais de um jogador
#Devemos inserir o Banco com dinheiro finito?
#Tentar implementar, nas trocas de dinheiros com jogadores, os prints simultaneos de dinheiro aumentando e diminuindo

# ----------------------------------------------------------------------------------------------------------------------------------------------------#

#"bibliotecas" auxiliares...
import sys
import os


# Constantes:
DELAY_TIME = 300000
LAP_PRIZE = 200.00
INITIAL_MONEY = 2500.00
POSITIVE = True

# ---------------------------------------------------------------------  Funcoes auxiliares --------------------------------------------------------#

def print_help():
	print ("----------   Welcome to the Pororoca's helper  ----------")
	print ("----                                                 ----")
	print ("----    'help'   : show this guide                   ----")
	print ("----    '0'	 : show this guide                   ----")
	print ("----    '1'	 : buy something of the bank         ----")
	print ("----    '2'	 : sell something to the bank        ----")
	print ("----    '3'	 : buy something of any player       ----")
	print ("----    '4'	 : sell something to any player      ----")
#	print ("----    '5'	 : pay  something to any player      ----")
	print ("----                                                 ----")
	print ("---------------------------------------------------------")


# funcao que printa o acrescimo de dinheiro
def print_money (value, who, value_positve):
	if value_positve:
		for i in range(value +1):
			print (players.name[who],"Saldo: R$ ", players.money[who] +i, end="\r")
			delay (DELAY_TIME)
	else :
		for j in range(value + 1):	
			print (players.name[who],"Saldo: R$ ", players.money[who] -j, end="\r")
			delay (DELAY_TIME)
	print('\n')


# funcao responsavel por esperar um tempo...
def delay(value):
	for j in range (value):
		pass
		
def clear_terminal():
	os.system('cls' if os.name == 'nt' else 'clear')

# Something like a struct in C.. here we set a list with the name of the players and them money
class players:
	name = list()
	money = list()

def print_saldo_de_todos(turn, num_players):

	# DEPOIS.. TENTAR PRINTAR COLORIDO ESSE CARA...
	print ("\033[32m",players.name[turn], "\t: R$ ", players.money[turn], "\033[0;0m") 

	for i in range(num_players):
		if i != turn:
			print ("",players.name[i], "\t: R$ ", players.money[i])
	print()

def buy_something_bank(turn):
	price = int(input('Qual o valor da sua compra ou divida?\n'))
	print_money(price, turn, not(POSITIVE))
	players.money[turn]-= price

def sell_something_bank(turn):
	price = int(input('Qual o valor de seu premio ou hipoteca?\n'))
	print_money(price, turn, POSITIVE)
	players.money[turn] += price

def buy_something_players(turn, num_target):
	price = int(input('Qual o valor da compra?\n'))
	print_money(price, turn, not(POSITIVE))
	print_money(price,num_target, POSITIVE)
	players.money[turn]-= price
	players.money[num_target]+= price

def sell_something_players(turn,num_target):
	price = int(input('Qual o valor da venda?\n'))
	print_money(price, turn, POSITIVE)
	print_money(price,num_target, not(POSITIVE))
	players.money[turn]+= price
	players.money[num_target]-= price

def show_the_Winner(num_players):
	max_money = max(players.money)
	winner_index = players.money.index(max_money)
	empate = False
	for i in range(num_players):
		if i != winner_index and players.money[i] == max_money:
			empate = True
			winner_index_2 = i
	if empate:
		print ("Os jogadores ", players.name[winner_index], "e ", players.name[winner_index_2], "empataram com R$ ", players.money[winner_index])
	else:
		print ("\tTemos que o Vencedor eh: ", players.name[winner_index], "com R$ ", players.money[winner_index])
	
	print_saldo_de_todos(winner_index, num_players)
	



# --------------------------------------------------------- Inicio de fato do programa ----------------------------------------------------------------#
# ---------------------------------------------------------		 Inicializacoes 	 ------------------------------------------------------------------#

#Iniciamos o programa capturando n players ..
num_players = int(input('Insira o numero de jogadores. (maximo 6)\n'))

if num_players == 0 or num_players == 1:
	print ('Joga sozinho ai.. otario (a)')
	exit()

# permite ate 6 players
while (num_players > 6) :
	num_players = int(input('Erro, Excesso de players. Insira novamente\n'))


for i in range(num_players):
	print ("\tInsira o nome do jogador", i +1)		#coloquei esse +1 para printar jogador 1, ao inves de jogador 0
	players.name.append(input())
	players.money.append(INITIAL_MONEY)				# insere o dinheiro inicial na conta de cada jogador
	print ()

if len(players.name) > num_players:
	print ("Ja deu merda, Ja deu merdaaa")
	exit()
 
for i in range (101):
	 print ("Armazenando as informacoes em nosso banco de dados: ", i, "%", end="\r")
	 delay(DELAY_TIME * 8)
print ()

for i in range (101):
	print ("Criando contas bancarias para os jogadores...   ", i, "%", end="\r")
	delay(DELAY_TIME * 8)
print ("\n")
input('Ok! Tudo Pronto. Pressione "Enter" para continuar.')



# ---------------------------------------------------------		 loop of the game 	 -----------------------------------------------------------------#

NEXT_ROUND = True

while NEXT_ROUND:
	turn = 0	# Primeira jogada, ou nova rodada.

	while turn < num_players: #	Realiza uma rodada

		clear_terminal()

		print_saldo_de_todos(turn, num_players)

		print (players.name[turn], ", qual a sua jogada?")
		actions = input()		#captura o que ocorre na determinada rodada

# -------------------------------------------------------- Seleciona e direciona uma acao... criar funcoes para cada acao ---------------------------#

		while actions != '':
			
			if actions == 'help' or actions == '0':
				print_help()
				actions = input('Agora, realize sua jogada\n')

			elif actions == '1':
				buy_something_bank(turn)
				actions = input('Algo mais? Pressione "Enter" para concluir a jogada\n')

			elif actions == '2':
				sell_something_bank(turn)
				actions = input('Algo mais? Pressione "Enter" para concluir a jogada\n')

			elif actions == '3':
				target = input('Quem vai vender?\n')
				while target == players.name[turn] or not(target in players.name):
					if target == players.name[turn]:
						target = input('Nao insira seu nome neh -.-" ... Tente novamente\n')
					else : 
						target = input ('Nome nao encontrado. Por favor, verifique e, entao, tente novamente\n')
				num_target = players.name.index(target)
				buy_something_players (turn, num_target)
				actions = input('Algo mais? Pressione "Enter" para concluir a jogada\n')
			
			elif actions == '4':
				target = input('Quem vai comprar?\n')
				while target == players.name[turn] or not(target in players.name):
					if target == players.name[turn]:
						target = input('Nao insira seu nome neh -.-" ... Tente novamente\n')
					else :
						target = input ('Nome nao encontrado. Por favor, verifique e, entao, tente novamente\n')	
				num_target = players.name.index(target)
				sell_something_players(turn, num_target)
				actions = input('Algo mais? Pressione "Enter" para concluir a jogada\n')
			
			elif actions == 'quit' or actions == '666':
				if turn != num_players - 1:
					finish_the_game = input('A rodada ainda nao acabou. Deseja realmente terminar o jogo? sim ou nao?\n')
					if finish_the_game == 'sim':
						NEXT_ROUND = False
						break
					elif finish_the_game == 'nao':
						NEXT_ROUND = False
				else: NEXT_ROUND = False
			else:
				print ("operacao invalida. Digite 'help' para visualizar as operacoes validas e, entao, tente novamente.")
				actions = input()		#captura o que ocorre na determinada rodada

		if not(NEXT_ROUND):
			break

		turn = turn + 1 #  proximo turno

show_the_Winner(num_players)