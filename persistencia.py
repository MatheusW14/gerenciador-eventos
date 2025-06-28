import pickle
import os


def salvar_dados(arquivo, dados):
    with open(arquivo, "wb") as f:
        pickle.dump(dados, f)


def carregar_dados(arquivo):
    if os.path.exists(arquivo):
        with open(arquivo, "rb") as f:
            return pickle.load(f)
    return []
