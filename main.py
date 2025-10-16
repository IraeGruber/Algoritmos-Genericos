import numpy as np
import random

# ==========================================
# Parâmetros do Algoritmo Genético
# ==========================================
NUM_INDIVIDUOS = 30
NUM_FEATURES = 45
MAX_GERACOES = 50
TAXA_CROSSOVER = 0.8
TAXA_MUTACAO = 0.05
TAMANHO_TORNEIO = 3
NUM_ELITE = 2

# ==========================================
# Função de Fitness
# ==========================================
def calcular_fitness(individuo, dataset, labels):
    indices_ativos = [i for i, bit in enumerate(individuo) if bit == 1]
    
    if len(indices_ativos) == 0:
        return float('inf')

    acuracia_simulada = 0.90 + random.uniform(-0.05, 0.05) - (len(indices_ativos) * 0.001)
    acuracia_real = acuracia_simulada

    proporcao_usada = len(indices_ativos) / NUM_FEATURES
    penalidade = proporcao_usada * 0.2 

    fitness = (1 - acuracia_real) + penalidade
    return fitness

# ==========================================
# Outras Funções (Seleção, Crossover, Mutação)
# ==========================================
def inicializar_populacao():
    return np.random.randint(0, 2, (NUM_INDIVIDUOS, NUM_FEATURES))

def selecionar_pais(populacao, fitness):
    participantes_idx = random.sample(range(len(populacao)), TAMANHO_TORNEIO)
    participantes_fitness = fitness[participantes_idx]
    vencedor_local_idx = np.argmin(participantes_fitness)
    return populacao[participantes_idx[vencedor_local_idx]]

def crossover(pai1, pai2):
    if random.random() > TAXA_CROSSOVER:
        return np.copy(pai1)
    filho = np.array([pai1[i] if random.random() < 0.5 else pai2[i] for i in range(NUM_FEATURES)])
    return filho

def mutacao(individuo):
    for i in range(NUM_FEATURES):
        if random.random() < TAXA_MUTACAO:
            individuo[i] = 1 - individuo[i]
    return individuo

# ==========================================
# Algoritmo Genético
# ==========================================
def algoritmo_genetico(dataset, labels):
    populacao = inicializar_populacao()
    melhor_individuo_geral = None
    melhor_fitness_geral = float('inf')

    print("Iniciando otimização...")
    for geracao in range(MAX_GERACOES):
        fitness = np.array([calcular_fitness(ind, dataset, labels) for ind in populacao])
        
        indices_ordenados = np.argsort(fitness)
        
        if fitness[indices_ordenados[0]] < melhor_fitness_geral:
            melhor_fitness_geral = fitness[indices_ordenados[0]]
            melhor_individuo_geral = np.copy(populacao[indices_ordenados[0]])
        
        nova_populacao = []
        for i in range(NUM_ELITE):
            nova_populacao.append(populacao[indices_ordenados[i]])

        while len(nova_populacao) < NUM_INDIVIDUOS:
            pai1 = selecionar_pais(populacao, fitness)
            pai2 = selecionar_pais(populacao, fitness)
            filho = crossover(pai1, pai2)
            filho = mutacao(filho)
            nova_populacao.append(filho)

        populacao = np.array(nova_populacao)

        if (geracao + 1) % 10 == 0:
            print(f"Geração {geracao + 1}/{MAX_GERACOES} | Melhor Fitness: {melhor_fitness_geral:.4f} | Features: {sum(melhor_individuo_geral)}")

    return melhor_individuo_geral, melhor_fitness_geral

# ==========================================
# Execução
# ==========================================
dataset_simulado = np.random.rand(100, NUM_FEATURES)
labels_simulados = np.random.randint(0, 2, 100)

melhor_solucao, melhor_fitness = algoritmo_genetico(dataset_simulado, labels_simulados)

print("\n--- Resultado Final ---")
print(f"Melhor subconjunto de features: {melhor_solucao}")
print(f"Número de features selecionadas: {sum(melhor_solucao)}")
print(f"Fitness final: {melhor_fitness:.4f}")