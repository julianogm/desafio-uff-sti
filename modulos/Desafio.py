### Biblioteca pandas para facilitar a 
### manipulação dos dados do arquivo .csv
import pandas as pd
from modulos.ClassAluno import *
from modulos.ClassDisciplina import *
from modulos.ClassCurso import *

### Realiza a leitura do csv, instanciando os objetos necessários e fazendo a 
### ligação entre eles, adicionando os alunos, cursos, e disciplinas em listas.
### Por fim, retorna as listas de objetos de aluno, curso e disciplina.
### As Classes sao Curso, Aluno e Disciplina
def carregar_dados(pathfile):
	f = pd.read_csv(pathfile)
	materia = None
	lista_alunos = []
	lista_cursos = []
	lista_disciplinas = []
	aluno_atual = -1		### Variável para acessar o aluno mais recente da lista de alunos.

	### Ordena o dataframe pela matricula (caso o .csv não estar ordenado)
	f = f.sort_values('MATRICULA')

	for index,row in f.iterrows():

		## Caso ainda não tenha sido instanciado, instancia o aluno e adiciona-o a uma lista.
		if row[0] not in [x.matricula for x in lista_alunos]:
			lista_alunos.append(Aluno(row[0]))
			aluno_atual += 1

		# Adiciona ao aluno atual um código de disciplina, junto com uma nota
		# e período, funcionando como um histórico, sendo esses dados passados em forma de tupla.
		lista_alunos[aluno_atual].historico = (row[1],row[3],row[5])
		
		## Caso ainda não tenha sido instanciado, instancia a disciplina e a adiciona a uma lista.
		if row[1] not in [z.cod_disciplina for z in lista_disciplinas]:
			lista_disciplinas.append(Disciplina(row[1], row[4]))		
		
		## Caso ainda não tenha sido instanciado, instancia o curso e o adiciona a uma lista
		if row[2] not in [y.cod_curso for y in lista_cursos]:
			lista_cursos.append(Curso(row[2]))

		# Adiciona a matricula do aluno atual na lista de alunos matriculados no curso correspondente.
		i_curso = [x.cod_curso for x in lista_cursos].index(row[2])
		lista_cursos[i_curso].matriculados = row[0]

	### Ordena as listas por matrícula, código do curso, e código de disciplina
	lista_alunos.sort(key=lambda x: x.matricula)
	lista_cursos.sort(key=lambda y: y.cod_curso)
	lista_disciplinas.sort(key=lambda z: z.cod_disciplina)

	return lista_alunos, lista_cursos, lista_disciplinas

### Recebe um objeto aluno e uma lista de objetos disciplina
### Verifica as disciplinas cursadas pelo aluno
### Adiciona em uma lista de tuplas os dados das disciplinas cursadas pelo aluno
### Após isso, passa a lista de tuplas para o objeto aluno calcular o cr, e retornar esse valor
def cr_aluno(aluno, lista_disciplinas):
	materias_cursadas = []
	for disciplina in lista_disciplinas:
		if aluno.verifica_inscricao(disciplina.cod_disciplina):
			materias_cursadas.append((disciplina.cod_disciplina,disciplina.carga_horaria))
	return aluno.calcula_cr(materias_cursadas)

### Recebe um objeto curso, além de listas de objetos aluno e disciplina 
### Percorre a lista de alunos, verificando se cada objeto aluno é matriculado
### No curso, somando o cr de todos os alunos do curso
### Retorna o cr medio do curso
def media_cr_curso(curso, lista_alunos, lista_disciplinas):
	cr_alunos = 0
	for aluno in lista_alunos:
		if curso.verifica_inscricao(aluno.matricula):
			cr_alunos += cr_aluno(aluno,lista_disciplinas)
	return int(cr_alunos/curso.num_inscritos)