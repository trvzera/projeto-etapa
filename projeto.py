import json
from time import sleep as slp
from datetime import datetime, date, timedelta

def carregar_json(nome_arquivo, padrao):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print(f"Aviso: Arquivo {nome_arquivo} não encontrado ou corrompido.")
        return padrao

estoque = carregar_json('banco.json', {})
logins = carregar_json('logins.json', {})

entradas = []
saidas = []
alteracoes = []

cores = {
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'azul': '\033[34m',
    'amarelo': '\033[33m',
    'reset': '\033[m',
    'reverse': '\033[7m'
}

def login():
    usuario = input("Digite seu usuário: ")
    senha = input("Digite sua senha: ")
    if (usuario == logins['interno'] and senha == logins['senhaInterno']):
        print(f"{cores['verde']}Login realizado com sucesso!{cores['reset']}")
        slp(1)
        return "INTERNO"
    elif (usuario == logins['lataria'] and senha == logins['senhaLataria']):
        print(f"{cores['verde']}Login realizado com sucesso!{cores['reset']}")
        slp(1)
        return "LATARIA"
    elif (usuario == logins['mecanica'] and senha == logins['senhaMecanica']):
        print(f"{cores['verde']}Login realizado com sucesso!{cores['reset']}")
        slp(1)
        return "MECANICA"
    elif (usuario == logins['eletrico'] and senha == logins['senhaEletrico']):
        print(f"{cores['verde']}Login realizado com sucesso!{cores['reset']}")
        slp(1)  
        return "ELETRICO"
    elif (usuario == logins['admin'] and senha == logins['senhaAdmin']):
        print(f"{cores['verde']}Login realizado com sucesso!{cores['reset']}")
        slp(1)
        return "ADMIN"
    else:
        print(f"{cores['vermelho']}Usuário ou senha inválidos!{cores['reset']}")
        return None

def gerarCodigo(produto, setor, tamanho, pais):
    setor = setor.lower()
    if setor == "interno":
        setorCod = "A"
    elif setor == "lataria":
        setorCod = "B"
    elif setor == "mecanica":
        setorCod = "C"
    elif setor == "eletrico":
        setorCod = "D"
    else:
        return "X"
    
    paisCod = pais[0:2].upper()
    codigo = produto[0:2].upper() + "-" + setorCod + tamanho[0:1].upper() + paisCod
    return codigo

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

def adicionarProduto(usuario_logado):
    produto = input("Digite o nome do produto: ")
    ja_existe = False
    for item in estoque.values():
        if item['produto'].lower() == produto.lower():
            ja_existe = True
            break
    if ja_existe:
        print(f"{cores['vermelho']}Produto já cadastrado!{cores['reset']}")
        return
    setor = input("Digite o setor responsável (interno, lataria, mecanica, eletrico): ").lower()
    if setor != usuario_logado.upper() and usuario_logado != "ADMIN":
        print(f"{cores['vermelho']}Você não tem permissão para o setor '{setor}'! Seu setor é '{usuario_logado}'.{cores['reset']}")
        return
    quantidade = int(input("Digite a quantidade: "))
    preco = float(input("Digite o preço: "))
    tamanho = input("Digite o tamanho (P, M, G): ").upper()
    pais = input("Digite o país de origem: ").upper()
    print("Tipos de carro: E (Esportivo), C (Comum), U (SUV), M (Master)")
    compatibilidade = input("Digite a compatibilidade (E/C/U/M): ").upper()
    fabricante = input("Digite o fabricante: ").upper()
    data_fab = input("Digite a data de fabricação (AAAA-MM-DD): ")
    parte = input("Digite a parte do veículo (Ex: painel, motor): ").upper()
    
    codigo = gerarCodigo(produto, setor, tamanho, pais)
    estoque[codigo] = {
        "produto": produto, 
        "quantidade": quantidade, 
        "preco": preco, 
        "tamanho": tamanho, 
        "pais": pais,
        "compatibilidade": compatibilidade,
        "setor": setor.upper(),
        "fabricante": fabricante,
        "data_fabricacao": data_fab,
        "parte": parte
    }
    data_hora = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    entradas.append({
        "data_hora": data_hora,         
        "codigo": codigo,
        "produto": produto,
        "quantidade": quantidade,
        "preco": preco,
        "tamanho": tamanho,
        "pais": pais,
        "compatibilidade": compatibilidade,
        "setor": setor.upper(),
        "fabricante": fabricante,
        "data_fabricacao": data_fab,
        "parte": parte
    })
    print(f"{cores['verde']}Produto adicionado com sucesso! Código: {codigo}{cores['reset']}")
    slp(1)
    return

