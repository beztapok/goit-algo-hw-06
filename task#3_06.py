import networkx as nx
import heapq

# Граф з вагами ребер
G = nx.Graph()

# Додавання вершин (станцій метро)
stations = ["Академмістечко", "Житомирська", "Святошин", "Нивки", 
            "Берестейська", "Шулявська", "Політехнічний інститут", 
            "Вокзальна", "Університет", "Театральна"]
G.add_nodes_from(stations)

# Додавання ребер з вагами (час у хвилинах між станціями)
edges_with_weights = [
    ("Академмістечко", "Житомирська", 4), 
    ("Житомирська", "Святошин", 3),
    ("Святошин", "Нивки", 5), 
    ("Нивки", "Берестейська", 6), 
    ("Берестейська", "Шулявська", 4), 
    ("Шулявська", "Політехнічний інститут", 3), 
    ("Політехнічний інститут", "Вокзальна", 2), 
    ("Вокзальна", "Університет", 3), 
    ("Університет", "Театральна", 2)
]

G.add_weighted_edges_from(edges_with_weights)

# Реалізація алгоритму Дейкстри
def dijkstra(graph, start):
    # Ініціалізація відстаней до всіх вершин як нескінченність
    distances = {vertex: float('infinity') for vertex in graph.nodes}
    distances[start] = 0  # Відстань від стартової вершини до себе
    priority_queue = [(0, start)]  # Черга пріоритету для обробки вершин

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # Якщо знайдена відстань до вершини більша за поточну, продовжити
        if current_distance > distances[current_vertex]:
            continue
        
        # Оновлення відстаней до сусідніх вершин
        for neighbor, attributes in graph[current_vertex].items():
            distance = current_distance + attributes['weight']
            
            # Якщо нова відстань до сусіда менша, ніж попередня
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Знаходження найкоротших шляхів від кожної вершини
all_shortest_paths = {}
for station in stations:
    all_shortest_paths[station] = dijkstra(G, station)

# Виведення результатів
for start_station, paths in all_shortest_paths.items():
    print(f"Найкоротші шляхи від станції {start_station}:")
    for end_station, distance in paths.items():
        print(f"  До станції {end_station}: {distance} хвилин")
