# Seleção de Features com Algoritmo Genético

## 📝 Descrição do Projeto

Este projeto é uma implementação em Python de um **Algoritmo Genético (AG)**, uma técnica de busca e otimização inspirada na teoria da evolução de Charles Darwin. O objetivo do algoritmo é encontrar o **subconjunto ideal de features** (características) em um conjunto de dados.

A otimização busca um equilíbrio entre dois objetivos:
1.  Maximizar a acurácia de um modelo de Machine Learning (simulada nesta implementação).
2.  Minimizar o número de features utilizadas, promovendo modelos mais simples e eficientes.

Cada "indivíduo" na população do algoritmo genético representa uma possível solução, onde cada gene (0 ou 1) indica a ausência ou presença de uma feature específica.

## 🛠️ Tecnologias e Bibliotecas

*   **Linguagem:** Python 3
*   **Bibliotecas Principais:**
    *   **Numpy:** Para operações numéricas eficientes e manipulação de arrays.

-----

## 📁 Estrutura do Projeto

O projeto é contido em um único script, facilitando a execução e o entendimento.

```bash
algoritmos-genericos/
├── main.py         # Script principal com toda a lógica do AG
└── README.md       # Documentação do projeto
```

-----

## 🚀 Como Rodar o Projeto

### **Pré-requisitos**

*   **Python** (versão 3.8 ou superior)
*   **pip** (gerenciador de pacotes do Python)

### **1. Configuração do Ambiente**

É recomendado o uso de um ambiente virtual para isolar as dependências do projeto.

```bash
# Crie um ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# No Windows:
.\venv\Scripts\activate
# No macOS/Linux:
# source venv/bin/activate

# Instale as dependências
pip install numpy
```

### **2. Base de Dados**

*   Este projeto **não requer um arquivo de dados externo**. Ele opera com um dataset e labels gerados aleatoriamente (`dataset_simulado` e `labels_simulados`) para demonstrar o funcionamento do algoritmo.
*   A função de fitness também é **simulada** para representar o desempenho de um modelo de classificação.

### **3. Executando a Aplicação**

*   Com o ambiente virtual ativado e as dependências instaladas, execute o seguinte comando no terminal:

```bash
python main.py
```

*   Ao final da execução, o terminal exibirá o melhor subconjunto de features encontrado, o número de features selecionadas e o valor de fitness correspondente.

-----

## 🧬 Funcionamento do Algoritmo Genético

1.  **Inicialização:** Uma população de indivíduos (soluções) é criada aleatoriamente.
2.  **Avaliação (Fitness):** Cada indivíduo é avaliado por uma função de fitness, que penaliza soluções com muitas features e recompensa aquelas com alta acurácia (simulada).
3.  **Seleção:** Indivíduos com melhor fitness são selecionados com maior probabilidade para se tornarem "pais" da próxima geração (usando o método de torneio).
4.  **Crossover (Recombinação):** Os "pais" trocam material genético para criar "filhos", combinando características das soluções existentes.
5.  **Mutação:** Uma pequena chance de mutação aleatória é aplicada aos genes dos filhos para introduzir nova diversidade genética na população.
6.  **Elitismo (Adicionado):** O melhor indivíduo da geração atual é transferido diretamente para a próxima, garantindo que o progresso não seja perdido.
7.  **Repetição:** O ciclo se repete por um número definido de gerações, evoluindo a população em direção a uma solução ótima.