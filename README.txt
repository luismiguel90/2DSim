# 2DSim Activity Provider

Este projeto implementa o **Activity Provider 2DSim** para a plataforma Inven!RA, permitindo aos alunos controlar um robô numa grelha 2D.
Objetivo do projeto

    Criar uma atividade educativa baseada num simulador 2D

    Permitir a execução de ações através do padrão Command

    Separar claramente:

        Criação de objetos

        Lógica de domínio

        Camada de controlo (API)

## Estrutura do projeto

        2dsim/
        │
        ├── app.py
        │
        ├── factories/
        │   ├── activity_factory.py
        │   └── simulador2d_factory.py
        │
        ├── models/
        │   ├── simulador_base.py
        │   └── simulador2d.py
        │
        ├── commands/
        │   ├── command_base.py
        │   ├── move_commands.py
        │   └── object_commands.py
        │
        └── templates/
            └── config.html


================================================================================================
= = = = = = = = = = = = = = = = = Camada de controlo (API) = = = = = = = = = = = = = = = = = = =
================================================================================================
O ficheiro app.py expõe os endpoints REST necessários ao funcionamento da atividade:

/api/deploy
Criação de uma instância da atividade (professor)

/api/provide_activity
Inicialização da atividade por um aluno

/api/execute_commands
Execução de comandos sobre o simulador (padrão Command)

/api/params, /api/analytics_list, /api/analytics
Configuração e analytics da atividade
================================================================================================
= = = = = = = = = = = = = = = = = Padrões de design utilizados = = = = = = = = = = = = = = = = = 
================================================================================================
          Factory Method (Criação)

O padrão Factory Method é utilizado para decidir dinamicamente qual o simulador concreto a criar, com base na configuração definida pelo professor.

Fluxo:
ActivityFactory recebe o pedido de criação
Simulador2DFactory decide qual mapa instanciar
É devolvida uma instância de Simulador2DMapa1, Simulador2DMapa2 ou Simulador2DMapa3
Este padrão evita dependências diretas entre o app.py e classes concretas de simulador.

          Command (Comportamento)

O padrão Command é utilizado para encapsular as ações do robô como objetos independentes.
Estrutura:
Command (interface)
Comandos concretos:
MoveUp, MoveDown, MoveLeft, MoveRight
PickObject, DropObject
Funcionamento:
O simulador mantém uma lista de comandos
Cada comando executa a sua ação através do método execute(simulador)
O simulador não conhece a lógica interna dos comandos
Este padrão permite:
Extensão fácil de novas ações
Separação clara entre invocador e executor
Eliminação de condicionais complexos

================================================================================================
= = = = = = = = = = = = = = = = = Parâmetros configuráveis = = = = = = = = = = = = = = = = = = =
================================================================================================

Seleção do mapa: mapa_1, mapa_2, mapa_3
Dificuldade: fácil, médio, difícil
Número máximo de passos permitidos

================================================================================================
= = = = = = = = = = = = = = = = = Analytics  disponíveis = = = = = = = = = = = = = = = = = = = =
================================================================================================

- Quantitativos:
Tempo de simulação
Distância percorrida
Eficiência do caminho
Número de colisões
Número de comandos utilizados

- Qualitativos:

Objetivo atingido
Tipo de abordagem
Erros comuns
Resposta ao feedback

================================================================================================
= = = = = = = = = = = = = = = = = = = = Como  executar = = = = = = = = = = = = = = = = = = = = =
================================================================================================

pip install flask
python app.py

================================================================================================
= = = = = = = = = = = = = = = = = = = = Nota final = = = = = = = = = = = = = = = = = = = = = = =
================================================================================================

Este projeto foi desenvolvido com foco pedagógico privilegiando:

Clareza arquitetural, uso consciente de padrões de design, capacidade de análise crítica através da identificação de antipadrões