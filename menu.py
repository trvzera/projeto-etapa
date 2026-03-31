from time import sleep as slp

cores ={
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'azul': '\033[34m',
    'amarelo': '\033[33m',
    'reset': '\033[m',
    'reverse': '\033[7m'
}
def menu(setor):
    print(f"\nBem vindo ao sistema de estoque! (USUÁRIO: {cores['amarelo']}{setor.upper()}{cores['reset']})")
    print("--- MENU ---")
    slp(0.2)
    print("1. Consultar estoque")
    slp(0.2)
    print("2. Adicionar produto")
    slp(0.2)
    print("3. Remover produto")
    slp(0.2)
    print("4. Atualizar produto")
    slp(0.2)
    print("5. Listar produtos")
    slp(0.2)
    print("6. Listar Movimentações")
    slp(0.2)
    print("7. Como funciona o código do produto?")
    slp(0.2)
    print(f"{cores['reverse']}0. Sair {cores['reset']}")
    slp(0.2)
    print("-" * 30)
    opcao = input("Digite sua opção: ")
    return opcao