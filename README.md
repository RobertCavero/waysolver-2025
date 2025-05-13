
# Waysolver-2025

O Waysolver é um programa executável que permite ao usuário visualizar o funcionamento de um sistema de navegação em conjunto com conceitos da áreas de **Estrutura de Dados**, **Linguagens Formais e Autômatos** e **Teoria dos Grafos e Complexidade**. Ademais, o projeto é direcionado a usuários com interesse em compreender melhor o funcionamento do algoritmo A* e sua aplicação prática.


## Utilização

Por se tratar de um arquivo .exe, seu funcionamento é limitado a computadores com o sistema operacional Windows. Uma de suas funcionalidades é chamada "Carregar Mapa", para utilizá-la basta utilizar um arquivo .txt escrito da seguinte maneira:

```
S . . X . . X . . .
. X . . . X . X . .
. X . . . . . . X .
. . X X . X X . . .
. . . . . . . . . .
X . X . X . X . X .
. . . X . . . . . .
. X . . . X X . . X
. . . . X . . X . E
X . X . . . X . . .
```
```S``` = ponto inicial (Start)

```E``` = ponto final (End)

```X``` = Obstáculos

```.``` = Espaço livre

**Os demais botões são:**

Iniciar - Inicia a busca pela rota mais curta. Utilizável quando o ponto inicial e o ponto final já estiverem definidos.

Resertar - limpa todos o mapa da aplicação, incluindo o ponto inicial e final.

Modo Obstáculo/Modo Normal - botão que alterna entre as funcionalidades de desenhar manualmente os obstáculos e de escolher o ponto inicial e final.

Gerar labirinto - torna de maneira aleatória 30% das espaços livres em obstáculos, criando assim um labirinto.

Carregar mapa - utilizando um arquivo .txt escrito com base na notação simples supracitada.


## Conceitos Utilizados

## 1. Estrutura de Dados – Mapa como Grafo em Lista de Adjacência

- Implementado com a classe `Spot`, ou seja, cada célula da grade (grid) é um nó.
- Vizinhos atualizados com `update_neighbors()`, que define os vizinhos (arestas do grafo), simulando uma **lista de adjacência**.

---

## 2. Linguagens Formais e Autômatos – Definição de Pontos e Caminhos

- O código inclui uma **notação simbólica** para representar mapas.
- Cada símbolo no arquivo .txt tem um significado específico:
  
  | Símbolo | Estado Representado     |
  |---------|--------------------------|
  | `S`     | Início (`start`)         |
  | `E`     | Fim (`end`)              |
  | `X`     | Barreira (`barrier`)     |
  | `.`     | Espaço livre (vazio)     |

## 3. Teoria dos Grafos e Complexidade – Algoritmo A*

- Foi implementado o algoritmo **A\***.
- Heurística utilizada: **Distância de Manhattan**
- Uso de `PriorityQueue` garante complexidade **O((E + V) log V)**.
- O código emprega:
  - Estrutura de prioridade
  - Heurística
  - Controle de estados

---

## 4. Aplicação Prática – Rotas entre Cidades

- A aplicação simula um mapa onde o usuário define:
  - Início (`start`)
  - Fim (`end`)
  - Barreiras (`barrier`)
- O botão **Gerar Labirinto** adiciona obstáculos, simulando cenários reais.
- A estrutura pode ser adaptada para representar:
  - **Cidades e estradas**
  - Com **nomes** e **pesos** (distâncias)

  
## Autores

- [@alesko29](https://github.com/alesko29)
- [@andrey-angeli](https://github.com/andrey-angeli)
- [@Dugi0204](https://github.com/Dugi0204)
- [@joelSDB](https://github.com/joelSDB)
- [@Nathan-Guisi](https://github.com/Nathan-Guisi)
- [@PaulohlmPereira](https://github.com/PaulohlmPereira)
- [@t4ur06](https://github.com/t4ur06)
- [@Junindalost](https://github.com/Junindalost)
- [@RobertCavero](https://github.com/RobertCavero)



