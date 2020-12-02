### As funções utilizadas na main() estão no arquivo Desafio.py
from modulos.Desafio import *

def main():

	### Gera as listas com os objetos referentes
	alunos, cursos, disciplinas = carregar_dados("./datasets/notas.csv")

	print(" ------ O CR dos alunos é: ------ ")
	print(" -------- aluno - CR ------------ ")
	for aluno in alunos:
		cr = cr_aluno(aluno,disciplinas)
		print(f'{aluno.matricula:15} - {cr}')

	#############################################

	print(" -------------------------------- ")
	print(" ---- Média de CR por curso: ---- ")
	print(" -------- curso - media --------- ")
	for curso in cursos:
		media = media_cr_curso(curso, alunos, disciplinas)
		print(f'{curso.cod_curso:15} - {media}')

if __name__ == "__main__":
    main()