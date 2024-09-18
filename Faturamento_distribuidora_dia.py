#Faturamento_distribuidora_dia.py
#O codigo simula a leitura do arquivo json no meu computador

import json

# Caminho do arquivo JSON
caminho_arquivo = r'C:\Users\Windows 11\Downloads\dados.json'

# Ler os dados do arquivo JSON
with open(caminho_arquivo, 'r') as arquivo:
    dados = json.load(arquivo)

# Filtrar os dias com faturamento
faturamentos = [d["valor"] for d in dados if d["valor"] > 0]

# a) Menor valor de faturamento
menor_faturamento = min(faturamentos)

# b) Maior valor de faturamento
maior_faturamento = max(faturamentos)

# c) Média mensal de faturamento
media_mensal = sum(faturamentos) / len(faturamentos)

# Número de dias com faturamento acima da média mensal
dias_acima_da_media = len([d for d in faturamentos if d > media_mensal])

print(f"Menor valor de faturamento: {menor_faturamento}")
print(f"Maior valor de faturamento: {maior_faturamento}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")
