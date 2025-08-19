import csv 
from dados import dados
import sys
import pandas as pd
import numpy as np

with open(f"{sys.path[0]}/ControleCarros.csv", "w") as csvfile: 
    writer = csv.DictWriter(csvfile, fieldnames=["Descricao", "placa", "Quantidade","Mes da Aquisicao","Valor","Colaborador","Observacoes","Quilometragem Inicial", "Quilometragem Final","Periodo de Uso", "Data de Retirada", "Data de Devolucao"])
    writer.writeheader()

    for dado in dados:
        writer.writerow(dado)

df = pd.read_csv(f"{sys.path[0]}/ControleCarros.csv")

#MOSTRANDO A TABELA
print(f"\nPrintando as primeiras 5 linhas: \n{df.head()}")
print(f"\n\nPrintando a tabela inteira: \n{df}")

#MOSTRANDO OPERAÇÕES COM NUMPY
carro_mais_caro = np.max(df['Valor'])
carro_mais_barato = np.min(df['Valor'])

print(f"\nValor do carro mais caro: {carro_mais_caro}")
print(f"\nValor do carro mais barato: {carro_mais_barato}")

#MOSTRANDO OS DADOS COMPLETOS COM O VALOR MAIS CARO E BARATO
indice_carro_mais_caro = df['Valor'].idxmax()
indice_carro_mais_barato = df['Valor'].idxmin()

carro_caro = df.iloc[indice_carro_mais_caro]
carro_barato = df.iloc[indice_carro_mais_barato]

print("\n\nCarro mais caro: \n", carro_caro)
print("\nCarro mais barato: \n", carro_barato)

#MOSTRANDO MAIS ESTATISTICAS
valor_avg = np.average(df["Valor"])
valor_median = np.median(df["Valor"])
print(f"\nValor da Média dos carros: {valor_avg}")
print(f"\nValor da Mediana dos carros: {valor_median}")