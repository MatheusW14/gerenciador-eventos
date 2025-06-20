from utils import obter_entrada
from participantes import participantes
from persistencia import salvar_dados, carregar_dados
from utils import remover_duplicatas
import datetime
import random

eventos = carregar_dados("eventos.pkl")


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
    salvar_dados("eventos.pkl", eventos)
    print(f"✅ Evento '{evento['nome']}' cadastrado! ID: {id_evento}")


def inscrever_participante(id_evento, id_participante):
    evento = next((e for e in eventos if e["id"] == id_evento), None)
    participante = next((p for p in participantes if p["id"] == id_participante), None)

    if not evento or not participante:
        return False

    if id_participante not in evento["participantes"]:
        evento["participantes"].append(id_participante)
        salvar_dados("eventos.pkl", eventos)
        return True
    return False


def listar_eventos():
    if not eventos:
        print("Nenhum evento cadastrado.")
        return

    print("\n=== Eventos Cadastrados ===")
    for evento in eventos:
        print(
            f"ID: {evento['id']}, Nome: {evento['nome']}, "
            f"Data: {evento['data']}, Tema: {evento['tema']}, "
            f"Participantes: {len(evento['participantes'])}"
        )


def remover_evento(id_evento):
    global eventos
    eventos = [e for e in eventos if e["id"] != id_evento]
    salvar_dados("eventos.pkl", eventos)
    print(f"Evento {id_evento} removido!")


def atualizar_tema_evento(id_evento, novo_tema):
    for e in eventos:
        if e["id"] == id_evento:
            e["tema"] = novo_tema
            salvar_dados("eventos.pkl", eventos)
            print(f"Tema do evento {id_evento} atualizado!")
            return
    print("Evento não encontrado.")


def buscar_eventos_por_tema(tema):
    return [e for e in eventos if e["tema"].lower() == tema.lower()]


def buscar_eventos_por_data(data_inicio, data_fim):
    def converter(data_str):
        return datetime.datetime.strptime(data_str, "%d/%m/%Y")

    inicio = converter(data_inicio)
    fim = converter(data_fim)

    return [e for e in eventos if inicio <= converter(e["data"]) <= fim]


def limpar_duplicatas_em_eventos():
    alterado = False
    for evento in eventos:
        originais = evento["participantes"]
        limpos = remover_duplicatas(originais)
        if len(originais) != len(limpos):
            evento["participantes"] = limpos
            alterado = True
    if alterado:
        salvar_dados("eventos.pkl", eventos)
        print("Duplicatas removidas dos eventos.")
    else:
        print("Nenhuma duplicata encontrada.")
