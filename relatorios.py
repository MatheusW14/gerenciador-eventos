from eventos import eventos
from collections import Counter
from participantes import participantes


def participantes_mais_ativos():
    """
    Retorna os 5 participantes mais ativos em eventos.

    A função percorre uma lista de eventos, contabilizando a frequência de participação
    de cada participante. Utiliza a classe Counter para contar as ocorrências de cada
    participante e retorna os 5 participantes com maior número de participações.

    Retorna:
        list: Uma lista de tuplas contendo os 5 participantes mais ativos e suas respectivas
        contagens de participações, ordenados em ordem decrescente de frequência.
    """
    contagem = Counter()
    for evento in eventos:
        for id_participante in evento["participantes"]:
            contagem[id_participante] += 1
    return contagem.most_common(5)


def temas_mais_frequentes():
    """
    Retorna os três temas mais frequentes em uma lista de eventos.

    A função percorre uma lista de eventos, extrai os temas de cada evento
    e calcula a frequência de ocorrência de cada tema. Em seguida, retorna
    os três temas mais comuns e suas respectivas contagens.

    Retorna:
        list: Uma lista de tuplas contendo os três temas mais frequentes e
        suas respectivas contagens, no formato [(tema1, contagem1), (tema2, contagem2), (tema3, contagem3)].

    Exemplo:
        >>> eventos = [{"tema": "Tecnologia"}, {"tema": "Saúde"}, {"tema": "Tecnologia"}]
        >>> temas_mais_frequentes()
        [("Tecnologia", 2), ("Saúde", 1)]
    """
    temas = [evento["tema"] for evento in eventos]
    return Counter(temas).most_common(3)


def eventos_risco_cancelamento(limite=2):
    """
    Retorna uma lista de eventos que estão em risco de cancelamento devido a um número insuficiente de participantes.

    Um evento é considerado em risco de cancelamento se o número de participantes for menor que o limite especificado.

    Args:
        limite (int, opcional): O número mínimo de participantes necessário para que um evento não seja considerado em risco.
                                O valor padrão é 2.

    Returns:
        list: Uma lista de eventos (dicionários) que possuem menos participantes do que o limite especificado.
    """
    return [e for e in eventos if len(e["participantes"]) < limite]


def eventos_por_tema():
    """
    Organiza eventos por tema.

    Esta função percorre uma lista de eventos e agrupa os nomes dos eventos
    por tema. O resultado é um dicionário onde as chaves são os temas e os
    valores são listas contendo os nomes dos eventos associados a cada tema.
    O dicionário final é ordenado alfabeticamente pelas chaves (temas).

    Returns:
        dict: Um dicionário ordenado onde as chaves são os temas e os valores
        são listas de nomes de eventos associados a cada tema.
    """
    temas = {}
    for evento in eventos:
        temas.setdefault(evento["tema"], []).append(evento["nome"])
    return dict(sorted(temas.items()))


def eventos_do_participante(id_participante):
    """
    Retorna uma lista de eventos nos quais um participante específico está inscrito.

    Args:
        id_participante (int): O identificador único do participante.

    Returns:
        list: Uma lista de dicionários representando os eventos em que o participante está incluído.
    """
    return [evento for evento in eventos if id_participante in evento["participantes"]]


def taxa_media_participacao_por_tema():
    """
    Calcula a taxa média de participação por tema de eventos.
    Esta função percorre uma lista de eventos, agrupando os temas e calculando
    a média de participantes para cada tema. O resultado é um dicionário onde
    as chaves são os temas e os valores são as médias arredondadas para duas
    casas decimais.
    Returns:
        dict: Um dicionário contendo os temas como chaves e as taxas médias de
        participação como valores.
    """
    temas = {}
    for evento in eventos:
        tema = evento["tema"]
        temas.setdefault(tema, []).append(len(evento["participantes"]))

    return {
        tema: round(sum(valores) / len(valores), 2) for tema, valores in temas.items()
    }


