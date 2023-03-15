class PascalArray:
    def __init__(self, primeira_posicao, ultima_posicao):
        self._primeira_posicao = primeira_posicao
        self._ultima_posicao = ultima_posicao
        self._length = (self._ultima_posicao - self._primeira_posicao) + 1
        self._array = self._length * []

    def atribuir(self, valor, posicao):
        try:
            self._array[posicao - self._primeira_posicao] = valor
        except ValueError:
            return ('Posição fora da lista')


    def acessar(self, posicao):
        if (posicao - self._primeira_posicao < 0) :
            return ('Posição fora da lista')
        return self._array[posicao - self._primeira_posicao]