from typing import Tuple
from model.elevador import Elevator
from errors.elevator_errors import ElevatorErrors

class ElevatorManager:

    def __init__(self, elevators: Tuple[Elevator]) -> None:
        self.__elevators = elevators

    def __move(self, elevator: Elevator, floor: int) -> str:

        return elevator.move(floor)

    def __get_elevator(self, elevator_id: int) -> Elevator | None:

        for elevator in self.__elevators:
            if elevator.check_id(elevator_id):
                return elevator

    def __valid_floor(self, floor: int) -> bool:

        return 0 < floor < 17

    def call(self, elevator_id: int, floor: int) -> None:
        elevator = self.__get_elevator(elevator_id)
        if not bool(elevator):
            return ElevatorErrors.raise_elevator_error()

        if not self.__valid_floor(floor):
            return ElevatorErrors.raise_floor_error()

        return self.__move(elevator, floor)
