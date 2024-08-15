import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання вершин (станцій метро)
stations = ["Академмістечко", "Житомирська", "Святошин", "Нивки", 
            "Берестейська", "Шулявська", "Політехнічний інститут", 
            "Вокзальна", "Університет", "Театральна"]
G.add_nodes_from(stations)

# Додавання ребер (зв'язків між станціями)
edges = [("Академмістечко", "Житомирська"), 
         ("Житомирська", "Святошин"),
         ("Святошин", "Нивки"), 
         ("Нивки", "Берестейська"), 
         ("Берестейська", "Шулявська"), 
         ("Шулявська", "Політехнічний інститут"), 
         ("Політехнічний інститут", "Вокзальна"), 
         ("Вокзальна", "Університет"), 
         ("Університет", "Театральна")]

G.add_edges_from(edges)

# Візуалізація графа
plt.figure(figsize=(10, 8))
nx.draw(G, with_labels=True, node_color="lightblue", font_size=12, node_size=1000, edge_color="gray")
plt.title("Граф станцій Київського метро")
plt.show()

# Аналіз графа
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degrees = dict(G.degree())

print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print("Ступені вершин:")
for station, degree in degrees.items():
    print(f"{station}: {degree}")
