import random
from utils import obter_entrada, validar_nao_vazio, validar_nome_proprio, validar_email
from persistencia import salvar_dados, carregar_dados


participantes = {carregar_dados("participantes.pkl")}


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
    for p in participantes:
        print(f"{p['id']}: {p['nome']} - {p['email']}")


def remover_participante(id_participante):

    global participantes

    tamanho_antes = len(participantes)
    participantes = [p for p in participantes if p["id"] != id_participante]

    if len(participantes) < tamanho_antes:
        salvar_dados("participantes.pkl", participantes)
        print(f"Participante {id_participante} removido com sucesso!")
    else:
        print(f"Erro: Participante com ID {id_participante} não foi encontrado.")


def atualizar_email_participante(id_participante, novo_email):
    for p in participantes:
        if p["id"] == id_participante:
            p["email"] = novo_email
            salvar_dados("participantes.pkl", participantes)
            print(f"Email do participante {id_participante} atualizado!")
            return
    print("Participante não encontrado.")


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
