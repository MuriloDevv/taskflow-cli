TaskFlow CLI

Gerenciador de tarefas que roda 100% no terminal, feito em Python com SQLite. Sem frameworks e sem dependências externas: só a biblioteca padrão da linguagem.

Projeto de estudo de backend, construído do zero, com foco em organização de código em camadas, validação de regras de negócio e persistência de dados.

Funcionalidades
Criar tarefas com título, descrição, prioridade e prazo opcional
Listar todas as tarefas em uma tabela formatada no terminal
Consultar uma tarefa pelo ID
Editar título e descrição
Marcar tarefas como concluídas
Excluir tarefas (com confirmação)
Filtrar por status (pendente, concluida) e prioridade (baixa, media, alta)
Dados salvos em SQLite: continuam lá depois de fechar o programa
Regras de negócio
O título não pode ser vazio (nem só espaços)
Cada tarefa tem um ID único, gerado pelo banco
Status e prioridade só aceitam valores válidos, validados no código e também no banco (CHECK)
Prazos precisam estar no formato AAAA-MM-DD e ser datas reais
Erros de entrada mostram uma mensagem clara e o programa não fecha
Consultas ao banco usam parâmetros (?), nunca texto concatenado, o que evita SQL injection
Conexões são sempre fechadas, mesmo quando acontece um erro
Tecnologias
Python 3
SQLite (módulo sqlite3 da biblioteca padrão)
Git e GitHub
Estrutura do projeto
taskflow-cli/
├── main.py       # ponto de entrada
├── cli.py        # menu, leitura de entradas e exibição da tabela
├── tasks.py      # regras de negócio e validações
├── database.py   # conexão e criação da tabela
└── README.md

Cada arquivo tem uma responsabilidade:

Arquivo	Responsabilidade
database.py	Sabe falar com o SQLite
tasks.py	Aplica as regras e executa as operações sobre as tarefas
cli.py	Conversa com o usuário no terminal
main.py	Inicializa o banco e inicia o programa
Como rodar

Pré-requisito: Python 3 instalado.

bash
# 1. Clone o repositório
git clone https://github.com/MuriloDevv/taskflow-cli.git
cd taskflow-cli

# 2. (Opcional) Crie e ative um ambiente virtual
python -m venv .venv
# Windows (PowerShell):
.venv\Scripts\Activate.ps1
# Linux/Mac:
source .venv/bin/activate

# 3. Execute
python main.py

Não há dependências para instalar. O arquivo taskflow.db é criado automaticamente na primeira execução.

Exemplo de uso
=== TaskFlow ===
1. Listar tarefas
2. Adicionar tarefa
3. Consultar tarefa por ID
4. Editar tarefa
5. Concluir tarefa
6. Excluir tarefa
7. Filtrar tarefas
0. Sair
Escolha: 1

ID   Título               Status     Prioridade Prazo
----------------------------------------------------------
1    Estudar SQL          pendente   alta       2026-11-01
2    Fazer o README       concluida  media      -
Próximos passos
 Testes automatizados (unittest ou pytest)
 Editar prioridade e prazo de uma tarefa existente
 Destacar tarefas com prazo vencido
 Ordenação por prazo e prioridade
 Comandos diretos via argumentos (python main.py add "titulo") com argparse
Aprendizados

Este projeto foi feito para praticar:

separação de responsabilidades em módulos
uso do sqlite3 com transações e tratamento de erros
validação de dados na camada de negócio e no banco
fluxo de trabalho com Git e GitHub
Autor

Feito por MuriloDevv.