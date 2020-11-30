### Cada objeto aluno tera seu identificador unico, e tera uma lista de objetos
### disciplina associado a ele (como um histórico)
class AlunoHistorico(object):
    def __init__(self, id_aluno):
        self.__id_aluno = id_aluno
        self.__disciplinas = []

    ### retorna a matricula do aluno
    @property
    def matricula(self):
        return self.__id_aluno

    ### retorna o historico de disciplinas (nesse casos, objetos) do aluno
    @property
    def disciplinas_aluno(self):
        return self.__disciplinas

    ### setter que faz a associacao entre o aluno e as disciplinas que o mesmo fez/faz
    ### essa associacao foi necessaria para o calculo do cr medio do curso
    @disciplinas_aluno.setter
    def disciplinas_aluno(self, disciplina):
        disciplina.aluno_associado = self.__id_aluno
        self.__disciplinas.append(disciplina)

    ### funcao que retorna o cr do aluno que a chamou
    @property
    def cr(self):
        nota_x_ch = 0
        chtotal = 0
        for it in self.__disciplinas:
            nota_x_ch += it.nota*it.carga_horaria
            chtotal += it.carga_horaria
        return int(nota_x_ch/chtotal)