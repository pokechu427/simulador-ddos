from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def home():
    # Simula um pequeno atraso para representar o processamento do servidor
    time.sleep(0.1)
    return "Servidor ativo"

if __name__ == '__main__':
    app.run(port=5000)  # O servidor irá rodar na porta 5000