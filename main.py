import numpy as np
import random
import copy


class GAParams:
    """Encapsula os parâmetros do Algoritmo Genético para melhor organização."""
    NUM_INDIVIDUOS = 30
    NUM_FEATURES = 45
    MAX_GERACOES = 100
    TAXA_CROSSOVER = 0.8
    TAXA_MUTACAO = 0.05
    TAMANHO_TORNEIO = 3
    TAXA_ELITISMO = 1  # Número de melhores indivíduos a serem mantidos


# Função de Fitness
def calcular_fitness(individuo, dataset, labels):
    """
    Calcula o fitness de um indivíduo.
    O fitness é menor para soluções melhores (menor erro, menor número de features).
    """
    num_features_ativas = np.sum(individuo)
    if num_features_ativas == 0:
        return float('inf')  # Penalidade máxima para indivíduos sem features

    # Simula a acurácia de um modelo treinado com as features selecionadas
    acuracia_simulada = 0.90 + random.uniform(-0.05, 0.05) - (num_features_ativas * 0.001)

    # Penalidade proporcional ao número de features usadas
    proporcao_usada = num_features_ativas / GAParams.NUM_FEATURES
    penalidade = proporcao_usada * 0.2  # Peso da penalidade

    # O objetivo é minimizar esta função (maximizar acurácia, minimizar features)
    fitness = 1 - acuracia_simulada + penalidade
    return fitness

# Inicialização da população
def inicializar_populacao():
    """Cria a população inicial de indivíduos."""
    populacao = np.random.randint(0, 2, (GAParams.NUM_INDIVIDUOS, GAParams.NUM_FEATURES))
    return populacao

# Seleção de pais (Torneio)
def selecionar_pais(populacao, fitness):
    """Seleciona um pai usando o método de seleção por torneio."""
    participantes_idx = random.sample(range(len(populacao)), GAParams.TAMANHO_TORNEIO)
    participantes_fitness = fitness[participantes_idx]
    vencedor_idx = participantes_idx[np.argmin(participantes_fitness)]
    return populacao[vencedor_idx]

# Crossover (Uniforme)
def crossover(pai1, pai2):
    """Realiza o crossover uniforme entre dois pais para gerar um filho."""
    if random.random() > GAParams.TAXA_CROSSOVER:
        return copy.deepcopy(pai1)  # Retorna uma cópia de um dos pais

    filho = np.array([pai1[i] if random.random() < 0.5 else pai2[i] for i in range(GAParams.NUM_FEATURES)])
    return filho

# Mutação
def mutacao(individuo):
    """Aplica mutação em um indivíduo, invertendo bits com base na taxa de mutação."""
    for i in range(GAParams.NUM_FEATURES):
        if random.random() < GAParams.TAXA_MUTACAO:
            individuo[i] = 1 - individuo[i]  # Inverte o bit
    return individuo

# Algoritmo Genético
def algoritmo_genetico(dataset, labels):
    """Executa o ciclo principal do Algoritmo Genético."""
    populacao = inicializar_populacao()
    melhor_geral = None
    melhor_fitness_geral = float('inf')

    for geracao in range(GAParams.MAX_GERACOES):
        fitness = np.array([calcular_fitness(ind, dataset, labels) for ind in populacao])

        # Elitismo: guarda os melhores indivíduos
        indices_ordenados = np.argsort(fitness)
        nova_populacao = []
        for i in range(GAParams.TAXA_ELITISMO):
            nova_populacao.append(populacao[indices_ordenados[i]])

        # Verifica se o melhor desta geração é o melhor de todos
        if fitness[indices_ordenados[0]] < melhor_fitness_geral:
            melhor_fitness_geral = fitness[indices_ordenados[0]]
            melhor_geral = copy.deepcopy(populacao[indices_ordenados[0]])

        # Gera o resto da população
        while len(nova_populacao) < GAParams.NUM_INDIVIDUOS:
            pai1 = selecionar_pais(populacao, fitness)
            pai2 = selecionar_pais(populacao, fitness)
            filho = crossover(pai1, pai2)
            filho = mutacao(filho)
            nova_populacao.append(filho)

        populacao = np.array(nova_populacao)
        print(f"Geração {geracao + 1}/{GAParams.MAX_GERACOES} | Melhor Fitness: {melhor_fitness_geral:.4f}")

    return melhor_geral, melhor_fitness_geral

# Execução simulada
dataset_simulado = np.random.rand(100, GAParams.NUM_FEATURES)
labels_simulados = np.random.randint(0, 2, 100)

melhor_solucao, melhor_fitness = algoritmo_genetico(dataset_simulado, labels_simulados)

print("\n--- Resultado Final ---")
print("Melhor subconjunto de features:", melhor_solucao)
print("Número de features selecionadas:", np.sum(melhor_solucao))
print("Fitness final:", melhor_fitness)
