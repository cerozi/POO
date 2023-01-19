import time

class Elevador:

    def __init__(self) -> None:
        self.__andares = [i for i in range(1, 16)]
        self.__andar_atual = 1

    def __movimentar(self, andar: int) -> None:

        _step = 1 if (andar > self.__andar_atual) else -1 

        for i in range(self.__andar_atual, andar, _step):
            print(f"Andar {i}...")
            time.sleep(1)

        print("Chegamos! ")
        self.__set_andar_atual(andar)

    def __set_andar_atual(self, andar: int) -> None:
        self.__andar_atual = andar

    def transportar(self, andar: int) -> None:

        if andar not in self.__andares:
            msg = "Digite um andar válido. "
            print(msg)
        else:
            self.__movimentar(andar)

    def ligar(self) -> None:

        while (True):
            andar = int(input('Defina um andar: '))
            self.transportar(andar)

    