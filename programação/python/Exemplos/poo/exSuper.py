class Mamifero():
	def __init__(self,nome,especie,falar):
		self.nome = nome
		self.especie = especie
		self.falar = falar

	def falando(self):
		if self.falar[0].lower == 's':

			print("%s sabe falar"%self.nome)
			return
		else:
			print("%s não sabe falar pois ele é um %s"%(self.nome,self.especie))
			return

joao = Mamifero('rex','cachorro','s')
joao.falando()