def removerProduto(usuario_logado):
    termo = input("Digite o código ou nome do produto: ").upper()
    info = None
    
    if termo in estoque:
        info = estoque[termo]
    else:
        for cod, dados in estoque.items():
            if dados['produto'].upper() == termo:
                info = dados
                codigo_produto = cod  
                break
    
    if info:
        print(f"{cores['verde']}Produto encontrado: {info['produto']} | Qtd atual: {info['quantidade']}{cores['reset']}")
        if info['setor'] != usuario_logado.upper() and usuario_logado != "ADMIN":
            print(f"{cores['vermelho']}Você não tem permissão para o setor '{info['setor']}'! Seu setor é '{usuario_logado}'.{cores['reset']}")
        else:
            quantidade = int(input("Digite a quantidade a ser removida: "))
            quant_antiga = info['quantidade']
            if quantidade > info['quantidade']:
                print(f"{cores['vermelho']}Erro: Quantidade solicitada maior que o estoque disponível!{cores['reset']}")
                return
            info['quantidade'] -= quantidade
            print(f"{cores['verde']}Remoção realizada! Nova quantidade de {info['produto']}: {info['quantidade']}{cores['reset']}")
            data_hora = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
            saidas.append({
                "codigo": codigo_produto,
                "produto": info['produto'],
                "data_hora": data_hora,
                "nova_quant": info['quantidade'],
                "remocao": quantidade,
                "quant_antiga": quant_antiga
            })
    else:
        print(f"{cores['vermelho']}Erro: Produto não encontrado!{cores['reset']}")

def atualizarProduto(usuario_logado):
    termo = input("Digite o código ou nome do produto que deseja atualizar: ").upper()
    info = None
    codigo_antigo = None

    if termo in estoque:
        info = estoque[termo]
        codigo_antigo = termo
    else:
        for cod, dados in estoque.items():
            if dados['produto'].upper() == termo:
                info = dados
                codigo_antigo = cod
                break

        if info['setor'] != usuario_logado.upper() and usuario_logado != "ADMIN":
            print(f"{cores['vermelho']}Você não tem permissão para o setor '{info['setor']}'! Seu setor é '{usuario_logado}'.{cores['reset']}")
        else:
            nome_antigo = info['produto']
            quantidade_antiga = info['quantidade']
            preco_antigo = info['preco']
            tamanho_antigo = info['tamanho']
            pais_antigo = info['pais']
            compat_antigo = info['compatibilidade']
            setor_antigo = info['setor']
            fabricante_antigo = info['fabricante']
            datafab_antiga = info['data_fabricacao']
            parte_antiga = info['parte']
            if info:
                novo_nome = input(f"Novo nome (atual: {info['produto']}): ")
                if not novo_nome:
                    novo_nome = info['produto']
                    
                nova_qtd = input(f"Nova quantidade (atual: {info['quantidade']}): ")
                if nova_qtd:
                    nova_qtd = int(nova_qtd)
                else:
                    nova_qtd = info['quantidade']
                    
                novo_preco = input(f"Novo preço (atual: {info['preco']}): ")
                if novo_preco:
                    novo_preco = float(novo_preco)
                else:
                    novo_preco = info['preco']
                    
                novo_tam = input(f"Novo tamanho (atual: {info.get('tamanho', '-')}) (P, M, G): ").upper()
                if not novo_tam:
                    novo_tam = info.get('tamanho', '-')
                    
                novo_pais = input(f"Novo país (atual: {info.get('pais', '-')}): ").upper()
                if not novo_pais:
                    novo_pais = info.get('pais', '-')
                
                compat_atual = info.get('compatibilidade', '-')
                nova_compat = input(f"Nova compatibilidade (atual: {compat_atual}) (E - Esportivo / C - Comum / U - SUV / M - Master): ").upper()
                if not nova_compat:
                    nova_compat = compat_atual
                
                novo_fabricante = input(f"Novo fabricante (atual: {info.get('fabricante', '-')}): ")
                if not novo_fabricante:
                    novo_fabricante = info.get('fabricante', '-')
                
                nova_datafab = input(f"Nova data de fabricação (atual: {info.get('data_fabricacao', '-')}) (AAAA-MM-DD): ")
                if not nova_datafab:
                    nova_datafab = info.get('data_fabricacao', '-')
                
                nova_parte = input(f"Nova parte (atual: {info.get('parte', '-')}): ").upper()
                if not nova_parte:
                    nova_parte = info.get('parte', '-')
                
                setor_origem = info['setor']
                novo_codigo = gerarCodigo(novo_nome, setor_origem, novo_tam, novo_pais)
                
                if novo_codigo != codigo_antigo:
                    estoque.pop(codigo_antigo)
                    
                estoque[novo_codigo] = {
                    "produto": novo_nome,
                    "quantidade": nova_qtd,
                    "preco": novo_preco,
                    "tamanho": novo_tam,
                    "pais": novo_pais,
                    "compatibilidade": nova_compat,
                    "setor": info.get('setor', setor_origem.upper()),
                    "fabricante": info.get('fabricante', '-'),
                    "data_fabricacao": info.get('data_fabricacao', '-'),
                    "parte": info.get('parte', '-')
                }
                alteracoes.append({
                    "codigo": novo_codigo,
                    "codigo_antigo": codigo_antigo,
                    "produto": novo_nome,
                    "nome_antigo": nome_antigo,
                    "data_hora": datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
                    "nova_qtd": nova_qtd,
                    "antiga_qtd": quantidade_antiga,
                    "preco": novo_preco,
                    "antigo_preco": preco_antigo,
                    "tamanho": novo_tam,
                    "antigo_tamanho": tamanho_antigo,
                    "pais": novo_pais,
                    "antigo_pais": pais_antigo,
                    "compatibilidade": nova_compat,
                    "antiga_compatibilidade": compat_antigo,
                    "setor": info.get('setor', setor_origem.upper()),
                    "fabricante": info.get('fabricante', '-'),
                    "antigo_fabricante": fabricante_antigo,
                    "data_fabricacao": info.get('data_fabricacao', '-'),
                    "antiga_data_fabricacao": datafab_antiga,
                    "parte": info.get('parte', '-'),
                    "antiga_parte": parte_antiga
                })
                print(f"{cores['verde']}Produto atualizado com sucesso! Novo código: {novo_codigo}{cores['reset']}")
            else:
                print(f"{cores['vermelho']}Produto não encontrado!{cores['reset']}")

