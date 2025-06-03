from utils import obter_entrada
import random


def gerar_id_participante():
    return f"P-{random.randint(1000,9999)}"
