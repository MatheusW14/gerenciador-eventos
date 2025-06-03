from utils import obter_entrada
import random

participantes = []


def gerar_id_participante():
    return f"P-{random.randint(1000,9999)}"


def cadastrar_participante():
    id_participante = gerar_id_participante()

    dados = {
        "nome": obter_entrada("Nome Completo: "),
        "email": obter_entrada("E-mail: "),
        "preferencias": obter_entrada(
            "Preferências temáticas (separadas por vírgula): "
        ).split(","),
    }

    participantes.append({"id": id_participante, **dados})
    print(f"✅ Participante {dados['nome']} cadastrado! ID: {id_participante}")
