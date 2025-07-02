from participantes import (
    cadastrar_participante,
    listar_participantes,
    remover_participante,
    gerenciar_atualizacao_email,
    exibir_participante_por_id,
)

from eventos import (
    cadastrar_evento,
    listar_eventos,
    gerenciar_remocao_evento,
    gerenciar_atualizacao_tema,
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
    """
    Exibe o menu principal do Sistema de Gerenciamento de Eventos.

    O menu apresenta as seguintes opções:
    - Gerenciar participantes:
        1. Cadastrar participante
        2. Listar participantes
        3. Buscar participante por ID
        4. Atualizar email do participante
        5. Remover participante
    - Gerenciar eventos:
        9. Buscar eventos por tema
        10. Buscar eventos por faixa de datas
        11. Atualizar tema do evento
        12. Remover evento
    - Outras opções:
        13. Relatórios
        14. Manutenção: Remover duplicatas
        15. Sair

    O menu é exibido com formatação visual para facilitar a navegação.
    """
    # SUGESTÃO para main.py -> mostrar_menu_principal()


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
    print("\n--- GERENCIAR EVENTOS ---")
    print("6. Cadastrar evento")
    print("7. Listar eventos")
    print("8. Inscrever participante em evento")
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
    """
    Displays a menu for generating various reports related to events and participants.
    Allows the user to select an option to view specific reports or return to the main menu.
    Menu Options:
        a. Participantes mais ativos - Displays the most active participants.
        b. Temas mais frequentes - Displays the most frequent themes.
        c. Eventos em risco de cancelamento - Displays events at risk of cancellation.
        d. Eventos agrupados por tema - Displays events grouped by theme.
        e. Eventos de um participante - Displays events associated with a specific participant.
        f. Taxa média de participação por tema - Displays the average participation rate per theme.
        g. Voltar ao menu principal - Returns to the main menu.
    The function will continue to prompt the user until a valid option is selected or the user chooses to exit.
    """
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
    """
    Função principal do sistema de gerenciamento de eventos.

    Esta função exibe o menu principal e permite que o usuário escolha entre
    várias opções para gerenciar participantes, eventos e relatórios. O sistema
    continuará em execução até que o usuário escolha a opção de sair.

    Opções disponíveis:
        1. Cadastrar participante
        2. Listar participantes
        3. Buscar participante por ID
        4. Atualizar email do participante
        5. Remover participante
        6. Cadastrar evento
        7. Listar eventos
        8. Gerenciar inscrição em evento
        9. Buscar eventos por tema
        10. Buscar eventos por faixa de datas
        11. Atualizar tema do evento
        12. Remover evento
        13. Relatórios
        14. Manutenção: Remover duplicatas
        15. Sair
    """
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
            gerenciar_atualizacao_email()
        elif opcao == "5":
            remover_participante()
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
            gerenciar_atualizacao_tema()
        elif opcao == "12":
            gerenciar_remocao_evento()
        elif opcao == "13":
            menu_relatorios()
        elif opcao == "14":
            limpar_duplicatas_em_eventos()
        elif opcao == "15":
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
