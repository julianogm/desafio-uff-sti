# Desafio UFF STI

Código para uma possível solução do desafio proposto pela STI - UFF.
O desafio consiste em calcular o CR dos alunos de uma universidade, de acordo com critérios prédefinidos, a partir de um arquivo csv que contém a lista de notas desses alunos. Ao final do processo, deverá ser impresso na tela o CR de todos os alunos e qual a média de CR dos cursos.
#### A linguagem utilizada foi python, na versão 3.8.

É utilizado o módulo pandas para facilitar a manipulação do csv. 
É necessário instalar o módulo pandas caso haja a necessidade de executar o código localmente.
##### No shell (Windows ou Linux):
```sh
$ pip install pandas
```
Nesse caso foi utilizado o instalador de pacotes pip.

### Estrutura
Os módulos foram divididos em Classes de Aluno, Disciplina e Curso, e um módulo de funções, além do arquivo main.

Cada objeto Aluno terá uma matrícula única, e também uma lista de tuplas que será seu histórico. Cada tupla dessa lista terá o código da disciplina cursada, a nota nessa disciplina, e o perído em que ela foi cursada.

Cada objeto Disciplina terá um código único de disciplina e sua carga horária.

Os objetos Curso, por sua vez, terão um código único de curso, e uma lista com todos os alunos matriculados.


### Saída
O arquivo main é o arquivo principal que faz a chamada dos métodos necessários para ler o arquivo e calcular o cr dos alunos e media de cr dos cursos. No final imprime os valores de saída no shell em que foi executada, como mostra a imagem abaixo:

>![saidadesafio](https://user-images.githubusercontent.com/29824937/100818948-ed089c00-3429-11eb-97a2-4c849151c6c5.png)


### GUI
Foi estruturado um outro arquivo, de forma semelhante ao arquivo principal, que imprime os dados em uma interface web (arquivo view).
Para isso foi utilizado o micro framework web Flask que faz a conexão do retorno das funções dos módulos com a página web. A estrutura da página web foi feita de forma simplificada, separando os dados impressos em uma tabela com duas colunas.

A saída nesse caso é mostrada abaixo (clique na imagem para abrir o site).

[![Sem título](https://user-images.githubusercontent.com/29824937/100823011-378e1680-3432-11eb-9e07-ef8a19d7ae0e.png)](http://juliano.pythonanywhere.com/)
