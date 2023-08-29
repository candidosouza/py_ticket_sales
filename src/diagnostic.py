# exemplo_diagnostico.py
import requests

# Atenção: O parâmetro verify=False torna sua conexão insegura. Use apenas para diagnóstico.
response = requests.get("https://localhost:9200", verify=False)

# Verifique a resposta
if response.status_code == 200:
    print("Conexão bem-sucedida!")
else:
    print(f"Conexão falhou! Código de status: {response.status_code}")