def listarEstoque():
    print("\n" + "="*50)
    print("ESTOQUE ATUAL".center(50))
    print("="*50)
    for codigo, info in estoque.items():
        slp(0.1)
        print(f"[{codigo}] {info['produto']:20} | Qtd: {info['quantidade']:3} | Preço: ${info['preco']:7.2f} | Tam: {info['tamanho']} | País: {info['pais']} | Comp: {info['compatibilidade']} | Fab: {info['fabricante']} | Data Fab: {info['data_fabricacao']} | Parte: {info['parte']}")
    print("="*50)

def listarMovimentacoes(): #TODO
    print("OPÇÕES: \n 1 - Entradas \n 2 - Saídas \n 3 - Alterações")
    op = input("Qual você deseja conferir? ")
    match op:
        case "1":
            print("\n" + "="*50)
            print("HISTÓRICO DE ENTRADAS".center(50))
            print("="*50)
            if not entradas:
                print(f"{cores['amarelo']}Nenhuma entrada registrada nesta sessão.{cores['reset']}")
            for e in entradas:
                print(f"{e['data_hora']} | {e['codigo']} | {e['produto']:15} | Qtd: {e['quantidade']} | Preço: ${e['preco']:7.2f} | Tam: {e['tamanho']} | País: {e['pais']} | Compatibilidade: {e['compatibilidade']} | Fabricante: {e['fabricante']} | Data Fabricação: {e['data_fabricacao']} | Parte: {e['parte']}")
            print("="*50)
            slp(1)
        case "2":
            print("\n" + "="*50)
            print("HISTÓRICO DE SAÍDAS".center(50))
            print("="*50)
            if not saidas:
                print(f"{cores['amarelo']}Nenhuma saída registrada nesta sessão.{cores['reset']}")
            for e in saidas:
                print(f"{e['data_hora']} | {e['codigo']} | {e['produto']:15} | Qtd Antiga: {e['quant_antiga']} | Remoção: {e['remocao']} | Qtd: {e['nova_quant']} |")
            print("="*50)
            slp(1)
        case "3":
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



while True:
    resultado_login = login()
    if resultado_login:
        setor_atual = resultado_login
        while True:
            op = menu(setor_atual)
            if op == "1":
                consultarEstoque()
            elif op == "2":
                adicionarProduto(setor_atual)
            elif op == "3":
                removerProduto(setor_atual)
                slp(1)
            elif op == "4":
                atualizarProduto(setor_atual)
            elif op == "5":
                listarEstoque()
            elif op == "6":
                listarMovimentacoes() #TODO
            elif op == "7":
                explicarCodigo()
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
