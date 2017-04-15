import random
import time
x=0
while x<1000:
	print ("Ola! Seja Bem Vindo ao Inspermon")
	Insperdex = {"Blastoise": {"Poder de Ataque": 20,"Nível de Defesa": 10,"Pontos de Vida": 120},
				"Charizard": {"Poder de Ataque": 25,"Nível de Defesa": 8,"Pontos de Vida": 120},
				"Alakazam": {"Poder de Ataque": 15,"Nível de Defesa": 20,"Pontos de Vida": 120},
				"Gyarados": {"Poder de Ataque": 25,"Nível de Defesa": 15,"Pontos de Vida": 120},
				"Snorlax": {"Poder de Ataque": 22,"Nível de Defesa": 20,"Pontos de Vida": 120},
				"Dragonite": {"Poder de Ataque": 30,"Nível de Defesa": 15,"Pontos de Vida": 120},
				"Bulbasaur": {"Poder de Ataque": 10,"Nível de Defesa": 15,"Pontos de Vida": 120},
				"Pikachu": {"Poder de Ataque": 15,"Nível de Defesa": 15,"Pontos de Vida": 120},
				"Ninetales": {"Poder de Ataque": 20,"Nível de Defesa": 10,"Pontos de Vida": 120},
				"Arcanine": {"Poder de Ataque":18,"Nível de Defesa": 23,"Pontos de Vida": 120}}
	print ("Veja Abaixo os Inspermons disponíveis:")
	disp = "Blastoise","Charizard","Alakazam","Gyarados","Snorlax","Dragonite","Bulbasaur","Pikachu","Ninetales","Arcanine"
	print (disp)
	perg = input ("Você deseja saber os atributos de algum? Basta digitar seu nome! ")
	print (Insperdex[perg])
	pergu =int(input("Se você deseja saber os atributos de mais algum digite 0. Se não digite 1 para continuar: "))
	if pergu==1:
		primeiro=input("Então agora escolha o seu Inspermon inicial dentre um dos apresentados: ")
	if pergu==0:
		pok=input("Você deseja saber os atributos e qual Inspermon?")
		print (Insperdex[pok])
		primeiro = input("Agora que você já viu as opções escolha o seu Inspermon inicial dentre um dos apresentados: ")
	print ("Ótima escolha! Agora é hora de iniciar a aventura!")
	a1=int(input ("O que você deseja fazer com seu pokémon? Dormir (2) ou Passear(3): "))
	if a1==2:
		print ("Certo! Então é hora de descansar")
		break
	if a1!=2:
		print ("Empolgante! Vamos passear pelo campus do Inspermon!")
		time.sleep(1)
		print("Nossa! Aquilo é um...")
		time.sleep(1)
		a2=random.choice(list(Insperdex.keys()))
		print(a2)
		b1 =int(input("Você deseja fugir (4) ou batalhar (5)? "))
		if b1==4:
			b2=random.choice([1,2])
			if b2==1:
				print ("Ufa!! Você conseguiu fugir depois de muito esforço!")
				time.sleep(1)
				print("Essa foi por pouco, vamos parar por hoje")
				break
			if b2==2:
				b3=1
				print("Você não conseguiu escapar da batalha e por isso perdeu a vez de atacar!")	
		if b1==5:
			b3=1
		if b3==1:
			print ("Vai começar um grande desafio de batalha entre Inspèrmons! Boa Sorte!! ")
			time.sleep(1)
			#batalha
			at1 = {{"Pontos de Vida"}(primeiro)}
			at2 = {{"Poder de Ataque"}(a2)}
			att = at1 - at2
			print (att)


