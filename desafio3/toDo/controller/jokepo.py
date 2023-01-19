from model.choices import IChoice
from model.player import Player

class Jokenpo:

    def __init__(self, first_player: Player, sec_player: Player) -> None:
        self.__first_player = first_player
        self.__sec_player = sec_player

    def __evaluate(self, fplayer_choice: IChoice, splayer_choice: IChoice) -> None:

        _result = (fplayer_choice > splayer_choice)

        if bool(_result == True):
            self.__first_player._increase_score()
        
        if bool(_result == False):
            self.__sec_player._increase_score()

    def play(self) -> None:

        first_choice = self.__first_player.get_random_choice()
        sec_choice = self.__sec_player.get_random_choice()

        self.__evaluate(first_choice, sec_choice)
        return self.__get_final_results()

    def __get_final_results(self) -> str:
        
        fplayer_score = self.__first_player.show_results()
        splayer_score = self.__sec_player.show_results()

        return f"{fplayer_score} \n{splayer_score}"