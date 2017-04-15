import random
import time
x=0
while x<1000:
	print ("Ola! Seja Bem Vindo ao Inspermon")
	Inspermons = {"Blastoise": {"Poder de Ataque": 55,"Nível de Defesa": 15,"Pontos de Vida": 100},
				"Charizard": {"Poder de Ataque": 90,"Nível de Defesa": 20,"Pontos de Vida": 100},
				"Alakazam": {"Poder de Ataque": 70,"Nível de Defesa": 10,"Pontos de Vida": 100},
				"Gyarados": {"Poder de Ataque": 75,"Nível de Defesa": 10,"Pontos de Vida": 100},
				"Snorlax": {"Poder de Ataque": 70,"Nível de Defesa": 25,"Pontos de Vida": 100},
				"Dragonite": {"Poder de Ataque":85,"Nível de Defesa": 15,"Pontos de Vida": 100},
				"Bulbasaur": {"Poder de Ataque": 45,"Nível de Defesa": 5,"Pontos de Vida": 100},
				"Pikachu": {"Poder de Ataque": 50,"Nível de Defesa": 10,"Pontos de Vida": 100},
				"Ninetales": {"Poder de Ataque": 105,"Nível de Defesa": 25,"Pontos de Vida": 100},
				"Arcanine": {"Poder de Ataque":80,"Nível de Defesa": 15,"Pontos de Vida": 100}}
	Insperdex={}
	time.sleep(1.5)
	print ("Veja Abaixo os Inspermons disponíveis no jogo:")
	disp = "Blastoise","Charizard","Alakazam","Gyarados","Snorlax","Dragonite","Bulbasaur","Pikachu","Ninetales","Arcanine"
	print (disp)
	time.sleep(1)
	perg = input ("Você deseja saber os atributos de algum? Basta digitar seu nome! ")
	print (Inspermons[perg])
	pergu =int(input("Se você deseja saber os atributos de mais algum digite 0. Se não digite 1 para continuar: "))          
	if pergu==1:
		primeiro=input("Então agora escolha o seu Inspermon inicial dentre um dos apresentados: ")
	r=(Inspermons[primeiro])
	Insperdex[primeiro]=r
	if pergu==0:
		pok=input("Você deseja saber os atributos de qual Inspermon?")
		print (Inspermons[pok])
		primeiro = input("Agora que você já viu as opções escolha o seu Inspermon inicial dentre um dos apresentados: ")
	r=(Inspermons[primeiro])
	Insperdex[primeiro]=r
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
		a2=random.choice(list(Inspermons.keys()))
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
		time.sleep(1)
		print("Vai começar um grande desafio de batalha entre Inspèrmons! Boa Sorte!! ")
	c2=random.choice([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1.2,1.25,1.3,1.35,1.4,1.45,1.5])
	if b1==5:
		b3=2
	if b3==2:
		print("Você sérá o primeiro a atacar!")
		c1=(Inspermons[a2]["Nível de Defesa"])-(Inspermons[primeiro]["Poder de Ataque"])
		if c2>1:
			print("Você está num dia de sorte, seu ataque terá mais força do que o normal!")
#meu ataque 1
			Inspermons[a2]["Pontos de Vida"]=Inspermons[a2]["Pontos de Vida"] + (c1*c2)
			c3=Inspermons[a2]["Pontos de Vida"]
			if c3<=0:
				print("Você o derrotou, muito bem!")
				break
			if c3>0:
				print("Seu ataque não foi forte o suficiente, restam %d Pontos de Vida do adversário!"%(c3))
				time.sleep(0.5)
				print("Agora é a vez dele atacar")
				b3=1
	if b3==1:
		time.sleep(1)			
		c4=random.choice([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1.05,1.1,1.15,1.2])
		if c4>1:
			print("Seu adversário está em um dia sorte, seu ataque terá mais força que o normal!")
#ataque dele 1
			c5=Inspermons[primeiro]["Nível de Defesa"]-Inspermons[a2]["Poder de Ataque"]
			Inspermons[primeiro]["Pontos de Vida"]=Inspermons[primeiro]["Pontos de Vida"]+(c5*c4)
			c6=Inspermons[primeiro]["Pontos de Vida"]
			if c6<=0:
				print("O seu adversário era forte demais, você perdeu!")
				break
			if c6>0:
				print("Você suportou ao ataque, e ainda restam %d Pontos de Vida ao seu Inspermon!"%(c6))
				time.sleep(0.5)
				print ("Então agora seu Inspermon atacará novamente")
#meu ataque 2
				c7=(Inspermons[a2]["Nível de Defesa"])-(Inspermons[primeiro]["Poder de Ataque"])
				Inspermons[a2]["Pontos de Vida"]=Inspermons[a2]["Pontos de Vida"]+(c7*c2)
				c8=Inspermons[a2]["Pontos de Vida"]
				if c8<=0:
					print("Você o derrotou, muito bem!")
					break
				if c8>0:
					print("Seu ataque não foi forte o suficiente, restam %d Pontos de Vida do adversário!"%(c8))
					time.sleep(0.5)
					print("Agora é a vez dele atacar")
					time.sleep(1)
