from .choices import JokenpoChoices, IChoice
import random

class Player:

    def __init__(self, name: str) -> None:
        self.__name = name
        self.__score = 0

    def get_random_choice(self) -> IChoice:
        choice = random.choice(JokenpoChoices.CHOICES)
        print(f"{self.__name}: {choice}")

        return choice

    def _increase_score(self) -> None:
        self.__score += 1

    def show_results(self) -> str:
        return f"{self.__name}: {self.__score}"