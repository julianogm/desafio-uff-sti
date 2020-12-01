from flask import Flask, render_template, request, url_for
from modulos.Desafio import *
from main import main

app = Flask(__name__)

@app.route('/')
def index():
    ### Gera as listas com os objetos referentes
	alunos, cursos, disciplinas = carregar_dados("./dataset/notas.csv")
	alunos_cr = []
	cursos_cr = []

	for aluno in alunos:
		cr = cr_aluno(aluno,disciplinas)
		alunos_cr.append((aluno.matricula,cr))

	#############################################

	for curso in cursos:
		media = media_cr_curso(curso, alunos, disciplinas)
		cursos_cr.append((curso.cod_curso, media))
	return render_template('index.html', alunos_cr=alunos_cr, cursos_cr=cursos_cr)

if __name__ == "__main__":
	app.run(debug=True)