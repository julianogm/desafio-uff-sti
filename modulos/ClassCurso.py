### Cada objeto curso tera seu identificador unico, e tera uma lista de objetos
### disciplina associado a ele
class Curso(object):
    def __init__(self, id_curso):
        self.__id_curso = id_curso
        self.__disciplinas_curso = []

    ### retorna o codigo do curso
    @property
    def cod_curso(self):
        return self.__id_curso

    ### retorna a lista de objetos disciplina associadas ao curso
    @property
    def disciplinas_curso(self):
        return self.__disciplinas_curso

    ### setter para a lista de objetos disciplina associadas ao curso
    @disciplinas_curso.setter
    def disciplinas_curso(self, disciplina):
    	self.__disciplinas_curso.append(disciplina)

    ### retorna o numero de alunos inscritos no curso
    @property
    def num_inscritos(self):
    	alunos_matriculados = []
    	for it in self.__disciplinas_curso:
    		if it.aluno_associado not in alunos_matriculados:
    			alunos_matriculados.append(it.aluno_associado)
    	return len(alunos_matriculados)

    ### verifica se a matricula é associada ao curso
    def verifica_inscricao(self, num_aluno):
        for it in self.__disciplinas_curso:
        	if num_aluno == it.aluno_associado:
        		return True
        return False