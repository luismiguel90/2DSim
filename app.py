from flask import Flask, render_template, jsonify, request
import random




app = Flask(__name__)

# Base
@app.route("/")
def index():
    return "Hello World. by Luís"



# Simulacao de base de dados num dicionario
# "activity_instances" -> ID da atividade
# value: {"activity_type": "2DSim", "students": {inveniraStdID: analytics}}
DB = { "activity_instances": {} }       

# Pagina de configuracao para o professor (config_url)
@app.route("/config")
def config():
    return render_template('config.html')



# Lista de parametros de configuracao (json_params_url)
@app.route("/api/params", methods=['GET'])
def params():
    return jsonify([
        {"name": "map_selection", "type": "enum","values": ["mapa_1", "mapa_2", "mapa_3"]},
        {"name": "dificuldade","type": "enum","values": ["fácil", "médio", "difícil"]},
        {"name": "max_steps","type": "integer","default": 50, "min": 10, "max": 200}
    ])



# Deploy de instancia da atividade pelo professor (user_url)
@app.route("/api/deploy", methods=['GET'])
def deploy():
    # Recebe tipo da atividade e o ID da instancia
    activity_type = request.args.get("activity_type", "2DSim")
    instance_id = request.args.get("instanceID", "instancia_1")

    # Criar instancia
    if instance_id not in DB["activity_instances"]:
        DB["activity_instances"][instance_id] = { 
            "activity_type": activity_type, 
            "students": {}                              # Registo de alunos ao acederem
        }

    # URL de acesso a instancia para alunos
    activity_url = f"{request.scheme}://{request.host}/activity?instanceID={instance_id}"
    return jsonify({
        "success": True,
        "activityURL": activity_url,
        "instanceID": instance_id,
        "activity_type": activity_type
    }) 


# Lista de analytics disponiveis (analytics_list_url)
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


# Analytics de todos os alunos da instancia (analytics_url)
@app.route("/api/analytics", methods=['POST'])
def analytics():
    data = request.get_json()
    instance_id = data.get("activityID")

    if instance_id not in DB["activity_instances"]:
        return jsonify([])                              # Instancia nao existe
    
    instance = DB["activity_instances"][instance_id]
    students = instance["students"]

    # Simulacao de dados de alunos, mockup data
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



if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

