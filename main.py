from time import sleep as slp
from datetime import datetime, date, timedelta
import logins, historico, explicar, manipulacaoProdutos, menu, verificarestoque
cores ={
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'azul': '\033[34m',
    'amarelo': '\033[33m',
    'reset': '\033[m',
    'reverse': '\033[7m'
}

while True:
    resultado_login = logins.login()
    if resultado_login:
        setor_atual = resultado_login
        while True:
            op = menu.menu(setor_atual)
            if op == "1":
                verificarestoque.consultarEstoque()
            elif op == "2":
                manipulacaoProdutos.adicionarProduto(setor_atual)
            elif op == "3":
                manipulacaoProdutos.removerProduto(setor_atual)
                slp(1)
            elif op == "4":
                manipulacaoProdutos.atualizarProduto(setor_atual)
            elif op == "5":
                verificarestoque.listarEstoque()
            elif op == "6":
                historico.listarMovimentacoes() #TODO
            elif op == "7":
                explicar.explicarCodigo()
            elif op == "0":
                print(f"{cores['vermelho']}Saindo do sistema...{cores['reset']}")
                slp(1)
                break
            else:
                print(f"{cores['vermelho']}Opção inválida!{cores['reset']}")
    else:
        cont = input(f"{cores['amarelo']}Deseja tentar novamente? {cores['reset']} ({cores['verde']}s{cores['reset']}/{cores['vermelho']}n{cores['reset']}): {cores['reset']}").lower()
        if cont != 's':
            break
