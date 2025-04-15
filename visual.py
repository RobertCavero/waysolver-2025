import matplotlib.pyplot as plt

# Matriz com [x, y, cor]
matriz = [
    [1.0, 2.5, "red"],
    [3.2, 4.8, "blue"],
    [5.0, 6.1, "green"],
    [2.5, 3.5, "orange"]
]

# Separando x, y e cores
x = [linha[0] for linha in matriz]
y = [linha[1] for linha in matriz]
cores = [linha[2] for linha in matriz]

# Criando gráfico de dispersão
plt.scatter(x, y, c=cores)

# Rótulos e título (opcional)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Gráfico de Dispersão com Cores")

plt.grid(True)
plt.show()

