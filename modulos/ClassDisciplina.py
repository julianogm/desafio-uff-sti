### Cada objeto disciplina funcionara como uma pagina de historico e será associado
### a um ou mais alunos e cursos
class DisciplinasHistorico(object):
    def __init__(self, cod_disciplina, carga_horaria, nota, periodo, curso):
        self.__cod_disciplina = cod_disciplina
        self.__carga_horaria = carga_horaria
        self.__matricula = 0
        self.__nota = nota
        self.__periodo = periodo
        self.__curso = curso

    ### retorna o codigo da disciplina
    @property
    def cod_disciplina(self):
        return self.__cod_disciplina

    ### retorna o a nota do objeto em questao (que estara associado a cursos e alunos)
    @property
    def nota(self):
        return self.__nota

    ### setter para nota
    #@nota.setter
    #def nota(self, nota):
    #    self.__nota = nota

    ### retorna a carga horaria da disciplina
    @property
    def carga_horaria(self):
        return self.__carga_horaria

    ### retorna a matricula associada
    @property
    def aluno_associado(self):
        return self.__matricula

    ### setter para a matricula associada
    @aluno_associado.setter
    def aluno_associado(self, matricula):
        self.__matricula = matricula

    ### retorna o curso associado
    @property
    def curso_associado(self):
        return self.__curso

    ### setter para o curso associado
    @curso_associado.setter
    def curso_associado(self, curso):
        self.__curso = curso