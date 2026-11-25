# Importando as bibliotecas
import pandas as pd
import matplotlib.pyplot as plt

# Lendo o arquivo CSV
dados = pd.read_csv("dados.csv")

# Mostrando os dados no terminal
print("Dados da escola Easycomp:")
print(dados)

# Verificando se existem valores vazios
print("\nValores vazios por coluna:")
print(dados.isnull().sum())

# Calculando os totais
total_interessados = dados["Interessados"].sum()
total_matriculados = dados["Matriculados"].sum()
total_sem_matricula = total_interessados - total_matriculados

# Calculando a porcentagem de conversão por curso
dados["Conversao (%)"] = dados["Matriculados"] / dados["Interessados"] * 100

# Mostrando os resultados no terminal
print("\nTotal de interessados:", total_interessados)
print("Total de matriculados:", total_matriculados)
print("Interessados que ainda não se matricularam:", total_sem_matricula)
print("\nTaxa de conversão por curso:")
print(dados[["Curso", "Conversao (%)"]])

# Criando o gráfico 1: interesse por curso
plt.bar(dados["Curso"], dados["Interessados"])
plt.title("Interesse por curso")
plt.xlabel("Curso")
plt.ylabel("Quantidade de interessados")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.show()

# Criando o gráfico 2: interessados x matriculados
posicoes = range(len(dados))
largura = 0.4
plt.bar([posicao - largura / 2 for posicao in posicoes], dados["Interessados"], width=largura, label="Interessados")
plt.bar([posicao + largura / 2 for posicao in posicoes], dados["Matriculados"], width=largura, label="Matriculados")
plt.title("Interessados x Matriculados")
plt.xlabel("Curso")
plt.ylabel("Quantidade de pessoas")
plt.xticks(posicoes, dados["Curso"], rotation=30, ha="right")
plt.legend()
plt.tight_layout()
plt.show()

# Criando o gráfico 3: taxa de conversão
plt.bar(dados["Curso"], dados["Conversao (%)"])
plt.title("Taxa de conversão por curso")
plt.xlabel("Curso")
plt.ylabel("Conversão (%)")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.show()
