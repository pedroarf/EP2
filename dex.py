print ("Ola! Seja Bem Vindo ao Inspèrmon")
Inspèrdex = {"Blastoise": {"Poder de Ataque": 20,"Nível de Defesa": 10,"Pontos de Vida": 120},
			"Charizard": {"Poder de Ataque": 25,"Nível de Defesa": 8,"Pontos de Vida": 120},
			"Alakazam": {"Poder de Ataque": 15,"Nível de Defesa": 20,"Pontos de Vida": 120},
			"Gyarados": {"Poder de Ataque": 25,"Nível de Defesa": 15,"Pontos de Vida": 120},
			"Snorlax": {"Poder de Ataque": 22,"Nível de Defesa": 20,"Pontos de Vida": 120},
			"Dragonite": {"Poder de Ataque": 30,"Nível de Defesa": 15,"Pontos de Vida": 120},
			"Bulbasaur": {"Poder de Ataque": 10,"Nível de Defesa": 15,"Pontos de Vida": 120},
			"Pikachu": {"Poder de Ataque": 15,"Nível de Defesa": 15,"Pontos de Vida": 120},
			"Ninetales": {"Poder de Ataque": 20,"Nível de Defesa": 10,"Pontos de Vida": 120},
			"Arcanine": {"Poder de Ataque":18,"Nível de Defesa": 23,"Pontos de Vida": 120}}
print ("Veja Abaixo os Inspèrmons disponíveis:")
disp = "Blastoise","Charizard","Alakazam","Gyarados","Snorlax","Dragonite","Bulbasaur","Pikachu","Ninetales","Arcanine"
print (disp)
perg = input ("Você deseja saber os atributos de algum? Basta digitar seu nome! ")
print (Inspèrdex[perg])
pergu = input ("Se você deseja saber os atributos de mais algum digite seu nome! Se não digite GO para continuar: ")
GO = 1
if pergu == 1:
	primeiro = input("Então agora escolha o seu Inspérmon inicial dentre um dos apresentados: ")
#procurar alguma ideia para ver todos possiveis ou algo do tipo
if pergu !=1:
	print (Inspèrdex[pergu])
primeiro = input("Agora que você já viu as opções escolha o seu Inspérmon inicial dentre um dos apresentados: ")
print ("Ótima escolha! Agora é hora de iniciar a aventura!")
a1 = input ("O que você deseja fazer com seu pokémon? Dormir (2) ou Passear(3): ")
if a1 ==2:
	print ("Certo! Então é hora de descansar")
if a1 !=2:
	print ("Empolgante! Vamos passear pelo campus do Inspèrmon!")
inserir algum intervalo de tempo
b1 = input ("Nossa! Encontramos um (algum pokemon) no caminho! E agora? Você deseja fugir (4) ou batalhar (5)? ")
if b1 ==4:
	print ("Ufa!! Você conseguiu fugir depois de muito esforço!")
if b1 ==5:
	print ("Vai começar um grande desafio de batalha entre Inspèrmons! Boa Sorte!! ")
