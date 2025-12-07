from flask import Flask, render_template, jsonify, request
import random
from factories.activity_factory import ActivityFactory



app = Flask(__name__)

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# Página Inicial
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
@app.route("/")
def index():
    return "Hello World. by Luís"



# Simulacao de base de dados num dicionario
# "activity_instances" -> ID da atividade
# value: {"activity_type": "2DSim", "students": {inveniraStdID: analytics}}
DB = { "activity_instances": {} }       

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# Pagina de configuracao para o professor (config_url)
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
@app.route("/config")
def config():
    return render_template('config.html')


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# Lista de parametros de configuracao (json_params_url)
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
@app.route("/api/params", methods=['GET'])
def params():
    return jsonify([
        {"name": "map_selection", "type": "enum","values": ["mapa_1", "mapa_2", "mapa_3"]},
        {"name": "dificuldade","type": "enum","values": ["fácil", "médio", "difícil"]},
        {"name": "max_steps","type": "integer","default": 50, "min": 10, "max": 200}
    ])


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# Fase 1 do deploy: professor cria instancia a atividade (user_url)
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
@app.route("/api/deploy", methods=['GET'])
def deploy():
    activity_type = request.args.get("activity_type", "2DSim")
    instance_id = request.args.get("instanceID", "instancia_1")

    # Criar instância na base de dados caso não exista
    if instance_id not in DB["activity_instances"]:
        DB["activity_instances"][instance_id] = { 
            "activity_type": activity_type, 
            "students": {}                                                  # Registo de alunos ao acederem
        }

    # URL de acesso a instância para alunos
    activity_url = f"{request.scheme}://{request.host}/activity?instanceID={instance_id}"
    return jsonify({
        "success": True,
        "activityURL": activity_url,
        "instanceID": instance_id,
        "activity_type": activity_type
    }) 

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# Lista de analytics disponíveis (analytics_list_url)
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
@app.route("/api/analytics_list", methods=['GET'])
def analytics_list():
    return jsonify({
        "quantAnalytics": [
                {"name": "tempo_simulacao"},
                {"name": "distancia_percorrida","type": "integer"},
                {"name": "eficiencia_caminho","type": "float"},
                {"name": "n_obj_secundarios","type": "integer"},
                {"name": "n_colisoes","type": "integer"},
                {"name": "n_comandos_usados","type": "integer"},
                {"name": "n_tentativas_sucesso","type": "integer"}
        ],
        "qualAnalytics": [
                {"name": "obj_atingido","type": "boolean"},
                {"name": "tipo_aproximacao","type": "text/plain"},
                {"name": "erros_comuns","type": "text/plain"},
                {"name": "resposta_feedback","type": "text/plain"}
        ]
    })

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# Analytics de todos os alunos da instância (analytics_url)
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
@app.route("/api/analytics", methods=['POST'])
def analytics():
    data = request.get_json()
    instance_id = data.get("activityID")

    if instance_id not in DB["activity_instances"]:
        return jsonify([])                                                          # Instância nao existe
    
    instance = DB["activity_instances"][instance_id]
    students = instance["students"]

    # Simulacao de dados de alunos caso não existam, mockup data
    if not students:
        for std_id in [1001, 1002]:
            students[std_id] = {
                "quantAnalytics": [
                    {"name": "tempo_simulacao", "value": round(random.uniform(10, 300), 1)},
                    {"name": "distancia_percorrida", "value": random.randint(0, 30)},
                    {"name": "eficiencia_caminho", "value": round(random.uniform(0, 1), 2)},
                    {"name": "n_obj_secundarios", "value": random.randint(0, 5)},
                    {"name": "n_colisoes", "value": random.randint(0, 10)},
                    {"name": "n_comandos_usados", "value": random.randint(10, 50)},
                    {"name": "n_tentativas_sucesso", "value": random.randint(1, 10)}
                ],
                "qualAnalytics": [
                    {"obj_atingido": random.choice([True, False])},
                    {"tipo_aproximacao": random.choice(["abordagem sistemática", "tentativa e erro"])},
                    {"erros_comuns": random.choice(["erro A", "erro B", "erro C"])},
                    {"resposta_feedback": random.choice(["bom", "precisa melhorar", "ótimo"])}
                ]
        }

    response = []
    for std_id, data in students.items():
        response.append({
            "inveniraStdID": std_id,
            "quantAnalytics": data["quantAnalytics"],
            "qualAnalytics": data["qualAnalytics"]
        })

    return jsonify(response)

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# Fase 2 do deploy: Provide Activity
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
@app.route("/api/provide_activity", methods=['POST'])
def provide_activity():
    
    """
    Quando o aluno inicia ou prossegue a atividade.
    Recebe JSON com (exemplo):
    {
        "activityID": "ID da instância",
        "Inven!RAstdID": "ID do aluno",
        "json_params": { "map_selection": "mapa_1", "dificuldade": "fácil", "max_steps": 50 }
    }

    Aqui aplica-se o padrão Factory Method:
    -> ActivityFactory decide qual simulador concreto criar (Mapa 1, 2 ou 3)
    -> Se o aluno já existir, apenas retorna a URL da atividade
    """

    data = request.get_json()

    if not data or 'activityID' not in data or 'Inven!RAstdID' not in data:
        return jsonify({'error': 'Campos obrigatórios ausentes.'}), 400

    activity_id = data['activityID']
    student_id = data['Inven!RAstdID']
    json_params = data.get('json_params', {})

    # Validar instância
    if activity_id not in DB["activity_instances"]:
        return jsonify({'error': 'Instância não encontrada na base de dados.'}), 404

    instance = DB["activity_instances"][activity_id]

    # Cria simulador através do Factory Method apenas se o aluno ainda não existir
    if student_id not in instance["students"]:
        simulador = ActivityFactory.criar_2d_simulator(activity_id, student_id, json_params)
        instance["students"][student_id] = {
            "config": json_params,
            "object": simulador,
            "analytics": {}
        }
        '''
        # -> Exemplo de uso do método iniciar()
        simulador_inicial = simulador.iniciar()
        print(f"[INFO] {simulador_inicial}")
        '''
    activity_url = f"{request.scheme}://{request.host}/activity?instanceID={activity_id}&studentID={student_id}"
    return jsonify({
        "success": True,
        "activityURL": activity_url,
        "activityID": activity_id,
        "studentID": student_id,
        "config": json_params
    })


# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# Run App
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

