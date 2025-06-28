import random
from utils import obter_entrada, validar_nao_vazio, validar_nome_proprio, validar_email
from persistencia import salvar_dados, carregar_dados


participantes = carregar_dados("participantes.pkl")


def gerar_id_participante():
    """
    Gera um identificador único para um participante.

    O identificador gerado segue o formato "P-" seguido de um número aleatório
    de 4 dígitos no intervalo de 1000 a 9999.

    Returns:
        str: O identificador único do participante no formato "P-XXXX".
    """
    return f"P-{random.randint(1000, 9999)}"


def cadastrar_participante():
    """
    Cadastra um novo participante no sistema.
    Solicita ao usuário as informações necessárias para o cadastro de um participante,
    incluindo nome completo, e-mail e preferências temáticas. Valida as entradas fornecidas
    e armazena os dados do participante em uma lista global. Os dados são persistidos em
    um arquivo utilizando o formato pickle.
    Steps:
    1. Gera um ID único para o participante.
    2. Solicita e valida o nome completo do participante.
    3. Solicita e valida o e-mail do participante.
    4. Solicita e processa as preferências temáticas do participante.
    5. Adiciona o participante à lista global de participantes.
    6. Salva os dados atualizados no arquivo "participantes.pkl".
    7. Exibe uma mensagem de sucesso com o nome e ID do participante cadastrado.
    Raises:
        ValueError: Se as entradas fornecidas pelo usuário não forem válidas.
    Note:
        As funções auxiliares `gerar_id_participante`, `obter_entrada`, `validar_nome_proprio`,
        `validar_email`, `validar_nao_vazio`, `salvar_dados` e a lista global `participantes`
        devem estar definidas no escopo do programa para que esta função funcione corretamente.
    """
    id_participante = gerar_id_participante()

    dados = {
        "nome": obter_entrada(
            "Nome Completo: ",
            validacao=validar_nome_proprio,
            erro="Nome inválido. Use apenas letras e espaços.",
        ),
        "email": obter_entrada(
            "E-mail: ", validacao=validar_email, erro="Formato de e-mail inválido."
        ),
        "preferencias": [
            pref.strip()
            for pref in obter_entrada(
                "Preferências temáticas (separadas por vírgula): ",
                validacao=validar_nao_vazio,
                erro="As preferências não podem ficar em branco.",
            ).split(",")
        ],
    }

    participantes.append({"id": id_participante, **dados})
    salvar_dados("participantes.pkl", participantes)
    print(f"✅ Participante {dados['nome']} cadastrado! ID: {id_participante}")


def listar_participantes():
    """
    Exibe a lista de participantes cadastrados.

    Esta função imprime no console uma lista de participantes cadastrados.
    Caso não haja participantes cadastrados, uma mensagem informativa será exibida.

    Retorno:
        None
    """
    print("\n--- Participantes cadastrados ---")
    if not participantes:
        print("Nenhum participante cadastrado.")
        return
    for p in participantes:
        print(f"{p['id']}: {p['nome']} - {p['email']}")


def remover_participante():
    """
    Remove um participante da lista de participantes com base no ID fornecido.
    Esta função exibe a lista atual de participantes, solicita ao usuário o ID
    do participante que deseja remover e, em seguida, remove o participante correspondente
    da lista. Se o participante for removido com sucesso, os dados atualizados são salvos
    em um arquivo. Caso contrário, uma mensagem de erro é exibida.
    Exibe:
        - Uma lista de participantes com seus IDs e nomes.
        - Mensagem de sucesso ao remover um participante.
        - Mensagem de erro caso o ID fornecido não seja encontrado.
    Entrada:
        - ID do participante a ser removido (fornecido pelo usuário).
    Efeitos colaterais:
        - Atualiza a lista global `participantes`.
        - Salva os dados atualizados no arquivo "participantes.pkl".
    Retorna:
        None
    """

    print("\n--- Participantes Atuais ---")
    if not participantes:
        print("Nenhum participante cadastrado para remover.")
        return

    for p in participantes:
        print(f"ID: {p['id']}, Nome: {p['nome']}")

    id_para_remover = input(
        "\nDigite o ID do participante que deseja remover: "
    ).strip()

    tamanho_antes = len(participantes)
    participantes[:] = [p for p in participantes if p["id"] != id_para_remover]

    if len(participantes) < tamanho_antes:
        salvar_dados("participantes.pkl", participantes)
        print(f"\n✅ Participante {id_para_remover} removido com sucesso!")
    else:
        print(f"\n❌ Erro: Participante com ID {id_para_remover} não foi encontrado.")


def atualizar_email_participante(id_participante, novo_email):
    """Apenas atualiza o email de um participante, dados o ID e o novo email."""
    for p in participantes:
        if p["id"] == id_participante:
            p["email"] = novo_email
            salvar_dados("participantes.pkl", participantes)
            print(f"\n✅ Email do participante {id_participante} atualizado!")
            return
    print(f"\nParticipante com ID {id_participante} não encontrado.")


def gerenciar_atualizacao_email():
    """
    Orquestra a atualização de email: lista os participantes,
    pede o ID e o novo email, e então chama a função de atualização.
    """
    listar_participantes()

    if not participantes:
        return

    id_p = input("\nDigite o ID do participante para atualizar: ").strip()
    novo_email = obter_entrada(
        "Digite o novo email: ",
        validacao=validar_email,
        erro="Formato de e-mail inválido.",
    )

    atualizar_email_participante(id_p, novo_email)


def exibir_participante_por_id():
    """
    Exibe os detalhes de um participante com base no ID fornecido pelo usuário.
    A função lista todos os participantes cadastrados e solicita ao usuário que insira
    o ID do participante que deseja buscar. Se o participante for encontrado, seus
    detalhes são exibidos. Caso contrário, uma mensagem informando que o participante
    não foi encontrado será exibida.
    Variáveis globais:
        participantes (list): Lista de dicionários contendo os dados dos participantes.
            Cada dicionário deve conter as chaves 'id', 'nome', 'email' e 'preferencias'.
    Entradas:
        ID do participante (str): Identificador único do participante a ser buscado.
    Saídas:
        Exibe no console os detalhes do participante ou uma mensagem de erro caso
        o participante não seja encontrado.
    """
    print("\n--- Participantes Atuais ---")
    if not participantes:
        print("Nenhum participante cadastrado para remover.")
        return

    for p in participantes:
        print(f"ID: {p['id']}, Nome: {p['nome']}")

    id_busca = input("Digite o ID do participante a ser buscado: ").strip()

    p = next((p for p in participantes if p["id"] == id_busca), None)

    if p:
        print("\n--- Detalhes do Participante ---")
        print(f"ID: {p['id']}")
        print(f"Nome: {p['nome']}")
        print(f"Email: {p['email']}")
        print(f"Preferências: {', '.join(p['preferencias'])}")
        print("---------------------------------")
    else:
        print("Participante não encontrado.")
