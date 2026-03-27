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

def login():
    usuario = input("Digite seu usuário: ")
    senha = input("Digite sua senha: ")
    if (usuario == logins['interno'] and senha == logins['senhaInterno']):
        print("Login realizado com sucesso!")
        slp(1)
        return "interno"
    elif (usuario == logins['lataria'] and senha == logins['senhaLataria']):
        print("Login realizado com sucesso!")
        slp(1)
        return "lataria"
    elif (usuario == logins['mecanica'] and senha == logins['senhaMecanica']):
        print("Login realizado com sucesso!")
        slp(1)
        return "mecanica"
    elif (usuario == logins['eletrico'] and senha == logins['senhaEletrico']):
        print("Login realizado com sucesso!")
        slp(1)
        return "eletrico"
    elif (usuario == logins['admin'] and senha == logins['senhaAdmin']):
        print("Login realizado com sucesso!")
        slp(1)
        return "admin"
    else:
        print("Usuário ou senha inválidos!")
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
    print(f"\nBem vindo ao sistema de estoque! (USUÁRIO: {setor.upper()})")
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
    print("6. Listar entradas")
    slp(0.2)
    print("7. Como funciona o código do produto?")
    slp(0.2)
    print("0. Sair")
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
                print(f"Preço em Real: R${info['preco'] * taxaReal:.2f}")
            elif info['pais'] == "CHINA":
                print(f"Preço em Yuan: ${info['preco'] * taxaYuan:.2f}")
            elif info['pais'] == "FRANCA":
                print(f"Preço em Euro: ${info['preco'] * taxaEuro:.2f}")
            elif info['pais'] == "CANADA":
                print(f"Preço em Dólar Canadense: ${info['preco'] * taxaDol:.2f}")
    else:
        print("Produto não encontrado!")
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
        print("Produto já cadastrado!")
        return
    setor = input("Digite o setor responsável (interno, lataria, mecanica, eletrico): ").lower()
    if setor != usuario_logado.lower() and usuario_logado != "admin":
        print(f"Você não tem permissão para o setor '{setor}'! Seu setor é '{usuario_logado}'.")
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
        "codigo": codigo,
        "produto": produto,
        "data_hora": data_hora,
        "quantidade": quantidade
    })
    print(f"Produto adicionado com sucesso! Código: {codigo}")
    slp(1)
    return

def removerProduto(usuario_logado):
    termo = input("Digite o código ou nome do produto: ").upper()
    info = None
    
    if termo in estoque:
        info = estoque[termo]
    else:
        for dados in estoque.values():
            if dados['produto'].upper() == termo:
                info = dados
                break
    
    if info:
        print(f"Produto encontrado: {info['produto']} | Qtd atual: {info['quantidade']}")
        quantidade = int(input("Digite a quantidade a ser removida: "))
        if quantidade > info['quantidade']:
            print("Erro: Quantidade solicitada maior que o estoque disponível!")
            return
        info['quantidade'] -= quantidade
        print(f"Remoção realizada! Nova quantidade de {info['produto']}: {info['quantidade']}")
    else:
        print("Erro: Produto não encontrado!")

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
            
        novo_tam = input(f"Novo tamanho (atual: {info.get('tamanho', '-')}, P, M, G): ").upper()
        if not novo_tam:
            novo_tam = info.get('tamanho', '-')
            
        novo_pais = input(f"Novo país (atual: {info.get('pais', '-')}, 2 letras): ").upper()
        if not novo_pais:
            novo_pais = info.get('pais', '-')
        
        compat_atual = info.get('compatibilidade', '-')
        nova_compat = input(f"Nova compatibilidade (atual: {compat_atual}, E - Esportivo / C - Comum / U - SUV / M - Master): ").upper()
        if not nova_compat:
            nova_compat = compat_atual
        
        setor_origem = "interno"
        if codigo_antigo and "-" in codigo_antigo:
            setor_letra = codigo_antigo.split("-")[1][0]
            if setor_letra == "A": setor_origem = "interno"
            elif setor_letra == "B": setor_origem = "lataria"
            elif setor_letra == "C": setor_origem = "mecanica"
        
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
        
        print(f"Produto atualizado com sucesso! Novo código: {novo_codigo}")
    else:
        print("Produto não encontrado!")

def listarEstoque():
    print("\n" + "="*50)
    print("ESTOQUE ATUAL".center(50))
    print("="*50)
    for codigo, info in estoque.items():
        slp(0.1)
        print(f"[{codigo}] {info['produto']:20} | Qtd: {info['quantidade']:3} | Preço: ${info['preco']:7.2f} | Tam: {info['tamanho']} | País: {info['pais']} | Compatibilidade: {info['compatibilidade']} | Fabricante: {info['fabricante']} | Data Fabricação: {info['data_fabricacao']} | Parte: {info['parte']}")
    print("="*50)

def listarEntradas():
    print("\n" + "="*50)
    print("HISTÓRICO DE ENTRADAS".center(50))
    print("="*50)
    if not entradas:
        print("Nenhuma entrada registrada nesta sessão.")
    for e in entradas:
        print(f"{e['data_hora']} | {e['codigo']} | {e['produto']:15} | Qtd: {e['quantidade']}")
    print("="*50)

def explicarCodigo():
    print("\n--- COMO FUNCIONA O CÓDIGO DO PRODUTO ---")
    slp(0.5)
    print("O código é gerado automaticamente:")
    slp(0.3)
    print("1. [XX] - Primeiras 2 letras do nome")
    print("2. [-]  - Separador")
    print("3. [S]  - Letra inicial do Setor (A=Interno, B=Lataria, C=Mecanica, D=Eletrico)")
    print("4. [T]  - Letra do Tamanho (P, M, G)")
    print("5. [PP] - Primeiras 2 letras do País")
    slp(0.3)
    print("Exemplo: BA-DMBR -> Bateria, Setor D (Elét.), Médio, BRasil")
    print("-" * 40)



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
            elif op == "4":
                atualizarProduto(setor_atual)
            elif op == "5":
                listarEstoque()
            elif op == "6":
                listarEntradas()
            elif op == "7":
                explicarCodigo()
            elif op == "0":
                print("Saindo do sistema...")
                slp(1)
                break
            else:
                print("Opção inválida!")
    else:
        cont = input("Deseja tentar novamente? (s/n): ").lower()
        if cont != 's':
            break
