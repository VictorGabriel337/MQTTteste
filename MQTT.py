from flask import Flask , render_template
from flask_cors import CORS
import paho.mqtt.publish as publish
import ssl

app = Flask(__name__)
CORS(app)  # permite acesso de outras origens (como o Netlify ou Live Server)

# Informações do HiveMQ Cloud
MQTT_HOST = "1ad75df9162145458cd4c72cf02374f8.s1.eu.hivemq.cloud"
MQTT_PORT = 8883  # Porta segura para TLS
MQTT_TOPIC = "Led_state"
MQTT_USERNAME = "victorgabriel337"  # coloque aqui o usuário da HiveMQ Cloud
MQTT_PASSWORD = "Victorgabriel337"    # coloque aqui a senha da HiveMQ Cloud


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ligar", methods=["POST"])
def ligar():
    try:
        publish.single(
            topic=MQTT_TOPIC,
            payload="1",
            hostname=MQTT_HOST,
            port=MQTT_PORT,
            auth={'username': MQTT_USERNAME, 'password': MQTT_PASSWORD},
            tls=ssl.create_default_context()
        )
        return "LED Ligado"
    except Exception as e:
        return f"Erro ao ligar: {e}", 500

@app.route("/desligar", methods=["POST"])
def desligar():
    try:
        publish.single(
            topic=MQTT_TOPIC,
            payload="0",
            hostname=MQTT_HOST,
            port=MQTT_PORT,
            auth={'username': MQTT_USERNAME, 'password': MQTT_PASSWORD},
            tls=ssl.create_default_context()
        )
        return "LED Desligado"
    except Exception as e:
        return f"Erro ao desligar: {e}", 500

if __name__ == "__main__":
    app.run(debug=True)
