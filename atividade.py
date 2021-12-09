class Pessoa :
	nome = None
	data_nas = None
	telefone = None

	def __init__(self, nome, data_nas, tel):
		self.nome = nome
		self.data_nas = data_nas
		self.telefone = tel
############################################################

class Membro(Pessoa):
	data_associacao = None
	def __init__(self, nome, data_nas, tel, data_assoc):
		super().__init__(nome, data_nas, tel)
		self.data_associacao = data_assoc
############################################################
class MembroVIP(Membro):
	extras = []

	def acrescentarBeneficios(self, beneficio):
		self.extras.append(beneficio)
		print('Benefício incluido')
		for item in self.extras:
			print(item)
############################################################

class Funcionario(Pessoa):
	data_contratacao = None

	def setDataContratacao(self, data_cont):
		self.data_contratacao = data_cont
############################################################

class SalvaVidas(Funcionario):
	tempoExperiencia = 0

	def __init__(self, nome, data_nas, tel, data_cont, temp):
		super().__init__(nome, data_nas, tel)
		self.data_contratacao = data_cont
		self.tempoExperiencia = temp
############################################################




