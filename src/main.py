#Que os jogos comecem :-)

#"bibliotecas" auxiliares...


# # funcao que printa o acrescimo de dinheiro


def print_money (value, who):
	print("Jogador ", who, end=" ")
	print ("Saldo: R$ ", value, end="\r")

def delay(value):
	for j in range (value):
		pass
		
		


# --------------------------------------------------------- Inicio de fato do programa ----------------------------------------------------------------#


#Iniciamos o programa capturando n jogadores ..
num_jogadores = input('Insira o numero de jogadores. (maximo 6)\n')

if num_jogadores == '0' or num_jogadores == '1':
	print ('Joga sozinho ai.. otario (a)')
	exit();

# permite ate 6 jogadores
# while (num_jogadores >= 5) :
	# num_jogadores = input('Erro, Excesso de jogadores. Insira novamente\n')

#criamos n listas, Pensar numa forma de otimizar

if num_jogadores == 2:
	jogador1 = list()
	jogador2 = list()

elif num_jogadores == 3:
	jogador1 = list()
	jogador2 = list()
	jogador3 = list()

elif num_jogadores == 4:
	jogador1 = list()
	jogador2 = list()
	jogador3 = list()
	jogador4 = list()

elif num_jogadores == 5:
	jogador1 = list()
	jogador2 = list()
	jogador3 = list()
	jogador4 = list()
	jogador5 = list()

elif num_jogadores == 6:
	jogador1 = list()
	jogador2 = list()
	jogador3 = list()
	jogador4 = list()
	jogador5 = list()
	jogador6 = list()
 
dinheiros= 5000.00
value = 20000



for i in range(0,value):
	 print_money (dinheiros + i, 1)
	 delay (5000)

print ('\n')