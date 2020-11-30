### foi usado o modulo pandas para facilitar a manipulacao
### dos dados do arquivo .csv
import pandas as pd
from modulos.ClassAluno import *
from modulos.ClassDisciplina import *
from modulos.ClassCurso import *

### realiza a leitura do csv, instanciando os objetos necessários
### e fazendo a ligação entre eles, e adicionando os alunos e cursos em listas
### por fim, retorna as listas de objetos de alunos e cursos
### as Classes sao Curso, AlunoHistorico e DisciplinaHistorico
def carregar_dados(pathfile):
	f = pd.read_csv(pathfile)
	materia = None
	lista_alunos = []
	lista_cursos = []
	aluno_atual = -1		### variavel para acessar a lista de alunos

	### ordena o dataframe pela matricula (para o caso do csv nao estar ordenado)
	f = f.sort_values('MATRICULA')

	for index,row in f.iterrows():

		## instancia o aluno com a matricula atual, caso ainda nao tenha sido feito
		if row[0] not in [aluno.matricula for aluno in lista_alunos]:
			lista_alunos.append(AlunoHistorico(row[0]))
			aluno_atual += 1
		
		## instancia o curso com o codigo de curso atual, caso ainda nao tenha sido feito
		if row[2] not in [curso.cod_curso for curso in lista_cursos]:
			lista_cursos.append(Curso(row[2]))

		## instancia a disciplina atual
		materia = DisciplinasHistorico(row[1], row[4], row[3], row[5], row[2])
		## realiza a associação entre o aluno e a disciplina da iteracao atual
		lista_alunos[aluno_atual].disciplinas_aluno = materia

		## realiza a associação entre o curso e a disciplina da iteracao atual
		for curso in lista_cursos:
			if curso.cod_curso == materia.curso_associado:
				curso.disciplinas_curso = materia

	### ordenando as listas por matricula e codigo do curso
	lista_alunos.sort(key=lambda aluno: aluno.matricula)
	lista_cursos.sort(key=lambda curso: curso.cod_curso)
	return lista_alunos, lista_cursos


### percorre a lista de alunos realizando a chamada do metodo da classe
### que retorna o cr calculado do objeto aluno que a chamou
def imprime_cr_alunos(lista_alunos):
	for aluno in lista_alunos:
		print(f'{aluno.matricula:26} - {aluno.cr}')

### percorre a lista de cursos e a de alunos, verificando quais alunos
### sao matriculados no respectivo curso, chamando os metodos necessarios para
### calcular o cr medio do curso
def imprime_media_cr(lista_cursos,lista_alunos):
	for curso in lista_cursos:
		cr_alunos = 0
		for aluno in lista_alunos:
			if curso.verifica_inscricao(aluno.matricula):
				cr_alunos += aluno.cr
		print(f'{curso.cod_curso:26} - {int(cr_alunos/curso.num_inscritos)}')