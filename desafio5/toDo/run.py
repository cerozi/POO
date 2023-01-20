from controller.manager import GerenciadorFerias
from model.model import Niteroi, BeloHorizonte, Fortaleza

niteroi = Niteroi(1)
belo_horizonte = BeloHorizonte(2)
fortaleza = Fortaleza(3)

gerenciador = GerenciadorFerias(
    (niteroi, belo_horizonte, fortaleza)
)

while (True):
    destino = None

    destino_da_viajem = int(input('Selecione o destino da viajem: '))
    response = gerenciador.realizar_atividade(destino_da_viajem)
    print(response)

    print()
