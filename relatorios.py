from eventos import eventos
from collections import Counter


def participantes_mais_ativos():
    contagem = Counter()
    for evento in eventos:
        for id_participante in evento["participantes"]:
            contagem[id_participante] += 1
    return contagem.most_common(5)


def temas_mais_frequentes():
    temas = [evento["tema"] for evento in eventos]
    return Counter(temas).most_common(3)


def eventos_risco_cancelamento(limite=2):
    return [e for e in eventos if len(e["participantes"]) < limite]


def eventos_por_tema():
    temas = {}
    for evento in eventos:
        temas.setdefault(evento["tema"], []).append(evento["nome"])
    return dict(sorted(temas.items()))


def eventos_do_participante(id_participante):
    return [evento for evento in eventos if id_participante in evento["participantes"]]


def taxa_media_participacao_por_tema():
    temas = {}
    for evento in eventos:
        tema = evento["tema"]
        temas.setdefault(tema, []).append(len(evento["participantes"]))

    return {
        tema: round(sum(valores) / len(valores), 2) for tema, valores in temas.items()
    }
