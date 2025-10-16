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
├── main.py      
└── README.md   
```

## 🚀 Como Rodar o Projeto

#### **Pré-requisitos**

* **Python** (versão 3.8 ou superior)
* **pip** (gerenciador de pacotes do Python)

#### **Executando a Aplicação**

Este projeto **não requer um arquivo de dados externo**, pois opera com um dataset e uma função de fitness simulados para focar na mecânica do algoritmo.

Com o ambiente ativado, execute o seguinte comando no terminal:

```bash
python main.py
```
## 👨‍💻 Estudantes

<table>
  <tr>
    <td align="center">
      <a href="#">
        <img src="https://avatars.githubusercontent.com/u/165969703?v=4" width="100px;" alt="Iraê"/><br>
        <sub>
          <b>Iraê Ervin Gruber da Silva</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="#">
        <img src="https://avatars.githubusercontent.com/u/165967253?s=96&v=4" width="100px;" alt="Jefferson"/><br>
        <sub>
          <b>Jefferson Alan Schmidt Ludwig</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="#">
        <img src="https://avatars.githubusercontent.com/u/166339825?v=4" width="100px;" alt="Lucas"/><br>
        <sub>
          <b>Lucas Maciel Delvalle Kesler</b>
        </sub>
      </a>
    </td>
  </tr>
</table>
