from modulos.Desafio import *

def main():
	lista_alunos, lista_cursos = carregar_dados("./dataset/notas.csv")

	print(" ----------------- O CR DOS ALUNOS É: ----------------- ")
	imprime_cr_alunos(lista_alunos)

	#############################################

	print(" ------------------------------------------------------ ")
	print(" ------------- A MEDIA DE CR POR CURSO É: ------------- ")
	imprime_media_cr(lista_cursos,lista_alunos)

if __name__ == "__main__":
    main()