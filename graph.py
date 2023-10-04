import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Resultados dos 4 cenários
results_cenario1 = pd.read_csv("sample_data/results_1.csv")
results_cenario2 = pd.read_csv("sample_data/results_2.csv")
results_cenario3 = pd.read_csv("sample_data/results_3.csv")
results_cenario4 = pd.read_csv("sample_data/results_4.csv")
resultados = [results_cenario1, results_cenario2, results_cenario3, results_cenario4]

# Erros de Little a cada 10 segundos dos 4 cenários
erros_cenario1 = pd.read_csv("res/erros_1.csv")
erros_cenario2 = pd.read_csv("res/erros_2.csv")
erros_cenario3 = pd.read_csv("res/erros_3.csv")
erros_cenario4 = pd.read_csv("res/erros_4.csv")
erros_cenarios = [erros_cenario1, erros_cenario2, erros_cenario3, erros_cenario4]

# Gráfico 1: Ocupação x Ocupação Simulada
def plot_grafico1(results_cenarios):
    plt.figure(figsize=(8, 6))
    for index, cenario in enumerate(resultados):
        plt.plot(cenario['Ocupação Objetivo'], cenario['Ocupação Simulada'], marker='o', linestyle='-', label=f'Cenário {index+1}')
    plt.xlabel('Ocupação Objetivo')
    plt.ylabel('Ocupação Simulada')
    plt.title('Ocupação Objetivo x Ocupação Simulada')
    plt.legend(loc='upper left')
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.xticks(np.arange(0.6, 1.11, 0.05), fontsize=12)
    plt.yticks(np.arange(0.6, 1.11, 0.05), fontsize=12)
    plt.tight_layout()
    def add_labels(x, y):
        for i in range(len(x)):
            plt.annotate(f'({x[i]:.4f}, {y[i]:.4f})', (x[i], y[i]), textcoords="offset points", xytext=(0, 10), ha='left', fontsize=12)
    for cenario in results_cenarios:
        add_labels(cenario['Ocupação Objetivo'], cenario['Ocupação Simulada'])
    plt.show()

# Gráfico 2: Ocupação Objetivo x E[N]
def plot_grafico2(results_cenarios):
    plt.figure(figsize=(8, 6))
    for index, cenario in enumerate(results_cenarios):
        plt.plot(cenario['Ocupação Objetivo'], cenario['E[N]'], marker='o', linestyle='-', label=f'Cenário {index+1}')
    plt.xlabel('Ocupação Objetivo')
    plt.ylabel('E[N]')
    plt.title('Ocupação Objetivo x E[N]')
    plt.xticks(np.arange(0.6, 1.11, 0.05), fontsize=12)
    plt.yticks(np.arange(0, 130, 10), fontsize=12)
    plt.tight_layout()
    plt.legend(loc='upper left')
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    def add_labels(x, y):
        for i in range(len(x)):
            plt.annotate(f'({x[i]:.2f}, {y[i]:.4f})', (x[i], y[i]), textcoords="offset points", xytext=(0, 10), ha='left', fontsize=12)
    for cenario in results_cenarios:
        add_labels(cenario['Ocupação Objetivo'], cenario['E[N]'])
    plt.show()

# Gráfico 3: Ocupação Objetivo x E[W]
def plot_grafico3(results_cenarios):
    plt.figure(figsize=(8, 6))
    for index, cenario in enumerate(results_cenarios):
        plt.plot(cenario['Ocupação Objetivo'], cenario['E[W]'], marker='o', linestyle='-', label=f'Cenário {index+1}')
    plt.xlabel('Ocupação Objetivo')
    plt.ylabel('E[W]')
    plt.title('Ocupação Objetivo x E[W]')
    plt.legend(loc='upper left')
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.xticks(np.arange(0.6, 1.11, 0.05), fontsize=12)
    plt.yticks(np.arange(0, 65, 5), fontsize=12)
    plt.tight_layout()
    
    def add_labels(x, y):
        for i in range(len(x)):
            plt.annotate(f'({x[i]:.2f}, {y[i]:.4f})', (x[i], y[i]), textcoords="offset points", xytext=(0, 10), ha='left', fontsize=12)

    for cenario in results_cenarios:
        add_labels(cenario['Ocupação Objetivo'], cenario['E[W]'])
    plt.show()

