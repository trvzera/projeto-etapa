import arquivosjson, historico, gerarcodigo
from time import sleep as slp 
from datetime import datetime

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
    
    codigo = gerarcodigo.gerarCodigo(produto, setor, tamanho, pais)
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
    historico.entradas.append({
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
            historico.saidas.append({
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
                novo_codigo = gerarcodigo.gerarCodigo(novo_nome, setor_origem, novo_tam, novo_pais)
                
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
                historico.alteracoes.append({
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
