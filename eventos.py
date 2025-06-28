import random
import datetime
from participantes import participantes
from persistencia import salvar_dados, carregar_dados
from utils import (
    obter_entrada,
    remover_duplicatas,
    validar_nao_vazio,
    validar_data_futura,
)

eventos = carregar_dados("eventos.pkl")


def gerar_id_evento():
    """Gera ID único no formato 'E-AAAAMMDD'"""
    hoje = datetime.datetime.now()
    return f"E-{hoje.strftime('%Y%m%d')}-{random.randint(100, 999)}"


def cadastrar_evento():
    """
    Cadastra um novo evento no sistema.
    Este método solicita ao usuário informações sobre o evento, como nome, data,
    tema central e inicializa a lista de participantes como vazia. As entradas
    são validadas para garantir que os dados fornecidos sejam consistentes e válidos.
    Após o cadastro, o evento é salvo em um arquivo persistente e uma mensagem de
    confirmação é exibida.
    O ID do evento é gerado automaticamente.
    Raises:
        ValueError: Se as entradas fornecidas pelo usuário não atenderem aos critérios
                    de validação (ex.: nome vazio, data inválida).
    Side Effects:
        - Adiciona o evento à lista global `eventos`.
        - Salva os dados atualizados no arquivo "eventos.pkl".
        - Exibe uma mensagem de confirmação no console.
    """
    id_evento = gerar_id_evento()

    evento = {
        "id": id_evento,
        "nome": obter_entrada(
            "Nome do evento: ",
            validacao=validar_nao_vazio,
            erro="O nome do evento não pode ser vazio.",
        ),
        "data": obter_entrada(
            "Data (DD/MM/AAAA): ",
            validacao=validar_data_futura,
            erro="Data inválida. Use o formato DD/MM/AAAA e não insira uma data passada.",
        ),
        "tema": obter_entrada(
            "Tema central: ",
            validacao=validar_nao_vazio,
            erro="O tema não pode ser vazio.",
        ),
        "participantes": [],
    }

    eventos.append(evento)
    salvar_dados("eventos.pkl", eventos)
    print(f"✅ Evento '{evento['nome']}' cadastrado! ID: {id_evento}")


def inscrever_participante(id_evento, id_participante):
    """
    Inscreve um participante em um evento, caso ambos existam e o participante
    ainda não esteja inscrito no evento.
    Args:
        id_evento (int): O identificador único do evento.
        id_participante (int): O identificador único do participante.
    Returns:
        bool: Retorna True se o participante foi inscrito com sucesso no evento.
              Retorna False se o evento ou participante não existir, ou se o
              participante já estiver inscrito no evento.
    """
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
    """
    Lista todos os eventos cadastrados.
    Esta função verifica se há eventos cadastrados na lista global `eventos`.
    Caso não existam eventos, exibe uma mensagem informando que não há eventos cadastrados.
    Caso existam, exibe uma lista formatada com as informações de cada evento, incluindo:
    - ID do evento
    - Nome do evento
    - Data do evento
    - Tema do evento
    - Número de participantes do evento
    Retorna:
        None
    """
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
    """
    Remove um evento da lista de eventos com base no ID fornecido.
    Esta função filtra a lista global de eventos, removendo o evento cujo ID
    corresponde ao `id_evento` fornecido. Após a remoção, os dados atualizados
    são salvos em um arquivo chamado "eventos.pkl".
    Args:
        id_evento (int): O identificador único do evento a ser removido.
    Efeitos Colaterais:
        - Modifica a lista global `eventos`, removendo o evento correspondente.
        - Salva a lista atualizada de eventos no arquivo "eventos.pkl".
        - Exibe uma mensagem no console indicando que o evento foi removido.
    Raises:
        Nenhuma exceção é explicitamente tratada nesta função.
    Exemplo:
        >>> remover_evento(3)
        Evento 3 removido!
    """

    global eventos
    eventos = [e for e in eventos if e["id"] != id_evento]
    salvar_dados("eventos.pkl", eventos)
    print(f"Evento {id_evento} removido!")


def atualizar_tema_evento(id_evento, novo_tema):
    """
    Atualiza o tema de um evento específico na lista de eventos.

    Args:
        id_evento (int): O identificador único do evento a ser atualizado.
        novo_tema (str): O novo tema a ser atribuído ao evento.

    Comportamento:
        - Procura na lista de eventos por um evento com o ID correspondente.
        - Se encontrado, atualiza o tema do evento e salva os dados atualizados no arquivo "eventos.pkl".
        - Exibe uma mensagem indicando que o tema foi atualizado com sucesso.
        - Caso o evento não seja encontrado, exibe uma mensagem informando que o evento não foi localizado.

    Retorna:
        None
    """
    for e in eventos:
        if e["id"] == id_evento:
            e["tema"] = novo_tema
            salvar_dados("eventos.pkl", eventos)
            print(f"Tema do evento {id_evento} atualizado!")
            return
    print("Evento não encontrado.")


def gerenciar_atualizacao_tema():
    """Orquestra a atualização de tema de um evento."""
    listar_eventos()
    if not eventos:
        return

    id_evento = input("\nDigite o ID do evento para atualizar o tema: ").strip()
    novo_tema = obter_entrada(
        "Digite o novo tema: ",
        validacao=validar_nao_vazio,
        erro="O tema não pode ser vazio.",
    )
    atualizar_tema_evento(id_evento, novo_tema)


