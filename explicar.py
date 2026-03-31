from time import sleep as slp

cores ={
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'azul': '\033[34m',
    'amarelo': '\033[33m',
    'reset': '\033[m',
    'reverse': '\033[7m'
}
def explicarCodigo():
    print("\n--- COMO FUNCIONA O CÓDIGO DO PRODUTO ---")
    slp(0.5)
    print(f"{cores['azul']}O código é gerado automaticamente:{cores['reset']}")
    slp(0.5)
    print(f"{cores['reverse']}1. [XX] - Primeiras 2 letras do nome{cores['reset']}")
    slp(0.5)
    print(f"{cores['reverse']}2. [-]  - Separador{cores['reset']}")
    slp(0.5)
    print(f"{cores['reverse']}3. [S]  - Letra inicial do Setor (A=Interno, B=Lataria, C=Mecanica, D=Eletrico){cores['reset']}")
    slp(0.5)
    print(f"{cores['reverse']}4. [T]  - Letra do Tamanho (P, M, G){cores['reset']}")
    slp(0.5)
    print(f"{cores['reverse']}5. [PP] - Primeiras 2 letras do País{cores['reset']}")
    slp(0.5)
    print(f"{cores['reverse']}Exemplo: BA-DMBR -> Bateria, Setor D (Elét.), Médio, BRasil{cores['reset']}")
    print("-" * 40)
    slp(2)