def exibir_participantes_mais_ativos():
    """
    Exibe uma lista dos participantes mais ativos em eventos.
    Esta função utiliza os dados retornados pela função `participantes_mais_ativos`
    para listar os participantes que mais participaram de eventos, ordenados pelo
    número total de eventos. Caso não haja atividades registradas, uma mensagem
    informativa será exibida.
    Para cada participante listado, são exibidos:
    - Nome do participante (ou "Desconhecido" caso o participante não seja encontrado).
    - ID do participante.
    - Total de eventos em que participou.
    Retorna:
        None: Esta função apenas exibe informações no console.
    """
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
    """
    Exibe os temas mais frequentes registrados em eventos.
    Esta função utiliza a função `temas_mais_frequentes` para obter os dados
    dos temas mais frequentes e os exibe no console. Caso não haja dados
    disponíveis, uma mensagem informativa será exibida.
    Saída:
        - Lista de temas com a quantidade de eventos associados a cada tema.
        - Mensagem informativa caso não existam eventos registrados.
    """
    print("\n--- 🌟 Temas mais Frequentes ---")
    dados = temas_mais_frequentes()
    if not dados:
        print("Nenhum evento com tema registrado.")
        return

    for tema, total in dados:
        print(f"{tema} - {total} evento(s)")


def exibir_eventos_risco_cancelamento():
    """
    Exibe uma lista de eventos que estão em risco de cancelamento devido ao baixo número de participantes.
    A função utiliza a função `eventos_risco_cancelamento` para obter os dados dos eventos com poucos participantes.
    Caso não haja eventos em risco, uma mensagem informativa será exibida.
    Para cada evento em risco, são exibidos o nome, o ID e o número de participantes.
    Retorno:
        None: A função apenas exibe informações no console e não retorna nenhum valor.
    """
    print("\n--- ⚠️ Eventos com Risco de Cancelamento (poucos participantes) ---")
    dados = eventos_risco_cancelamento()
    if not dados:
        print("Nenhum evento em risco.")
        return

    for e in dados:
        print(f"{e['nome']} ({e['id']}) - {len(e['participantes'])} participante(s)")


def exibir_eventos_por_tema_agrupado():
    """
    Exibe uma lista de eventos agrupados por tema.
    Esta função utiliza os dados retornados pela função `eventos_por_tema` para
    exibir os eventos organizados por tema. Caso não existam eventos disponíveis
    para agrupar, uma mensagem informativa será exibida.
    Saída:
        - Para cada tema, exibe o nome do tema seguido por uma lista de eventos
          associados a ele.
        - Caso não existam eventos, exibe "Nenhum evento para agrupar.".
    """
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
    """
    Exibe os eventos associados a um participante específico.
    Solicita ao usuário o ID de um participante, busca os eventos relacionados
    a esse participante e exibe uma lista formatada com os nomes e IDs dos eventos.
    Caso nenhum evento seja encontrado, informa ao usuário.
    Retorno:
        None
    """
    pid = input("Digite o ID do participante: ").strip()
    dados = eventos_do_participante(pid)

    if dados:
        print(f"\n--- 📅 Eventos do Participante {pid} ---")
        for e in dados:
            print(f"  - {e['nome']} ({e['id']})")
    else:
        print("Nenhum evento encontrado para este participante.")


def exibir_taxa_media_participacao_por_tema():
    """
    Exibe a taxa média de participação por tema com base nos dados fornecidos.
    Esta função chama a função `taxa_media_participacao_por_tema` para obter os dados
    de participação média por tema. Caso não existam dados disponíveis, uma mensagem
    informativa será exibida. Caso contrário, os temas e suas respectivas médias de
    participantes por evento serão apresentados no console.
    Retorno:
        None: Esta função não retorna valores, apenas exibe informações no console.
    """
    print("\n--- 📊 Taxa Média de Participação por Tema ---")
    dados = taxa_media_participacao_por_tema()
    if not dados:
        print("Não há dados para calcular a taxa.")
        return

    for tema, media in dados.items():
        print(f"{tema}: média de {media:.2f} participante(s) por evento")
