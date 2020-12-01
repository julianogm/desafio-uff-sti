### Cada objeto aluno tera seu identificador unico,
### além de uma lista de tuplas que será como um histórico
### onde cada tupla armazena o codigo da disciplina, 
### a nota dessa disciplina, e o periodo em que foi cursada 
class Aluno(object):
    def __init__(self, id_aluno):
        self.__id_aluno = id_aluno
        self.__dnp = []                 ### (disciplina, nota, periodo)

    ### Retorna a matrícula do aluno
    @property
    def matricula(self):
        return self.__id_aluno

    ### Retorna uma lista com o código de todas as disciplinas que o aluno cursou
    @property
    def disciplinas(self):
        disciplinas = [x[0] for x in self.__dnp]
        return disciplinas

    ### Retorna uma lista com todas as notas do aluno
    @property
    def notas(self):
        notas = [x[1] for x in self.__dnp]
        return notas
    
    ### Retorna o histórico do aluno (disciplina, nota e período cursado)
    @property
    def historico(self):
        return self.__dnp
    
    ### Adiciona a tupla recebida na lista de tuplas
    @historico.setter
    def historico(self, dnptuple):
        self.__dnp.append(dnptuple)

    ### Verifica se o aluno já cursou a disciplina recebida
    def verifica_inscricao(self, id_disciplina):
        for x in self.__dnp:
            if x[0] == id_disciplina:
                return True
        return False

    ### Função que calcula e retorna o CR do aluno que a chamou
    def calcula_cr(self, lista_inscricoes):
        nota_x_ch = 0
        chtotal = 0
        for x in lista_inscricoes:
            for y in self.__dnp:
                if y[0] == x[0]:
                    nota_x_ch += y[1]*x[1]
                    chtotal += x[1]
        return int(nota_x_ch/chtotal)