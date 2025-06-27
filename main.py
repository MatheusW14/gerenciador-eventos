from participantes import (
    cadastrar_participante,
    listar_participantes,
    remover_participante,
    atualizar_email_participante,
    exibir_participante_por_id,
)

from eventos import (
    cadastrar_evento,
    listar_eventos,
    remover_evento,
    atualizar_tema_evento,
    limpar_duplicatas_em_eventos,
    gerenciar_inscricao_evento,
    exibir_eventos_por_tema,
    exibir_eventos_por_data,
)

from relatorios import (
    exibir_participantes_mais_ativos,
    exibir_temas_mais_frequentes,
    exibir_eventos_risco_cancelamento,
    exibir_eventos_por_tema_agrupado,
    exibir_eventos_de_um_participante,
    exibir_taxa_media_participacao_por_tema,
)

from utils import limpar_terminal


def mostrar_menu_principal():
    print("\n" + "=" * 50)
    print("SISTEMA DE GERENCIAMENTO DE EVENTOS".center(50))
    print("=" * 50)
    print("--- GERENCIAR PARTICIPANTES ---")
    print("1. Cadastrar participante")
    print("2. Listar participantes")
    print("3. Buscar participante por ID")
    print("4. Atualizar email do participante")
    print("5. Remover participante")
    print("9. Buscar eventos por tema")
    print("10. Buscar eventos por faixa de datas")
    print("11. Atualizar tema do evento")
    print("12. Remover evento")
    print("\n--- OUTRAS OPÇÕES ---")
    print("13. Relatórios")
    print("14. Manutenção: Remover duplicatas")
    print("15. Sair")
    print("=" * 50)


def menu_relatorios():
    while True:
        print("\n" + "=" * 30)
        print("MENU DE RELATÓRIOS".center(30))
        print("=" * 30)
        print("a. Participantes mais ativos")
        print("b. Temas mais frequentes")
        print("c. Eventos em risco de cancelamento")
        print("d. Eventos agrupados por tema")
        print("e. Eventos de um participante")
        print("f. Taxa média de participação por tema")
        print("g. Voltar ao menu principal")
        print("=" * 30)

        opcao = input("Escolha uma opção de relatório: ").strip().lower()

        if opcao == "a":
            exibir_participantes_mais_ativos()
        elif opcao == "b":
            exibir_temas_mais_frequentes()
        elif opcao == "c":
            exibir_eventos_risco_cancelamento()
        elif opcao == "d":
            exibir_eventos_por_tema_agrupado()
        elif opcao == "e":
            exibir_eventos_de_um_participante()
        elif opcao == "f":
            exibir_taxa_media_participacao_por_tema()
        elif opcao == "g":
            break
        else:
            print("Opção inválida.")


def main():
    while True:
        mostrar_menu_principal()
        opcao = input("Escolha uma opção: ").strip()

        limpar_terminal()

        if opcao == "1":
            cadastrar_participante()
        elif opcao == "2":
            listar_participantes()
        elif opcao == "3":
            exibir_participante_por_id()
        elif opcao == "4":
            id_p = input("ID do participante para atualizar: ")
            novo_email = input("Digite o novo email: ")
            atualizar_email_participante(id_p, novo_email)
        elif opcao == "5":
            id_p_remover = input("Digite o ID do participante a remover: ")
            remover_participante(id_p_remover)
        elif opcao == "6":
            cadastrar_evento()
        elif opcao == "7":
            listar_eventos()
        elif opcao == "8":
            gerenciar_inscricao_evento()
        elif opcao == "9":
            exibir_eventos_por_tema()
        elif opcao == "10":
            exibir_eventos_por_data()
        elif opcao == "11":
            id_evento = input("Digite o ID do evento para atualizar o tema: ")
            novo_tema = input("Digite o novo tema: ")
            atualizar_tema_evento(id_evento, novo_tema)
        elif opcao == "12":
            id_evento_remover = input("Digite o ID do evento a remover: ")
            remover_evento(id_evento_remover)
        elif opcao == "14":
            limpar_duplicatas_em_eventos()
        elif opcao == "15":
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
