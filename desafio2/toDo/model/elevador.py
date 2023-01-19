class Elevator:

    def __init__(self, id: int) -> None:
        self.__id = id
        self.__current_floor = 1

    def check_id(self, id: int) -> bool:
        return bool(self.__id == id)

    def move(self, floor: int) -> str:
        self.__set_floor(floor)
        return self.__moving_message()

    def __set_floor(self, floor: int) -> None:
        self.__current_floor = floor

    def __moving_message(self) -> str:
        return f'Elevador {self.__id} indo para o andar {self.__current_floor}'