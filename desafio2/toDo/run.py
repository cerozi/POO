from controller.manager import ElevatorManager
from model.elevador import Elevator

elevators = (Elevator(1), Elevator(2))
manager = ElevatorManager(elevators)

while (True):
    elevadorId = int(input('Defina o elevador: '))
    andar = int(input('Defina um andar: '))

    response = manager.call(elevadorId, andar)
    print(response)
    
    print()
