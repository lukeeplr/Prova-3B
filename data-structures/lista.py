class Lista:
	itens = None
	tamanho = None
	ultimo = None

	def __init__(self,tamanho):
		self.itens = [None]*tamanho
		self.ultimo = 0
		self.tamanho = tamanho

	def estaCheia(self):
		return self.ultimo == self.tamanho

	def estaVazia(self):
		return self.ultimo == 0

	def inserir(self,item,pos):
		if not self.estaCheia() and pos<=self.ultimo:
			for i in range(self.ultimo,pos,-1):
				self.itens[i] = self.itens[i-1]
			self.itens[pos] = item
			self.ultimo +=1
		else:
			print('operacao invalida')

	def remover(self,pos):
		if not self.estaVazia() and pos < self.ultimo:
			item = self.itens[pos]
			for i in range(pos,self.ultimo-1):
				self.itens[i] = self.itens[i+1]
			self.ultimo -=1
			return item
		else:
			print('operacao invalida')

	def imprimir(self):
		for i in range(self.ultimo):
			print(self.itens[i])
		print('---')
