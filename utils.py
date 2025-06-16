def obter_entrada(prompt, *args, validacao=None, erro="Entrada inválida", **kwargs):
    """
    Solicita uma entrada do usuário com validação opcional.
    Aceita argumentos adicionais (args, kwargs) para testes ou extensões.
    """
    while True:
        entrada = input(prompt, *args, **kwargs).strip()
        if validacao and not validacao(entrada):
            print(erro)
        else:
            return entrada


def remover_duplicatas(lista):
    """Remove itens duplicados mantendo ordem"""
    return list(dict.fromkeys(lista))
