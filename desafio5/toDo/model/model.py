from abc import ABC, abstractmethod
from typing import Tuple

class IDestino(ABC):

    def __init__(self, id: int) -> None:
        self.__id = id

    @abstractmethod
    def get_atividade(self) -> str:
        pass

    def get_info(self) -> Tuple:
        return (self.__id, self)

class Niteroi(IDestino):

    def get_atividade(self) -> str:
        return 'Ir para praia.'

class BeloHorizonte(IDestino):

    def get_atividade(self) -> str:
        return 'Visitar Inhotim'

class Fortaleza(IDestino):

    def get_atividade(self) -> str:
        return 'Ir para o BeachPark'

