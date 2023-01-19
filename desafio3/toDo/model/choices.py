from abc import ABC, abstractproperty

class IChoice(ABC):

    @abstractproperty
    def NAME(self):
        pass

    def __repr__(self) -> str:
        return self.NAME

class Pedra(IChoice):

    NAME = 'Pedra'

    def __gt__(self, choice: IChoice) -> None:

        if choice.NAME == self.NAME:
            return None

        if choice.NAME == 'Papel':
            return False

        return True


class Papel(IChoice):

    NAME = 'Papel'

    def __gt__(self, choice: IChoice) -> None:

        if choice.NAME == self.NAME:
            return None

        if choice.NAME == 'Tesoura':
            return False

        return True

class Tesoura(IChoice):

    NAME = 'Tesoura'
    
    def __gt__(self, choice: IChoice) -> None:

        if choice.NAME == self.NAME:
            return None

        if choice.NAME == 'Pedra':
            return False

        return True

class JokenpoChoices:

    CHOICES = [Pedra(), Papel(), Tesoura()]
