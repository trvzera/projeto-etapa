
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