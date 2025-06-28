import random
from utils import obter_entrada, validar_nao_vazio, validar_nome_proprio, validar_email
from persistencia import salvar_dados, carregar_dados


participantes = carregar_dados("participantes.pkl")


def gerar_id_participante():
    return f"P-{random.randint(1000, 9999)}"


def cadastrar_participante():
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
    print("\n--- Participantes cadastrados ---")
    if not participantes:
        print("Nenhum participante cadastrado.")
        return
    for p in participantes:
        print(f"{p['id']}: {p['nome']} - {p['email']}")


def remover_participante():

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
    """Pede um ID ao usuário, busca o participante e exibe seus detalhes."""
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
