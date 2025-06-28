import pickle
import os


def salvar_dados(arquivo, dados):
    """
    Salva os dados fornecidos em um arquivo no formato binário usando o módulo pickle.

    Args:
        arquivo (str): O caminho do arquivo onde os dados serão salvos.
        dados (qualquer tipo serializável): Os dados que serão serializados e salvos no arquivo.

    Raises:
        pickle.PickleError: Se ocorrer um erro durante a serialização dos dados.
        IOError: Se ocorrer um erro ao abrir ou escrever no arquivo.
    """
    with open(arquivo, "wb") as f:
        pickle.dump(dados, f)


def carregar_dados(arquivo):
    """
    Carrega dados de um arquivo binário usando o módulo pickle.

    Args:
        arquivo (str): O caminho para o arquivo que contém os dados serializados.

    Returns:
        list: Os dados carregados do arquivo, ou uma lista vazia se o arquivo não existir.

    Observação:
        Certifique-se de que o arquivo especificado existe e contém dados serializados
        no formato esperado para evitar erros de desserialização.
    """
    if os.path.exists(arquivo):
        with open(arquivo, "rb") as f:
            return pickle.load(f)
    return []
