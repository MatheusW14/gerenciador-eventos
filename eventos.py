from utils import obter_entrada
from participantes import participantes
import datetime
import random

eventos = []


def gerar_id_evento():
    """Gera ID único no formato 'E-AAAAMMDD'"""
    hoje = datetime.datetime.now()
    return f"E-{hoje.strftime('%Y%m%d')}-{random.randint(100, 999)}"


def cadastrar_evento():
    id_evento = gerar_id_evento()

    evento = {
        "id": id_evento,
        "nome": obter_entrada("Nome do evento: "),
        "data": obter_entrada(
            "Data (DD/MM/AAAA): ",
            lambda x: len(x) == 10 and x[2] == "/" and x[5] == "/",
        ),
        "tema": obter_entrada("Tema central: "),
        "participantes": [],
    }

    eventos.append(evento)
    print(f"✅ Evento '{evento['nome']}' cadastrado! ID: {id_evento}")


def inscrever_participante(id_evento, id_participante):
    evento = next((e for e in eventos if e["id"] == id_evento), None)
    participante = next((p for p in participantes if p["id"] == id_participante), None)

    if not evento or not participante:
        return False

    # Verifica duplicidade
    if id_participante not in evento["participantes"]:
        evento["participantes"].append(id_participante)
        return True
    return False
