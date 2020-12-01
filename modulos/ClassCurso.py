### Cada objeto curso tera seu identificador único,
### além uma lista de matrículas associadas a ele
class Curso(object):
    def __init__(self, id_curso):
        self.__id_curso = id_curso
        self.__alunos = []

    ### Retorna o código do curso
    @property
    def cod_curso(self):
        return self.__id_curso

    ### Retorna todas as matriículas dos alunos do curso
    @property
    def matriculados(self):
        return self.__alunos

    ### Setter para a lista de matrículas do curso, que adiciona
    ### a matrícula recebida na lista de matriculas associadas
    @matriculados.setter
    def matriculados(self, matricula):
        if matricula not in self.__alunos:
    	    self.__alunos.append(matricula)
        else:
            pass

    ### Retorna o número de alunos inscritos no curso
    @property
    def num_inscritos(self):
    	return len(self.__alunos)

    ### Retorna verdadeiro se a matricula recebida está 
    ### na lista de matriculas inscritas no curso
    def verifica_inscricao(self, matricula):
        if matricula in self.__alunos:
            return True
        return False