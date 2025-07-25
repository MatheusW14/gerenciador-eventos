# Sistema de Gerenciamento de Eventos - Comunidade Tech

Este projeto é um sistema de linha de comando para gerenciar eventos técnicos, workshops e atividades educacionais promovidos pela **Comunidade Tech**. Foi desenvolvido em Python como parte de um trabalho final da disciplina de Algoritmos e Lógica de Programação.

---

## Funcionalidades

✅ Cadastro de **participantes**  
✅ Cadastro de **eventos**  
✅ Inscrição de participantes em eventos  
✅ Listagem de eventos e participantes  
✅ **Busca** de participantes por ID  
✅ **Remoção** de eventos e participantes  
✅ **Atualização** de email e tema  
✅ Relatórios completos:
- Participantes mais ativos  
- Temas mais frequentes  
- Eventos com risco de cancelamento  
- Eventos por tema  
- Eventos de um participante específico  
- **Taxa média de participação por tema**

✅ **Busca filtrada** por tema e por faixa de datas  
✅ Detecção e remoção de **duplicatas** de participantes nos eventos  
✅ Armazenamento persistente com arquivos `.pkl`

---

## Estrutura do Projeto

```bash
.
├── main.py                # Menu e fluxo principal
├── eventos.py            # Funções relacionadas a eventos
├── participantes.py      # Funções de participantes
├── relatorios.py         # Relatórios estatísticos
├── persistencia.py       # Leitura e escrita com pickle
├── utils.py              # Funções utilitárias (ex: entrada, remover duplicatas)
├── eventos.pkl           # Arquivo gerado com os eventos cadastrados
├── participantes.pkl     # Arquivo gerado com os participantes cadastrados
└── README.md             # Este arquivo
```

---

## Como Rodar

1. **Tenha o Python 3 instalado**
2. Clone o projeto ou baixe os arquivos
3. No terminal, execute:
```bash
python main.py
```

---

## Tecnologias e conceitos usados

- Python 3
- Modularização
- List comprehensions
- `*args` e `**kwargs` em funções
- Arquivos binários com `pickle`
- Estruturas de dados: listas, dicionários
- Boas práticas de programação

---

## Exemplo de uso (menu principal)

```
SISTEMA DE GERENCIAMENTO DE EVENTOS
1. Cadastrar participante
2. Cadastrar evento
3. Inscrever participante em evento
4. Listar eventos
5. Listar participantes
6. Buscar participante por ID
7. Relatórios
8. Sair
```

---

## Autor

Desenvolvido como parte de um projeto acadêmico.

---