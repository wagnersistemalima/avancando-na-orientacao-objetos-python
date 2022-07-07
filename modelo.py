class Programa:

    def __init__(self, nome: str, ano: int):
        self._nome = nome.title()
        self._ano = ano
        self._likes = 0

    # getters

    @property
    def nome(self):
        return self._nome

    @property
    def ano(self):
        return self._ano

    @property
    def likes(self):
        return self._likes

    # setters

    @nome.setter
    def nome(self, nome: str):
        self._nome = nome.title()

    # metodos

    def dar_likes(self):
        self._likes += 1


class Filme(Programa):

    def __init__(self, nome: str, ano: int, duracao: int):
        self._nome = nome.title()
        self._ano = ano
        self._duracao = duracao
        self._likes = 0

    @property
    def duracao(self):
        return self._duracao


class Serie(Programa):

    def __init__(self, nome: str, ano: int, temporada: int):
        self._nome = nome.title()
        self._ano = ano
        self._temporada = temporada
        self._likes = 0

    # getters

    @property
    def temporada(self):
        return self._temporada


vingadores = Filme("Vingadores guerra infinita", 1981, 160)
print(f"Nome: {vingadores.nome}, Ano: {vingadores.ano}, Duração: {vingadores.duracao} min, likes: {vingadores.likes}")

vingadores.dar_likes()
print("----------> reload")

print(f"Nome: {vingadores.nome}, Ano: {vingadores.ano}, Duração: {vingadores.duracao} min, likes: {vingadores.likes}")

print("---------------------------------------------")

atlanta = Serie("Serie atlanta", 1967, 1)

# imprimir utilizando formatação do python 3.6 em diante
print(f"Nome: {atlanta.nome}, Ano: {atlanta.ano}, Temporada: {atlanta.temporada}, likes: {atlanta.likes}")

atlanta.dar_likes()
atlanta.dar_likes()
print("----------> reload")

print(f"Nome: {atlanta.nome}, Ano: {atlanta.ano}, Temporada: {atlanta.temporada}, likes: {atlanta.likes}")
