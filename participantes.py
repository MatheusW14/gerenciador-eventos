from utils import obter_entrada
from persistencia import salvar_dados, carregar_dados
import random

participantes = carregar_dados("participantes.pkl")


def gerar_id_participante():
    return f"P-{random.randint(1000, 9999)}"


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
    salvar_dados("participantes.pkl", participantes)

    print(f"Participante {dados['nome']} cadastrado! ID: {id_participante}")


def remover_participante(lista_participantes, id_participante):
    lista_participantes = [p for p in lista_participantes if p["id"] != id_participante]
    salvar_dados("participantes.pkl", lista_participantes)
    print(f"Participante {id_participante} removido!")
    return lista_participantes


def atualizar_email_participante(id_participante, novo_email):
    for p in participantes:
        if p["id"] == id_participante:
            p["email"] = novo_email
            salvar_dados("participantes.pkl", participantes)
            print(f"Email do participante {id_participante} atualizado!")
            return
    print("Participante não encontrado.")
