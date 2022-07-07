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

    def imprime(self):
        print(f"{self._nome} - {self._ano} - {self._likes} likes")


class Filme(Programa):

    def __init__(self, nome: str, ano: int, duracao: int):
        super().__init__(nome, ano)
        self._duracao = duracao

    @property
    def duracao(self):
        return self._duracao

    def imprime(self):
        print(f"{self._nome} - {self._ano} - {self._duracao} min - {self._likes} likes")


class Serie(Programa):

    def __init__(self, nome: str, ano: int, temporada: int):
        super().__init__(nome, ano)
        self._temporada = temporada

    # getters

    @property
    def temporada(self):
        return self._temporada

    def imprime(self):
        print(f"{self._nome} - {self._ano} - {self._temporada} temporadas - {self._likes} likes")


vingadores = Filme("Vingadores guerra infinita", 1981, 160)

vingadores.dar_likes()

print(f"{vingadores.nome} - {vingadores.duracao} - {vingadores.likes}")
print("---------------------------------------------")

atlanta = Serie("Serie atlanta", 1967, 1)

atlanta.dar_likes()
atlanta.dar_likes()

print(f"{atlanta.nome} - {atlanta.temporada} - {atlanta.likes}")

print("---------------------------------------------")

filmes_series = [vingadores, atlanta]
print(filmes_series)

for programa in filmes_series:

    programa.imprime()

