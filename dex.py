import random
import time
qqq=0
while qqq<100:
    print ("Ola! Seja Bem Vindo ao Inspermon")
    Inspermons = {"Blastoise": {"Poder de Ataque": 55,"Nível de Defesa": 15,"Pontos de Vida": 100,"XP": 0},
                "Charizard": {"Poder de Ataque": 90,"Nível de Defesa": 20,"Pontos de Vida": 100,"XP": 0},
                "Alakazam": {"Poder de Ataque": 70,"Nível de Defesa": 10,"Pontos de Vida": 100,"XP": 0},
                "Gyarados": {"Poder de Ataque": 75,"Nível de Defesa": 10,"Pontos de Vida": 100,"XP": 0},
                "Snorlax": {"Poder de Ataque": 700,"Nível de Defesa": 25,"Pontos de Vida": 100,"XP": 0},
                "Dragonite": {"Poder de Ataque":85,"Nível de Defesa": 15,"Pontos de Vida": 100,"XP": 0},
                "Bulbasaur": {"Poder de Ataque": 45,"Nível de Defesa": 5,"Pontos de Vida": 100,"XP": 0},
                "Pikachu": {"Poder de Ataque": 50,"Nível de Defesa": 10,"Pontos de Vida": 100,"XP": 0},
                "Ninetales": {"Poder de Ataque": 105,"Nível de Defesa": 25,"Pontos de Vida": 100,"XP": 0},
                "Arcanine": {"Poder de Ataque":80,"Nível de Defesa": 15,"Pontos de Vida": 100,"XP": 0}}
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
        del Inspermons[primeiro]
    if pergu==0:
        pok=input("Você deseja saber os atributos de qual Inspermon? ")
        print (Inspermons[pok])
        primeiro = input("Agora que você já viu as opções escolha o seu Inspermon inicial dentre um dos apresentados: ")
        r=(Inspermons[primeiro])
        Insperdex[primeiro]=r
        del Inspermons[primeirox]
    print ("Ótima escolha! Agora é hora de iniciar a aventura!")
    a1=int(input ("O que você deseja fazer com seu pokémon? Dormir (2) ou Passear(3): "))
    if a1==2:
        print ("Certo! Então é hora de descansar")
        break
    if a1==3:
        print ("Empolgante! Vamos passear pelo campus do Inspermon!")
        time.sleep(1)
        v=1
        while v<10: 
            c2=random.choice([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1.2,1.25,1.3,1.35,1.4,1.45,1.5])
            c4=random.choice([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1.05,1.1,1.15,1.2])
            c2=1
            c4=1
            print("Estávamos passeando quando derrepente...")
            print("Nossa! Aquilo é um...")
            time.sleep(2)
            a2=random.choice(list(Inspermons.keys()))
            print(a2)
            b1 =int(input("Você deseja fugir (4) ou batalhar (5)? "))
            if b1==5:
                print("Vai começar um grande desafio de batalha entre Inspèrmons! Boa Sorte!! ")
                time.sleep(0.5)
                print("Você será o primeiro a atacar!")
                y=0
                while y<100:
                    if c2>1:
                        print("Você está num dia de sorte, seu ataque terá mais força do que o normal!")
                    Inspermons[a2]["Pontos de Vida"]=Inspermons[a2]["Pontos de Vida"]+(c2*(Inspermons[a2]["Nível de Defesa"]-Insperdex[primeiro]["Poder de Ataque"]))
                    print("loading...")
                    time.sleep(4)
                    if Inspermons[a2]["Pontos de Vida"]<=0:
                        print("Você o derrotou, muito bem!")                                
                        time.sleep(0.5)
                        print("Parabéns! Você ganhou 1 XP!")
                        Insperdex[primeiro]["XP"]=Insperdex[primeiro]["XP"]+1
                        break
                    if Inspermons[a2]["Pontos de Vida"]>0:
                        print("Seu ataque não foi forte o suficiente, restam %d Pontos de Vida do adversário!"%(Inspermons[a2]["Pontos de Vida"]))
                        time.sleep(1)
                        print("Agora é hora do seu adversário atacar")
                        print("loading...")
                        time.sleep(2)
                        if c4>1:
                            print("Seu adversário está em um dia sorte, seu ataque terá mais força que o normal!")
                        Insperdex[primeiro]["Pontos de Vida"]=Insperdex[primeiro]["Pontos de Vida"]+(c4*(Insperdex[primeiro]["Nível de Defesa"]-Inspermons[a2]["Poder de Ataque"]))
                        if Insperdex[primeiro]["Pontos de Vida"]<=0:
                            print("O seu adversário era forte demais, você perdeu!")
                            break
                        if Insperdex[primeiro]["Pontos de Vida"]>0:
                            print("Você suportou ao ataque, e ainda restam %d Pontos de Vida ao seu Inspermon!"%(Insperdex[primeiro]["Pontos de Vida"]))
                            print("Agora o seu Inspermon atacará de novo")