# Gera os 3 gráficos iniciais
plot_grafico1(resultados)
plot_grafico2(resultados)
plot_grafico3(resultados)

# Gráficos dos Erros de Little de cada Cenário
# É feita a média dos erros de little a cada 12 horas de simulação
# O gráfico é criado com a Média dos Erros de Little x Tempo (h)
def plot_erros_little_interval(erros_cenario, cenario_numero):
    intervalo_segundos = 12 * 3600
    pontos_por_intervalo = int(intervalo_segundos / erros_cenario['Tempo'].iloc[1])
    x_intervalos_horas = np.arange(12, 241, 12)
    erros_media = []
    for i in range(0, len(x_intervalos_horas)):
        inicio_intervalo = i * pontos_por_intervalo
        fim_intervalo = (i + 1) * pontos_por_intervalo
        erros_intervalo = erros_cenario['Erro Little'][inicio_intervalo:fim_intervalo]
        erro_medio = np.mean(erros_intervalo)
        erros_media.append(erro_medio)
    plt.figure(figsize=(14, 6))
    plt.plot(x_intervalos_horas, erros_media, linestyle='-', linewidth=1)
    plt.axhline(y=0.0, color='red', linestyle='--', linewidth=1.5, label='Objetivo (Erro = 0.0)')
    plt.xlabel('Tempo (horas)', fontsize=14)
    plt.ylabel('Erro de Little (Média)', fontsize=14)
    plt.title(f'Erro de Little x Tempo - Cenário {cenario_numero}', fontsize=16)
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.xticks(np.arange(12, 241, 12), fontsize=7)
    plt.yticks(np.arange(-0.1, 0.1, 0.01), fontsize=7)
    plt.show()

# Gera os gráficos dos Erros de Little para cada cenário
plot_erros_little_interval(erros_cenario1, 1)
plot_erros_little_interval(erros_cenario2, 2)
plot_erros_little_interval(erros_cenario3, 3)
plot_erros_little_interval(erros_cenario4, 4)

# Cria dos Erros de Little de todos os cenários juntos
def plot_erros_little_multi(erros_cenarios):
    intervalo_segundos = 12 * 3600
    pontos_por_intervalo = int(intervalo_segundos / erros_cenarios[0]['Tempo'].iloc[1])
    x_intervalos_horas = np.arange(12, 241, 12)
    plt.figure(figsize=(14, 6))
    
    for i, erros_cenario in enumerate(erros_cenarios):
        erros_media = []
        for j in range(0, len(x_intervalos_horas)):
            inicio_intervalo = j * pontos_por_intervalo
            fim_intervalo = (j + 1) * pontos_por_intervalo
            erros_intervalo = erros_cenario['Erro Little'][inicio_intervalo:fim_intervalo]
            erro_medio = np.mean(erros_intervalo)
            erros_media.append(erro_medio)
        
        label = f'Cenário {i+1}'
        plt.plot(x_intervalos_horas, erros_media, linestyle='-', linewidth=1, label=label)

    plt.xlabel('Tempo (horas)', fontsize=14)
    plt.ylabel('Erro de Little (Média)', fontsize=14)
    plt.title('Erro de Little x Tempo - Todos os Cenários', fontsize=16)
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.xticks(np.arange(12, 241, 12), fontsize=7)
    plt.yticks(np.arange(-0.1, 0.1, 0.01), fontsize=7)
    plt.legend(loc='lower right', fontsize=8)
    plt.show()

# Gera o gráfico (Erros de Little) de todos os cenários juntos 
plot_erros_little_multi(erros_cenarios)