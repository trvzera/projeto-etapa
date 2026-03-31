import arquivosjson, manipulacaoProdutos
from time import sleep as slp
estoque = arquivosjson.carregar_json('banco.json', {})
logins = arquivosjson.carregar_json('logins.json', {})

cores ={
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'azul': '\033[34m',
    'amarelo': '\033[33m',
    'reset': '\033[m',
    'reverse': '\033[7m'
}

def consultarEstoque():
    taxaReal = 5.20
    taxaYuan = 6.91
    taxaEuro =  0.87
    taxaDol = 1.39
    termo = input("Digite o código ou nome do produto: ").upper()
    info = ""
    if termo in estoque:
        info = estoque[termo]
    else:
        for dados in estoque.values():
            if dados['produto'].upper() == termo:
                info = dados
                break
    if info:
        print(f"\nProduto: {info['produto']}")
        slp(0.2)
        print(f"Quantidade: {info['quantidade']}")
        slp(0.2)
        print(f"Preço: ${info['preco']:.2f}")
        slp(0.2)
        print(f"Tamanho: {info.get('tamanho', '-')}")
        slp(0.2)
        print(f"País: {info.get('pais', '-')}")
        slp(0.2)
        compat = info.get('compatibilidade', '-')
        print(f"Compatível com: {compat}")
        slp(0.2)
        print(f"Setor: {info.get('setor', '-')}")
        slp(0.2)
        print(f"Fabricante: {info.get('fabricante', '-')}")
        slp(0.2)
        print(f"Data Fab.: {info.get('data_fabricacao', '-')}")
        slp(0.2)
        print(f"Parte: {info.get('parte', '-')}")
        slp(0.2)
        escolha = input("Deseja fazer a conversao da moeda? (s/n): ").lower()
        if escolha == "s":
            if info['pais'] == "BRASIL":
                print(f"{cores['verde']}Preço em Real: R${info['preco'] * taxaReal:.2f}{cores['reset']}")
            elif info['pais'] == "CHINA":
                print(f"{cores['vermelho']}Preço em Yuan: ${info['preco'] * taxaYuan:.2f}{cores['reset']}")
            elif info['pais'] == "FRANCA":
                print(f"{cores['azul']}Preço em Euro: ${info['preco'] * taxaEuro:.2f}{cores['reset']}")
            elif info['pais'] == "CANADA":
                print(f"{cores['vermelho']}Preço em Dólar Canadense: ${info['preco'] * taxaDol:.2f}{cores['reset']}")
    else:
        print(f"{cores['vermelho']}Produto não encontrado!{cores['reset']}")
    slp(1)
    return

def listarEstoque():
    print("\n" + "="*50)
    print("ESTOQUE ATUAL".center(50))
    print("="*50)
    for codigo, info in estoque.items():
        slp(0.1)
        print(f"[{codigo}] {info['produto']:20} | Qtd: {info['quantidade']:3} | Preço: ${info['preco']:7.2f} | Tam: {info['tamanho']} | País: {info['pais']} | Comp: {info['compatibilidade']} | Fab: {info['fabricante']} | Data Fab: {info['data_fabricacao']} | Parte: {info['parte']}")
    print("="*50)