def gerenciar_remocao_evento():
    """Orquestra a remoção de um evento."""
    listar_eventos()
    if not eventos:
        return

    id_evento_remover = input("\nDigite o ID do evento a remover: ").strip()
    remover_evento(id_evento_remover)


def buscar_eventos_por_tema(tema):
    """
    Busca eventos com base no tema fornecido.

    Esta função filtra uma lista de eventos e retorna aqueles cujo tema
    corresponde ao tema especificado, ignorando diferenças de maiúsculas
    e minúsculas.

    Args:
        tema (str): O tema a ser buscado nos eventos.

    Returns:
        list: Uma lista de eventos (dicionários) cujo tema corresponde ao tema fornecido.
    """
    return [e for e in eventos if e["tema"].lower() == tema.lower()]


def buscar_eventos_por_data(data_inicio, data_fim):
    """
    Busca eventos dentro de um intervalo de datas.
    Esta função filtra uma lista de eventos e retorna apenas aqueles cuja data
    está dentro do intervalo especificado por `data_inicio` e `data_fim`.
    Args:
        data_inicio (str): Data inicial do intervalo no formato "DD/MM/AAAA".
        data_fim (str): Data final do intervalo no formato "DD/MM/AAAA".
    Returns:
        list: Uma lista de eventos (dicionários) cujas datas estão dentro do intervalo especificado.
    """

    def converter(data_str):
        return datetime.datetime.strptime(data_str, "%d/%m/%Y")

    inicio = converter(data_inicio)
    fim = converter(data_fim)

    return [e for e in eventos if inicio <= converter(e["data"]) <= fim]


def limpar_duplicatas_em_eventos():
    """
    Remove duplicatas da lista de participantes em cada evento e salva as alterações, se necessário.

    Esta função percorre uma lista global de eventos, verifica a lista de participantes de cada evento
    e remove quaisquer duplicatas. Se alguma alteração for feita, os dados atualizados são salvos em
    um arquivo chamado "eventos.pkl". Caso contrário, uma mensagem indicando que nenhuma duplicata foi
    encontrada é exibida.

    Retorna:
        None
    """
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


def gerenciar_inscricao_evento():
    """
    Gerencia a inscrição de um participante em um evento.
    Solicita ao usuário o ID do evento e o ID do participante, e tenta inscrever
    o participante no evento correspondente. Exibe uma mensagem de sucesso caso
    a inscrição seja realizada com sucesso, ou uma mensagem de erro caso o evento
    ou participante não sejam encontrados, ou se o participante já estiver inscrito.
    Retorna:
        None
    """
    id_evento = input("Digite o ID do evento: ").strip()
    id_participante = input("Digite o ID do participante: ").strip()

    sucesso = inscrever_participante(id_evento, id_participante)

    if sucesso:
        print("✅ Participante inscrito com sucesso!")
    else:
        print(
            "Erro: Participante ou evento não encontrado, ou participante já inscrito."
        )


def exibir_eventos_por_tema():
    """
    Exibe uma lista de eventos filtrados por tema fornecido pelo usuário.
    Solicita ao usuário que insira um tema e busca eventos relacionados a esse tema
    utilizando a função `buscar_eventos_por_tema`. Caso existam eventos correspondentes,
    exibe os detalhes de cada evento encontrado. Caso contrário, informa que nenhum
    evento foi encontrado.
    Returns:
        None
    """
    tema = input("Digite o tema a buscar: ").strip()
    eventos_encontrados = buscar_eventos_por_tema(tema)

    if eventos_encontrados:
        print(f"\n--- Eventos com o tema '{tema}' ---")
        for e in eventos_encontrados:
            print(f"  - {e['nome']} (ID: {e['id']}) - Data: {e['data']}")
        print("------------------------------------")
    else:
        print("Nenhum evento encontrado com esse tema.")


def exibir_eventos_por_data():
    """
    Exibe os eventos cadastrados em um intervalo de datas fornecido pelo usuário.
    Solicita ao usuário que insira uma data inicial e uma data final no formato DD/MM/AAAA.
    Em seguida, busca os eventos que estão dentro desse intervalo de datas e os exibe no console.
    Caso nenhum evento seja encontrado, informa ao usuário.
    Se o formato das datas fornecidas for inválido, exibe uma mensagem de erro.
    Exceções:
        ValueError: Lançada quando as datas fornecidas não estão no formato esperado (DD/MM/AAAA).
    Entradas:
        - Data inicial (str): Data de início do intervalo no formato DD/MM/AAAA.
        - Data final (str): Data de término do intervalo no formato DD/MM/AAAA.
    Saídas:
        - Lista de eventos encontrados no intervalo de datas, exibida no console.
        - Mensagem informativa caso nenhum evento seja encontrado ou o formato das datas seja inválido.
    """
    print("Use o formato DD/MM/AAAA para as datas.")
    data_inicio = input("Data inicial: ").strip()
    data_fim = input("Data final: ").strip()

    try:
        eventos_encontrados = buscar_eventos_por_data(data_inicio, data_fim)
        if eventos_encontrados:
            print(f"\n--- Eventos entre {data_inicio} e {data_fim} ---")
            for e in eventos_encontrados:
                print(f"  - {e['nome']} (ID: {e['id']}) - Data: {e['data']}")
            print("---------------------------------------------")
        else:
            print("Nenhum evento encontrado nesse intervalo de datas.")
    except ValueError:
        print("Formato de data inválido. Por favor, use DD/MM/AAAA.")
