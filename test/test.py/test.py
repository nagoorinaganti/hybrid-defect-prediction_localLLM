from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Tuple
import heapq
import random

# -----------------------------
# Graph + A* Pathfinding Engine
# -----------------------------

@dataclass(order=True)
class PriorityNode:
    priority: float
    node: str = field(compare=False)
    cost: float = field(compare=False)
    path: List[str] = field(compare=False, default_factory=list)

class WeightedGraph:
    def __init__(self):
        self.graph: Dict[str, List[Tuple[str, int]]] = {}
        self.coordinates: Dict[str, Tuple[int, int]] = {}

    def add_node(self, node: str, x: int, y: int):
        self.graph[node] = []
        self.coordinates[node] = (x, y)

    def add_edge(self, src: str, dest: str, weight: int):
        self.graph[src].append((dest, weight))
        self.graph[dest].append((src, weight))

    def heuristic(self, a: str, b: str) -> float:
        x1, y1 = self.coordinates[a]
        x2, y2 = self.coordinates[b]
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    def a_star(self, start: str, goal: str):
        pq = []
        heapq.heappush(pq, PriorityNode(0, start, 0, [start]))

        visited = {}

        while pq:
            current = heapq.heappop(pq)

            if current.node == goal:
                return current.path, current.cost

            if current.node in visited and visited[current.node] <= current.cost:
                continue

            visited[current.node] = current.cost

            for neighbor, weight in self.graph[current.node]:
                new_cost = current.cost + weight
                priority = new_cost + self.heuristic(neighbor, goal)

                heapq.heappush(
                    pq,
                    PriorityNode(
                        priority,
                        neighbor,
                        new_cost,
                        current.path + [neighbor]
                    )
                )

        return None, float("inf")


# -----------------------------
# Simulation
# -----------------------------

def generate_random_graph(size: int = 10) -> WeightedGraph:
    g = WeightedGraph()

    for i in range(size):
        node = chr(65 + i)
        g.add_node(node, random.randint(0, 100), random.randint(0, 100))

    nodes = list(g.graph.keys())

    for _ in range(size * 2):
        a, b = random.sample(nodes, 2)
        weight = random.randint(1, 20)
        g.add_edge(a, b, weight)

    return g


def main():
    graph = generate_random_graph(12)

    start = "A"
    goal = "L"

    path, cost = graph.a_star(start, goal)

    print("=" * 50)
    print("A* PATHFINDING RESULT")
    print("=" * 50)

    if path:
        print(f"Shortest Path : {' -> '.join(path)}")
        print(f"Total Cost    : {cost}")
    else:
        print("No path found.")

    print("\nGraph Structure:")
    for node, edges in graph.graph.items():
        print(f"{node}: {edges}")


if __name__ == "__main__":
    main()