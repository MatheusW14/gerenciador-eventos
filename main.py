import participantes
import eventos
import relatorios


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
    print("8. Sair")
    print("=" * 50)


def mostrar_relatorios():
    print("\n" + "-" * 50)
    print("MENU DE RELATÓRIOS")
    print("-" * 50)
    print("1. Participantes mais ativos")
    print("2. Temas mais frequentes")
    print("3. Eventos em risco de cancelamento")
    print("4. Eventos por tema")
    print("5. Voltar")
    print("-" * 50)


def main():
    while True:
        mostrar_menu()
        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            participantes.cadastrar_participante()

        elif opcao == "2":
            eventos.cadastrar_evento()

        elif opcao == "3":
            eventos.listar_eventos()
            id_evento = input("\nDigite o ID do evento: ").strip()
            participantes.listar_participantes()
            id_participante = input("Digite o ID do participante: ").strip()
            if eventos.inscrever_participante(id_evento, id_participante):
                print("\n✅ Inscrição realizada com sucesso!")
            else:
                print("\n❌ Falha na inscrição!")

        elif opcao == "4":
            eventos.listar_eventos()

        elif opcao == "5":
            participantes.listar_participantes()

        elif opcao == "6":
            id_participante = input("\nDigite o ID do participante: ").strip()
            participante = participantes.buscar_participante(id_participante)
            if participante:
                print("\n=== Dados do Participante ===")
                print(f"Nome: {participante['nome']}")
                print(f"E-mail: {participante['email']}")
                print(f"Preferências: {', '.join(participante['preferencias'])}")
            else:
                print("\nParticipante não encontrado!")

        elif opcao == "7":
            while True:
                mostrar_relatorios()
                sub_opcao = input("\nEscolha um relatório: ").strip()

                if sub_opcao == "1":
                    print("\n=== Participantes Mais Ativos ===")
                    for id_participante, qtd in relatorios.participantes_mais_ativos():
                        participante = participantes.buscar_participante(
                            id_participante
                        )
                        nome = participante["nome"] if participante else "Desconhecido"
                        print(f"{nome} (ID: {id_participante}) - {qtd} eventos")

                elif sub_opcao == "2":
                    print("\n=== Temas Mais Frequentes ===")
                    for tema, qtd in relatorios.temas_mais_frequentes():
                        print(f"{tema}: {qtd} eventos")

                elif sub_opcao == "3":
                    print("\n=== Eventos em Risco de Cancelamento ===")
                    for evento in relatorios.eventos_risco_cancelamento():
                        print(
                            f"{evento['nome']} (ID: {evento['id']}) - {len(evento['participantes'])} participantes"
                        )

                elif sub_opcao == "4":
                    print("\n=== Eventos por Tema ===")
                    for tema, lista_eventos in relatorios.eventos_por_tema().items():
                        print(f"\nTema: {tema}")
                        for evento in lista_eventos:
                            print(f"- {evento}")

                elif sub_opcao == "5":
                    break

                else:
                    print("\nOpção inválida!")

        elif opcao == "8":
            print("\nSaindo do sistema...")
            break

        else:
            print("\nOpção inválida!")


if __name__ == "__main__":
    main()
