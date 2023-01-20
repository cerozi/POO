from typing import Iterable, Union
from model.model import IDestino

class GerenciadorFerias:

    def __init__(self, destinos: Iterable[IDestino]) -> None:
        self.__destinos = destinos

    def __validar_destino(self, escolha: int) -> Union[IDestino, None]:
        info = dict((destino.get_info() for destino in self.__destinos))
        return info.get(escolha)

    def __viajar(self, destino: IDestino) -> str:
        return destino.get_atividade()

    def __escolha_invalida(self) -> str:
        return 'Escolha inválida'

    def realizar_atividade(self, escolha: int) -> str:
        destino = self.__validar_destino(escolha)
        if destino is None:
            return self.__escolha_invalida()

        return self.__viajar(destino)