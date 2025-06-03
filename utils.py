def obter_entrada(prompt, validacao=None, erro="Entrada inválida"):
    """
    Solicita uma entrada do usuário com validação opcional.

    Args:
        prompt (str): Mensagem exibida ao usuário para solicitar a entrada.
        validacao (callable, optional): Função que recebe a entrada como argumento e retorna
            True se a entrada for válida ou False caso contrário. Se None, nenhuma validação será aplicada.
        erro (str, optional): Mensagem de erro exibida ao usuário caso a validação falhe.
            O padrão é "Entrada inválida".

    Returns:
        str: A entrada fornecida pelo usuário, após passar pela validação (se aplicável).
    """
    while True:
        entrada = input(prompt).strip()
        if validacao and not validacao(entrada):
            print(erro)
        else:
            return entrada


def remover_duplicatas(lista):
    """Remove itens duplicados mantendo ordem"""
    return list(dict.fromkeys(lista))
