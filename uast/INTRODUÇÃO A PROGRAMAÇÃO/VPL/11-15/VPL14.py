nLaranjas = int(input(""))
resto = nLaranjas%6
if nLaranjas <6:
    print("{:.2f} {}".format((nLaranjas*1.5), "Promoção não ativada"))

elif nLaranjas>6 and resto == 0:
    print("{:.2f} {} {:.0f} {:.0f}".format(nLaranjas, "Promoção ativada", nLaranjas, resto))

elif nLaranjas>6 and resto != 0:
    print("{:.2f} {} {:.0f} {:.0f}".format((nLaranjas-resto)+(resto*1.5), "Promoção ativada", nLaranjas-resto, resto))
