from time import sleep as slp
entradas = []
saidas = []
alteracoes = []
cores ={
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'azul': '\033[34m',
    'amarelo': '\033[33m',
    'reset': '\033[m',
    'reverse': '\033[7m'
}

def listarMovimentacoes(): 
    def listarentradas():
        print("\n" + "="*50)
        print("HISTÓRICO DE ENTRADAS".center(50))
        print("="*50)
        if not entradas:
            print(f"{cores['amarelo']}Nenhuma entrada registrada nesta sessão.{cores['reset']}")
        for e in entradas:
            print(f"{e['data_hora']} | {e['codigo']} | {e['produto']:15} | Qtd: {e['quantidade']} | Preço: ${e['preco']:7.2f} | Tam: {e['tamanho']} | País: {e['pais']} | Compatibilidade: {e['compatibilidade']} | Fabricante: {e['fabricante']} | Data Fabricação: {e['data_fabricacao']} | Parte: {e['parte']}")
            print("="*50)
            slp(1)
    def listarsaidas():
        print("\n" + "="*50)
        print("HISTÓRICO DE SAÍDAS".center(50))
        print("="*50)
        if not saidas:
            print(f"{cores['amarelo']}Nenhuma saída registrada nesta sessão.{cores['reset']}")
        for e in saidas:
            print(f"{e['data_hora']} | {e['codigo']} | {e['produto']:15} | Qtd Antiga: {e['quant_antiga']} | Remoção: {e['remocao']} | Qtd: {e['nova_quant']} |")
        print("="*50)
        slp(1)
    def listaratleracoes():
        print("\n" + "="*50)
        print("HISTÓRICO DE ALTERAÇÕES".center(50))
        print("="*50)
        if not alteracoes:
            print(f"{cores['amarelo']}Nenhuma alteração registrada nesta sessão.{cores['reset']}")
        for e in alteracoes:
            print(f"ANTES DA ALTERAÇÃO: \n {e['data_hora']} | {e['codigo_antigo']} | {e['nome_antigo']:15} | Qtd: {e['antiga_qtd']} | Preço: ${e['antigo_preco']} | Tam: {e['antigo_tamanho']} | País: {e['antigo_pais']} | Compatibilidade: {e['antiga_compatibilidade']} | Fabricante: {e['antigo_fabricante']} | Data Fabricação: {e['antiga_data_fabricacao']} | Parte: {e['antiga_parte']}")
            print("="*50)
            print(f"DEPOIS DA ALTERAÇÃO: \n {e['data_hora']} | {e['codigo']} | {e['produto']:15} | Qtd: {e['nova_qtd']} | Preço: ${e['preco']} | Tam: {e['tamanho']} | País: {e['pais']} | Compatibilidade: {e['compatibilidade']} | Fabricante: {e['fabricante']} | Data Fabricação: {e['data_fabricacao']} | Parte: {e['parte']}")
        print("="*50)
        slp(1)
    print("OPÇÕES:")
    slp(0.3)
    print("1 - Listar Entradas")
    slp(0.3)
    print("2 - Listar Saídas")
    slp(0.3)
    print("3 - Listar Alterações")
    slp(0.3)
    print("0 - Voltar")
    slp(0.3)
    op = input("Qual você deseja conferir? ")
    match op:
        case "1":
           listarentradas()
           slp(1)
        case "2":
            listarsaidas()
            slp(1)
        case "3":
            listaratleracoes()
            slp(1)
        case "0":
            print("Voltando ao menu...")
            slp(1)
        case _:
            print(f"{cores['vermelho']}Opção inválida!{cores['reset']}")
            slp(1)