#batalha se não conseguir fugir
            if b1==4:
                b2=random.choice([1,2])
                if b2==1:
                    print ("Ufa!! Você conseguiu fugir depois de muito esforço!")
                    time.sleep(1)
                    print("Essa foi por pouco, vamos parar por hoje")
                    break
                if b2==2:
                    print("Você não conseguiu escapar da batalha e por isso perdeu a vez de atacar!")
                    print("Vai começar um grande desafio de batalha entre Inspèrmons! Boa Sorte!! ")
                    time.sleep(0.5)
                    y=0
                    while y<100:
                        if c4>1:
                            print("Seu adversário está em um dia sorte, seu ataque terá mais força que o normal!")
                        Insperdex[primeiro]["Pontos de Vida"]=Insperdex[primeiro]["Pontos de Vida"]+(c4*(Insperdex[primeiro]["Nível de Defesa"]-Inspermons[a2]["Poder de Ataque"]))
                        print("loading...")
                        time.sleep(4)
                        if Insperdex[primeiro]["Pontos de Vida"]<=0:
                            print("O seu adversário era forte demais, você perdeu")                                
                            break
                        if Insperdex[primeiro]["Pontos de Vida"]>0:
                            print("Você suportou ao ataque, e ainda restam %d Pontos de Vida ao seu Inspermon!"%(Insperdex[primeiro]["Pontos de Vida"]))
                            time.sleep(0.5)
                            print("Agora é sua vez de atacar!")
                            print("loading...")
                            time.sleep(2)
                            if c2>1:
                                print("Você está num dia de sorte, seu ataque terá mais força do que o normal!")
                            Inspermons[a2]["Pontos de Vida"]=Inspermons[a2]["Pontos de Vida"]+(c4*(Inspermons[a2]["Nível de Defesa"]-Insperdex[primeiro]["Poder de Ataque"]))
                            if Inspermons[a2]["Pontos de Vida"]<=0:
                                print("Muito bem! Você o derrotou!")
                                time.sleep(0.5)
                                print("Parabéns! Você ganhou 1 XP!")
                                Insperdex[primeiro]["XP"]=Insperdex[primeiro]["XP"]+1
                                break
                            if Inspermons[a2]["Pontos de Vida"]>0:
                                print("Seu ataque não foi forte o suficiente, restam %d Pontos de Vida do adversário!"%(Inspermons[a2]["Pontos de Vida"]))
                                print("Agora é a vez do seu adversário atacar de novo")
            time.sleep(2)
            print("Após essa batalha você tem %d de XP"%(Insperdex[primeiro]["XP"]))
            if Insperdex[primeiro]["XP"]==3:
#                 print("Você acumulou XP suficiente para evoluir!")
#                 p1="Blastoise"
#                 p2="Charizard"
#                 p3="Alakazam"
#                 p4="Snorlax"
#                 p5="Dragonite"
#                 p6="Bulbasaur"
#                 p8="Ninetales"
#                 p9="Arcaine"
#                 p7="Pikachu"
#                 if primeiro==p1:
# evoluão do blastoise        
#                     Insperdex[primeiro]="Mine"
#                 if primeiro==p2:
# evoluão do charizard
#                     Insperdex[primeiro]="e"
#                 if primeiro==p3:
# evoluão do alakazam
#                     Insperdex[primeiro]="d"
#                 if primeiro==p4:
# evoluão do gyarados    
#                     Insperdex["ee"]=Insperdex[primeiro]
                if primeiro=="Snorlax":
# evoluão do snorlax
                    Insperdex[primeiro]=Insperdex["weirdoo"]
#                 if primeiro==p5:
# evoluão do dragonite        
#                     Insperdex[primeiro]="uu"
#                 if primeiro==p6:
# evoluão do bulbasaur 
#                    Insperdex[primeiro]="rrrr"
#                 if primeiro==p7:
# evoluão do pikachu
#                     Insperdex[primeiro]="qqqqqqq"
#                 if primeiro==p8:
# evoluão do ninetales   
#                     Insperdex[primeiro]="ccc"
#                 if primeiro==p9:
# evoluão do arcaine 
#                     Insperdex[primeiro]="Lllll"
            print(Insperdex)
            print ("Agora que acabou a batalha vamos procurar por um pacote de vida extra no campus!")
            time.sleep(1)
            pacote = random.choice([1,1,1,2,2,2,2,2,2,2,2])
            if pacote == 2:
                Insperdex[primeiro]["Pontos de Vida"] == 100
                time.sleep(2)
                print ("Ótimo! Você encontrou um pacote e sua vida foi regenerada agora vamos continuar a jornada")
                time.sleep(2)
                perg2 = int(input("Com a vida regenerada você agora prefere descansar(1) seu Inspermon ou seguir passeando(2) pelo campus? "))
                if perg2 == 1:
                    time.sleep(2)
                    print ("Certo então é hora de descansar")
                    break               
                if perg2 == 2:
                    time.sleep(2)
                    continue
            if pacote == 1:
                if Insperdex[primeiro]["Pontos de Vida"]>0:
                    x = int(input("Infelizmente você não encontrou nada pelo campus! A sua vida atual é de %d pontos! Você deseja continuar(1) ou prefere reiniciar(2) o jogo? " %(Insperdex)[primeiro]["Pontos de Vida"]) )
                    time.sleep(0.5)
                    if x ==1:
                        continue
                    if x ==2:
                        print ("O jogo será reiniciado!")
                        time.sleep(1)
                        print ("loading...")
                        time.sleep(3)
                        break
                if Insperdex[primeiro]["Pontos de Vida"]<=0:
                    print("Infelizmente você não encontrou nada pelo campus e sua vida atual é baixa demais para continuar")
                    print("O jogo será reiniciado")
                    time.sleep(1)
                    print("loading...")
                    break    