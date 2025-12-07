# 2DSim Activity Provider

Este projeto implementa o **Activity Provider 2DSim** para a plataforma Inven!RA, permitindo aos alunos controlar um robô numa grelha 2D.

## Estrutura do projeto

- `/app.py` → Endpoints da API:
  - `/api/deploy` → Fase 1: Criação da instância pelo professor.
  - `/api/provide_activity` → Fase 2: Aluno inicia/prossegue atividade.
  - `/api/params`, `/api/analytics_list`, `/api/analytics` → Parâmetros e analytics.
  
- `/models/` → Classes dos simuladores:
  - `simulador_base.py` → Classe abstrata `SimuladorBase`.
  - `simulador2d.py` → Subclasses concretas `Simulador2DMapa1/2/3`.

- `/factories/` → Fábricas que aplicam padrão de criação **Factory Method**:
  - `simulador2d_factory.py` → Cria simulador 2D correto com base nos parâmetros do professor.
  - `activity_factory.py` → Encapsula o uso da `Simulador2DFactory`.

## Padrão de criação utilizado

O **Factory Method** permite separar a lógica de criação da lógica de uso:

1. **ActivityFactory** decide que simulador concreto criar.
2. **Simulador2DFactory** devolve a instância correta (`Mapa1`, `Mapa2`, `Mapa3`) com base nos parâmetros.
3. **Simulador2DMapaX** implementa o método `iniciar()`.

Este padrão permite escalar facilmente para diferentes mapas consoante a dificuldades e presets sem modificar o `app.py`.

## Parâmetros configuráveis

- Escolha do mapa: `mapa_1`, `mapa_2`, `mapa_3`.
- Dificuldade: `fácil`, `médio`, `difícil`.
- Número máximo de passos permitidos.

## Analytics disponíveis

- **Quantitativos:** tempo, distância, eficiência, objetivos secundários, colisões, comandos, tentativas até sucesso.
- **Qualitativos:** objetivo atingido, tipo de aproximação, erros comuns, reação ao feedback.

## Como executar

```bash
pip install flask
python app.py
