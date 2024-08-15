import networkx as nx
from collections import deque

# Граф з першого завдання
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

# Реалізація BFS
def bfs(graph, start, goal):
    visited = set()
    queue = deque([[start]])
    
    if start == goal:
        return [start]
    
    while queue:
        path = queue.popleft()
        node = path[-1]
        
        if node not in visited:
            neighbors = graph[node]
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                
                if neighbor == goal:
                    return new_path
            
            visited.add(node)
    
    return None

# Реалізація DFS
def dfs(graph, start, goal, path=None, visited=None):
    if path is None:
        path = []
    if visited is None:
        visited = set()
    
    path.append(start)
    visited.add(start)
    
    if start == goal:
        return path
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            result = dfs(graph, neighbor, goal, path, visited)
            if result:
                return result
    
    path.pop()
    return None

# Виконання алгоритмів
start_station = "Академмістечко"
goal_station = "Театральна"

dfs_path = dfs(G, start_station, goal_station)
bfs_path = bfs(G, start_station, goal_station)

# Генерація файлу README.md
readme_content = f"""
# Завдання 2: Реалізація та порівняння алгоритмів DFS і BFS

## Опис
У цьому завданні було реалізовано алгоритми пошуку у глибину (DFS) та пошуку у ширину (BFS) для знаходження шляхів у графі, який моделює станції Київського метро. Граф було створено у першому завданні.

## Результати виконання алгоритмів

- **DFS шлях**: {dfs_path}
- **BFS шлях**: {bfs_path}

## Порівняння та пояснення

- **DFS** досліджує граф глибше, що може призводити до знаходження більш довгого шляху до цілі. Це особливо помітно в графах з великою кількістю вузлів.
- **BFS** гарантує знаходження найкоротшого шляху за кількістю ребер. Це досягається тим, що алгоритм проходить всі вузли на кожному рівні перед тим, як перейти до наступного рівня.

Таким чином, BFS є більш ефективним для знаходження найкоротшого шляху у незважених графах, таких як наш граф станцій метро.
"""

# Запис у файл
with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)

print("README.md файл успішно створено!")
