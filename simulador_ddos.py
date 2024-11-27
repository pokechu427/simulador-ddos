import requests
import threading

# Função para realizar uma requisição ao servidor
def make_request():
    try:
        response = requests.get("http://127.0.0.1:5000/") 
        print(response.text)
    except requests.exceptions.RequestException as e:
        print("Falha na conexão:", e)

# Função para simular um ataque DDoS com múltiplas requisições simultâneas
def simulate_ddos(threads):
    thread_list = []
    for _ in range(threads):
        thread = threading.Thread(target=make_request)
        thread_list.append(thread)
        thread.start()

    # Aguarda que todas as threads terminem
    for thread in thread_list:
        thread.join()

# Solicita o número de requisições simuladas ao usuário
num_requests = int(input("Digite o número de requisições para simular o ataque DDoS: "))
simulate_ddos(num_requests)