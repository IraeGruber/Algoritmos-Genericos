# Seleção de Features com Algoritmo Genético

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Numpy](https://img.shields.io/badge/Numpy-1.21%2B-orange.svg)

## 📝 Descrição do Projeto

Este projeto é uma implementação em Python de um **Algoritmo Genético (AG)**, uma meta-heurística de otimização inspirada na teoria da evolução de Charles Darwin. O código é uma demonstração prática dos conceitos apresentados em pesquisas sobre o tema, como o artigo *"[A systematic literature review of the Genetic Algorithm based Feature Selection for machine learning](https://www.sciencedirect.com/science/article/abs/pii/S0167404821002728)"*.

O objetivo do algoritmo é encontrar o **subconjunto ideal de features** (características) em um conjunto de dados, buscando um equilíbrio entre dois objetivos conflitantes:
1.  **Maximizar a performance** de um modelo de Machine Learning (simulada nesta implementação).
2.  **Minimizar o número de features** utilizadas, promovendo modelos mais simples, rápidos e menos propensos a overfitting.

Cada "indivíduo" na população do AG representa uma possível solução, onde um vetor binário (cromossomo) indica a ausência (0) ou presença (1) de uma feature.

## 🧬 Componentes do Algoritmo Genético

1.  **Inicialização:** Uma população de soluções (vetores binários) é criada aleatoriamente.
2.  **Avaliação (Fitness):** Cada solução é avaliada por uma função que calcula seu "valor". A fórmula busca minimizar o resultado de `(1 - Acurácia) + Penalidade`.
    * A **Acurácia** é **simulada** para fins didáticos.
    * A **Penalidade** aumenta proporcionalmente ao número de features selecionadas.
3.  **Seleção (Torneio):** Indivíduos com melhor fitness (menor valor) são selecionados com maior probabilidade para se tornarem "pais" da próxima geração.
4.  **Crossover (Recombinação Uniforme):** Os "pais" trocam material genético para criar "filhos", combinando características das soluções existentes.
5.  **Mutação (Bit-Flip):** Uma pequena chance de mutação (inverter um bit) é aplicada aos filhos para introduzir diversidade e explorar novas áreas do espaço de busca.
6.  **Elitismo:** Os melhores indivíduos da geração atual são transferidos diretamente para a próxima, garantindo que o progresso alcançado nunca seja perdido.
7.  **Repetição:** O ciclo se repete por um número definido de gerações, evoluindo a população em direção a uma solução cada vez melhor.

## 🛠️ Tecnologias e Bibliotecas

* **Linguagem:** Python 3
* **Bibliotecas Principais:**
    * **Numpy:** Para operações numéricas eficientes e manipulação de arrays.

## 📁 Estrutura do Projeto

O projeto é contido em um único script para facilitar a execução e o entendimento.

```bash
selecao-features-ag/
├── main.py      # Script principal com toda a lógica do AG
└── README.md    # Esta documentação
```

## 🚀 Como Rodar o Projeto

#### **Pré-requisitos**

* **Python** (versão 3.8 ou superior)
* **pip** (gerenciador de pacotes do Python)

#### **1. Configuração do Ambiente**

É recomendado o uso de um ambiente virtual (`venv`) para isolar as dependências.

```bash
# Crie um ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# No Windows:
.\venv\Scripts\activate
# No macOS/Linux:
source venv/bin/activate

# Instale as dependências
pip install numpy
```

#### **2. Executando a Aplicação**

Este projeto **não requer um arquivo de dados externo**, pois opera com um dataset e uma função de fitness simulados para focar na mecânica do algoritmo.

Com o ambiente ativado, execute o seguinte comando no terminal:

```bash
python main.py
```

#### **Saída Esperada**

Ao final da execução, o terminal exibirá um resultado similar a este:

```
Iniciando otimização...
Geração 10/50 | Melhor Fitness: 0.2815 | Features: 8
Geração 20/50 | Melhor Fitness: 0.2601 | Features: 7
Geração 30/50 | Melhor Fitness: 0.2455 | Features: 5
Geração 40/50 | Melhor Fitness: 0.2455 | Features: 5
Geração 50/50 | Melhor Fitness: 0.2455 | Features: 5

--- Resultado Final ---
Melhor subconjunto de features: [0 1 0 0 1 0 ... 1 0 1 0 1]
Número de features selecionadas: 5
Fitness final: 0.2455
```

## 🔧 De Simulação para Aplicação Real

Para adaptar este projeto a um problema real, a principal mudança ocorre na função `calcular_fitness`. Em vez de simular a acurácia, você deve treiná-la e avaliá-la usando um modelo de Machine Learning real.

A lógica seria a seguinte:

```python
# Exemplo de como a função fitness seria em um caso real
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def calcular_fitness_real(individuo, dataset, labels):
    indices_ativos = [i for i, bit in enumerate(individuo) if bit == 1]
    
    if len(indices_ativos) == 0:
        return float('inf')

    # 1. Selecionar apenas as features ativas
    X_selecionado = dataset[:, indices_ativos]

    # 2. Dividir os dados
    X_train, X_test, y_train, y_test = train_test_split(X_selecionado, labels, test_size=0.3, stratify=labels)

    # 3. Treinar e avaliar o modelo
    model = RandomForestClassifier(n_estimators=50)
    model.fit(X_train, y_train)
    acuracia_real = accuracy_score(y_test, model.predict(X_test))

    # 4. Calcular o fitness com a acurácia real
    proporcao_usada = len(indices_ativos) / len(individuo)
    penalidade = proporcao_usada * 0.2
    fitness = (1 - acuracia_real) + penalidade
    
    return fitness
```