#Que os jogos comecem :-)

#"bibliotecas" auxiliares...
import sys

# Constantes:
DELAY_TIME = 5000
NEW_ROUND = 200.00
INITIAL_MONEY = 2500.00

# ---------------------------------------------------------------------  Funcoes auxiliares --------------------------------------------------------#

def print_help():
	print ("----------   Welcome to the Pororoca's helper  ----------")
	print ("----                                                 ----")
	print ("----    'help'   : show this guide                   ----")
	print ("----    '0'	 : show this guide                   ----")
	print ("----    '1'	 : buy some property of the bank     ----")
	print ("----    '2'	 : sell some property to the bank    ----")
	print ("----    '3'	 : buy some property of any player   ----")
	print ("----    '4'	 : sell some property to any player  ----")
	print ("----                                                 ----")
	print ("---------------------------------------------------------")


# funcao que printa o acrescimo de dinheiro
def print_money (value, who):
	print (who,"Saldo: R$ ", value, end="\r")

# funcao responsavel por esperar um tempo...
def delay(value):
	for j in range (value):
		pass
		

# Something like a struct in C.. here we set a list with the name of the players and them money
class players:
	name = list()
	money = list()

def print_saldo_de_todos(turn, num_players):

	# DEPOIS.. TENTAR PRINTAR COLORIDO ESSE CARA...
	print (players.name[turn], "\t: R$ ", players.money[turn]) 

	for i in range(num_players):
		if i != turn:
			print (players.name[i], "\t: R$ ", players.money[i])


def show_the_Winner():
	pass



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
	 delay(DELAY_TIME * 500)
print ()

for i in range (101):
	print ("Criando contas bancarias para os jogadores...   ", i, "%", end="\r")
	delay(DELAY_TIME * 500)
print ()

# ---------------------------------------------------------		 loop of the game 	 -----------------------------------------------------------------#
NEXT_ROUND = True

while NEXT_ROUND:
	turn = 0	# Primeira jogada, ou nova rodada.

	while turn < num_players: #	Realiza uma rodada

		print_saldo_de_todos(turn, num_players)

		print (players.name[turn], ", qual a sua jogada?")

		actions = input()		#captura o que ocorre na determinada rodada

# -------------------------------------------------------- Seleciona e direciona uma acao... criar funcoes para cada acao ---------------------------#
		if actions == 'help' or actions == '0':
			print_help()
		elif actions == 'quit' or actions == '666':
			if turn != num_players - 1:
				finish_the_game = input('A rodada ainda nao acabou. Deseja realmente terminar o jogo? sim ou nao?\n')
				if finish_the_game == 'sim':
					NEXT_ROUND = False
					break
				elif finish_the_game == 'nao':
					NEXT_ROUND = False
			else: NEXT_ROUND = False

#--------------------------------------------------------- apenas uns testes... ---------------------------------------------------------------------#
		dinheiros= 5000.00
		value = 20000

		for i in range(0,value):
			 print_money (players.money[turn] + i, players.name[turn])
			 delay (DELAY_TIME)

		players.money[turn]+= value
		print (players.name[turn],"Saldo: R$ ", players.money[turn])


		print ('\n')
		turn = turn + 1 #  proximo 

show_the_Winner()