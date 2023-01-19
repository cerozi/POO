from controller.jokepo import Jokenpo
from model.player import Player

matheus = Player("Matheus")
bob = Player("Bob")

jokenpo = Jokenpo(matheus, bob)

while (True):
    
    input()
    result = jokenpo.play()
    print(result)
