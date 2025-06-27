from eventos import eventos
from collections import Counter
from participantes import participantes


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


def exibir_participantes_mais_ativos():
    print("\n--- 👥 Participantes mais Ativos ---")
    dados = participantes_mais_ativos()
    if not dados:
        print("Nenhuma atividade registrada.")
        return

    for pid, total in dados:
        p = next((p for p in participantes if p["id"] == pid), None)
        nome = p["nome"] if p else "Desconhecido"
        print(f"{nome} ({pid}) - {total} evento(s)")


def exibir_temas_mais_frequentes():
    print("\n--- 🌟 Temas mais Frequentes ---")
    dados = temas_mais_frequentes()
    if not dados:
        print("Nenhum evento com tema registrado.")
        return

    for tema, total in dados:
        print(f"{tema} - {total} evento(s)")


def exibir_eventos_risco_cancelamento():
    print("\n--- ⚠️ Eventos com Risco de Cancelamento (poucos participantes) ---")
    dados = eventos_risco_cancelamento()
    if not dados:
        print("Nenhum evento em risco.")
        return

    for e in dados:
        print(f"{e['nome']} ({e['id']}) - {len(e['participantes'])} participante(s)")


def exibir_eventos_por_tema_agrupado():
    print("\n--- 📚 Eventos Agrupados por Tema ---")
    dados = eventos_por_tema()
    if not dados:
        print("Nenhum evento para agrupar.")
        return

    for tema, lista in dados.items():
        print(f"\n{tema}:")
        for nome in lista:
            print(f"  - {nome}")


def exibir_eventos_de_um_participante():
    pid = input("Digite o ID do participante: ").strip()
    dados = eventos_do_participante(pid)

    if dados:
        print(f"\n--- 📅 Eventos do Participante {pid} ---")
        for e in dados:
            print(f"  - {e['nome']} ({e['id']})")
    else:
        print("Nenhum evento encontrado para este participante.")


def exibir_taxa_media_participacao_por_tema():
    print("\n--- 📊 Taxa Média de Participação por Tema ---")
    dados = taxa_media_participacao_por_tema()
    if not dados:
        print("Não há dados para calcular a taxa.")
        return

    for tema, media in dados.items():
        print(f"{tema}: média de {media:.2f} participante(s) por evento")
