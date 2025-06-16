from participantes import (
    cadastrar_participante,
    participantes,
    remover_participante,
    atualizar_email_participante,
)
from eventos import (
    cadastrar_evento,
    listar_eventos,
    inscrever_participante,
    remover_evento,
    atualizar_tema_evento,
)
from relatorios import (
    participantes_mais_ativos,
    temas_mais_frequentes,
    eventos_risco_cancelamento,
    eventos_por_tema,
    eventos_do_participante,
)


def mostrar_menu():
    print("\n" + "=" * 50)
    print("SISTEMA DE GERENCIAMENTO DE EVENTOS")
    print("=" * 50)
    print("1. Cadastrar participante")
    print("2. Cadastrar evento")
    print("3. Inscrever participante em evento")
    print("4. Listar eventos")
    print("5. Listar participantes")
    print("6. Buscar participante por ID")
    print("7. Relatórios")
    print("8. Remover participante")
    print("9. Remover evento")
    print("10. Atualizar email do participante")
    print("11. Atualizar tema do evento")
    print("12. Sair")
    print("=" * 50)


def menu_relatorios():
    while True:
        print("\n=== RELATÓRIOS ===")
        print("a - Participantes mais ativos")
        print("b - Temas mais frequentes")
        print("c - Eventos em risco de cancelamento")
        print("d - Eventos por tema")
        print("e - Eventos de um participante")
        print("f - Voltar")

        opcao = input("Escolha uma opção: ").strip().lower()

        if opcao == "a":
            print("\n--- Participantes mais ativos ---")
            for pid, total in participantes_mais_ativos():
                p = next((p for p in participantes if p["id"] == pid), None)
                nome = p["nome"] if p else "Desconhecido"
                print(f"{nome} ({pid}) - {total} evento(s)")
        elif opcao == "b":
            print("\n--- Temas mais frequentes ---")
            for tema, total in temas_mais_frequentes():
                print(f"{tema} - {total} evento(s)")
        elif opcao == "c":
            print("\n--- Eventos com risco de cancelamento ---")
            eventos = eventos_risco_cancelamento()
            if not eventos:
                print("Nenhum evento em risco.")
            for e in eventos:
                print(
                    f"{e['nome']} ({e['id']}) - {len(e['participantes'])} participante(s)"
                )
        elif opcao == "d":
            print("\n--- Eventos por tema ---")
            temas = eventos_por_tema()
            for tema, lista in temas.items():
                print(f"\n{tema}:")
                for nome in lista:
                    print(f"  - {nome}")
        elif opcao == "e":
            pid = input("Digite o ID do participante: ").strip()
            eventos_participante = eventos_do_participante(pid)
            if eventos_participante:
                print(f"\nEventos em que o participante {pid} está inscrito:")
                for e in eventos_participante:
                    print(f"  - {e['nome']} ({e['id']})")
            else:
                print("Nenhum evento encontrado para esse participante.")
        elif opcao == "f":
            break
        else:
            print("Opção inválida.")


def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_participante()
        elif opcao == "2":
            cadastrar_evento()
        elif opcao == "3":
            id_evento = input("ID do evento: ")
            id_participante = input("ID do participante: ")
            sucesso = inscrever_participante(id_evento, id_participante)
            if sucesso:
                print("Participante inscrito com sucesso!")
            else:
                print("Participante ou evento não encontrado.")
        elif opcao == "4":
            listar_eventos()
        elif opcao == "5":
            print("\n--- Participantes cadastrados ---")
            for p in participantes:
                print(f"{p['id']}: {p['nome']} - {p['email']}")
        elif opcao == "6":
            id_busca = input("ID do participante: ").strip()
            p = next((p for p in participantes if p["id"] == id_busca), None)
            if p:
                print(
                    f"ID: {p['id']}\nNome: {p['nome']}\nEmail: {p['email']}\nPreferências: {', '.join(p['preferencias'])}"
                )
            else:
                print("Participante não encontrado.")
        elif opcao == "7":
            menu_relatorios()
        elif opcao == "8":
            id_p = input("ID do participante a remover: ").strip()
            remover_participante(id_p)
        elif opcao == "9":
            id_e = input("ID do evento a remover: ").strip()
            remover_evento(id_e)
        elif opcao == "11":
            id_p = input("ID do participante: ")
            novo_email = input("Novo email: ")
            atualizar_email_participante(id_p, novo_email)

        elif opcao == "12":
            id_e = input("ID do evento: ")
            novo_tema = input("Novo tema: ")
            atualizar_tema_evento(id_e, novo_tema)
        elif opcao == "10":
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