#ataque dele 2
					c9=Inspermons[primeiro]["Nível de Defesa"]-Inspermons[a2]["Poder de Ataque"]
					Inspermons[primeiro]["Pontos de Vida"]=Inspermons[primeiro]["Pontos de Vida"]+(c9*c4)
					c10=Inspermons[primeiro]["Pontos de Vida"]
					if c10<=0:
						print("O seu adversário era forte demais, você perdeu!")
						break
					if c10>0:
						print("Você suportou ao ataque, e ainda restam %d Pontos de Vida ao seu Inspermon!"%(c10))
						time.sleep(0.5)
						print("Agora seu Inspermon terá mais uma chance de ataque")
						time.sleep(1)
#meu ataque 3
						c11=(Inspermons[a2]["Nível de Defesa"])-(Inspermons[primeiro]["Poder de Ataque"])
						Inspermons[a2]["Pontos de Vida"]=Inspermons[a2]["Pontos de Vida"]+(c11*c2)
						c12=Inspermons[a2]["Pontos de Vida"]
						if c12<=0:
							print("Você o derrotou, muito bem!")
							break
						if c12>0:
							print("Seu ataque não foi forte o suficiente, restam %d Pontos de Vida do adversário!"%(c12))
							time.sleep(0.5)
							print("O adversário agora terá outra chance de atacar")
							time.sleep(1)
#ataque dele 3
							c13=Inspermons[primeiro]["Nível de Defesa"]-Inspermons[a2]["Poder de Ataque"]
							Inspermons[primeiro]["Pontos de Vida"]=Inspermons[primeiro]["Pontos de Vida"]+(c13*c4)
							c14=Inspermons[primeiro]["Pontos de Vida"]
							if c14<=0:
								print("O seu adversário era forte demais, você perdeu!")
								break
							if c14>0:
								print("Você suportou ao ataque, e ainda restam %d Pontos de Vida ao seu Inspermon!"%(c14))
								print("Agora seu Inspermon terá mais uma chance de ataque")
								time.sleep(1)
#meu ataque 4
								c15=(Inspermons[a2]["Nível de Defesa"])-(Inspermons[primeiro]["Poder de Ataque"])
								Inspermons[a2]["Pontos de Vida"]=Inspermons[a2]["Pontos de Vida"]+(c15*c2)
								c16=Inspermons[a2]["Pontos de Vida"]
								if c16<=0:
									print("Você o derrotou, muito bem!")
									break
								if c16>0:
									print("Seu ataque não foi forte o suficiente, restam %d Pontos de Vida do adversário!"%(c16))
									print("O adversário agora terá outra chance de atacar")
									time.sleep(1)
#ataque dele 4
									c18=Inspermons[primeiro]["Nível de Defesa"]-Inspermons[a2]["Poder de Ataque"]
									Inspermons[primeiro]["Pontos de Vida"]=Inspermons[primeiro]["Pontos de Vida"]+(c18*c4)
									c19=Inspermons[primeiro]["Pontos de Vida"]
									if c19<=0:
										print("O seu adversário era forte demais, você perdeu!")
										break
									if c19>0:
										print("Você suportou ao ataque, e ainda restam %d Pontos de Vida ao seu Inspermon!"%(c19))
										time.sleep(0.5)
										print("Agora seu Inspermon terá mais uma chance de ataque") 
#meu ataque 5
										c20=(Inspermons[a2]["Nível de Defesa"])-(Inspermons[primeiro]["Poder de Ataque"])
										Inspermons[a2]["Pontos de Vida"]=Inspermons[a2]["Pontos de Vida"]+(c20*c2)
										c21=Inspermons[a2]["Pontos de Vida"]
										if c21<=0:
											print("Você o derrotou, muito bem!")
											break
										if c21>0:
											print("Seu ataque não foi forte o suficiente, restam %d Pontos de Vida do adversário!"%(c21))
											time.sleep(0.5)
											print("O adversário agora terá outra chance de atacar")
											time.sleep(1)
#ataque dele 5
											c22=Inspermons[primeiro]["Nível de Defesa"]-Inspermons[a2]["Poder de Ataque"]
											Inspermons[primeiro]["Pontos de Vida"]=Inspermons[primeiro]["Pontos de Vida"]+(c22*c4)
											c23=Inspermons[primeiro]["Pontos de Vida"]
											if c23<=0:
												print("O seu adversário era forte demais, você perdeu!")
												break
											if c23>0:
												print("Você suportou ao ataque, e ainda restam %d Pontos de Vida ao seu Inspermon!"%(c23))
												time.sleep(0.5)
												print("Agora seu Inspermon terá a ultima chance de ataque")
												time.sleep(1)
#meu ataque 6
												c24=(Inspermons[a2]["Nível de Defesa"])-(Inspermons[primeiro]["Poder de Ataque"])
												Inspermons[a2]["Pontos de Vida"]=Inspermons[a2]["Pontos de Vida"]+(c24*c2)
												c25=Inspermons[a2]["Pontos de Vida"]
												if c25<=0:
													print("Você o derrotou, muito bem!")
													break


			
			
