import os
import datetime


def obter_entrada(prompt, *args, validacao=None, erro="Entrada inválida", **kwargs):
    """
    Solicita uma entrada do usuário com validação opcional.
    Aceita argumentos adicionais (args, kwargs) para testes ou extensões.
    """
    while True:
        entrada = input(prompt, *args, **kwargs).strip()
        if validacao and not validacao(entrada):
            print(erro)
        else:
            return entrada


def remover_duplicatas(lista):
    """Remove itens duplicados mantendo ordem"""
    return list(dict.fromkeys(lista))


def limpar_terminal():
    """Limpa a tela do terminal, funcionando em Windows, Linux e macOS."""
    os.system("cls" if os.name == "nt" else "clear")


def validar_nao_vazio(texto):
    """Retorna True se o texto não for vazio ou apenas espaços em branco."""
    return bool(texto and not texto.isspace())


def validar_nome_proprio(nome):
    """
    Valida se o nome não é vazio e contém apenas letras e espaços.
    Uma validação simples para nomes próprios.
    """
    if not validar_nao_vazio(nome):
        return False
    return nome.replace(" ", "").isalpha()


def validar_email(email):
    """
    Faz uma validação simples de e-mail.
    Verifica se não é vazio, se tem um '@' e um '.' depois do '@'.
    """
    if not validar_nao_vazio(email):
        return False
    partes = email.split("@")
    if len(partes) != 2:
        return False
    dominio = partes[1]
    return "." in dominio


def validar_data_futura(data_str):
    """
    Verifica se a string é uma data válida no formato DD/MM/AAAA
    e se a data não está no passado.
    """
    try:
        data_evento = datetime.datetime.strptime(data_str, "%d/%m/%Y").date()
        if data_evento < datetime.date.today():
            print("Erro: A data do evento não pode ser no passado.")
            return False
        return True
    except ValueError:
        return False
