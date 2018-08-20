"""A CBF solicitou que você fizesse um programa para calcular a pontuação dos times do Campeonato Brasileiro (Série A).
Inicialmente o programa precisa ler o nome dos times que participam da Série A. Para interromper o cadastro de times,
deverá ser lido a String "fim_times" no lugar do nome do time.
Nome do time da casa
Gols do time da casa
Nome do time visitante
Gols do time visitante
Essa leitura se repete para cada jogo.
Para interromper o cadastro dos jogos, deverá ser lido a String "fim_dos_jogos" no lugar do nome do time da casa.

"""

times=[]
jogos=[]
cont = 1
print("###CADASTRO DOS TIMES###")
while True:
    time = {}
    time["nome"]=input("Time {}: ".format(cont)).title()
    if time["nome"].lower() == "fim_times":
        break
    else:
        time["golsFeitos"]=0
        time["golsSofridos"]=0
        time["qJogos"]=0
        time["qPontos"]=0
        time["qVitorias"]=0
        time["qDerrotas"]=0
        time["qEmpates"]=0
        time["saldoDeGols"]=0
        times.append(time)
        cont+=1

print("###FIM DO CADASTRO DOS TIMES###")
#jogos
print("\n###REGISTRO DOS JOGOS###")

#parte do registro de partidias
while True:
    tc = input("Time da Casa: ").title()
    existet1 = False
    existet2 = False

    #time1
    if tc.lower() =="fim_dos_jogos":
        break

    #testa se o time esta cadastrado
    for x in range(len(times)):
        if times[x]["nome"]==tc:
            existet1 = True
            times[x]["qJogos"]+=1
    if not existet1:
        print("time não encontrado")
        continue
    #fim do teste<-
    golsT1 = int(input("Gols Time da Casa: "))

    #time2
    tv = input("Time Visitante: ").title()
    #testa se o time vistante esta cadastrado
    for x in range(len(times)):
        if times[x]["nome"]==tv:
            existet2 = True
            times[x]["qJogos"]+=1
    if not existet2:
        print("time não encontrado")
        continue
    #fim do teste<-

    golsT2 = int(input("Gols Time Visitante: "))
	#calcula o saldo de gols e grava no dicionario os gols
    for x in range(len(times)):
        if times[x]["nome"]==tc:
            times[x]["golsFeitos"]+=golsT1
            times[x]["golsSofridos"]+=golsT2
			#subtrai os gols sofridos dos gols feitos e salva no saldo de gols
            times[x]["saldoDeGols"]=times[x]["golsFeitos"]-times[x]["golsSofridos"]
            if golsT1>golsT2:
                times[x]["qPontos"] += 3
                times[x]["qVitorias"] += 1
            elif golsT1 == golsT2:
                times[x]["qPontos"] += 1
                times[x]["qEmpates"] += 1
            else:
                times[x]["qDerrotas"] +=1

	#calcula o saldo de gols e grava no dicionario os gols
    for x in range(len(times)):
        if times[x]["nome"]==tv:
            times[x]["golsFeitos"]+=golsT2
            times[x]["golsSofridos"]+=golsT1
			#subtrai os gols sofridos dos gols feitos e salva no saldo de gols
            times[x]["saldoDeGols"]=times[x]["golsFeitos"]-times[x]["golsSofridos"]
            if golsT2>golsT1:
                times[x]["qPontos"]+=3
                times[x]["qVitorias"]+=1
            elif golsT1==golsT2:
                times[x]["qPontos"]+=1
                times[x]["qEmpates"]+=1
            else:
                times[x]["qDerrotas"] +=1


    print("##Jogo Cadastrado Com Sucesso.##")

print("=== Tabela de Pontuação ===\nTIME|JOGOS|PONTOS|VITÓRIAS|DERROTAS|EMPATES|SALDO")
campeao = {"nome":times[0]["nome"],"qPontos":times[0]["qPontos"]}

for time in range(len(times)):
    if times[time]["qPontos"]>campeao["qPontos"]:
        campeao["nome"]=times[time]["nome"]

for time in range(len(times)):
    t = times[time]
    print("{}|{}|{}|{}|{}|{}|{}".format(t["nome"], t["qJogos"], t["qPontos"],
            t["qVitorias"],t["qDerrotas"],t["qEmpates"],t["saldoDeGols"]))

print("===CAMPEÃO===\n Parabéns {}!".format(campeao["nome"]))