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
perg = input ("Você deseja saber os atributos de algum? Basta digitar seu nome!")
print (Inspèrdex[perg])
pergu = input ("Se você deseja saber os atributos de mais algum digite seu nome! Se não digite 1:")
if pergu == 1:
	primeiro = input("Então agora escolha o seu Inspérmon inicial dentre um dos apresentados:")
	print (Inspèrdex[perg])
if pergu!=1:
	print (Inspèrdex[pergu])
primeiro = input("Agora que você já viu todas as opções escolha o seu Inspérmon inicial dentre um dos apresentados")

