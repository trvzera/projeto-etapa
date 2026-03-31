import arquivosjson
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
