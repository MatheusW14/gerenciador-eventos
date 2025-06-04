from eventos import eventos
from participantes import participantes
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
        if evento["tema"] not in temas:
            temas[evento["tema"]] = []
        temas[evento["tema"]].append(evento["nome"])
    return temas
