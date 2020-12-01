### Cada objeto disciplina terá seu identificador unico
### além de uma carga horaria
class Disciplina(object):
    def __init__(self, cod_disciplina, carga_horaria):
        self.__cod_disciplina = cod_disciplina
        self.__carga_horaria = carga_horaria

    ### Retorna o código da disciplina
    @property
    def cod_disciplina(self):
        return self.__cod_disciplina

    ### Retorna a carga horária da disciplina
    @property
    def carga_horaria(self):
        return int(self.__carga_horaria)

