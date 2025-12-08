from __future__ import annotations

from math import prod, sqrt


class Vector3:
    def __init__(self, x: int, y: int, z: int) -> None:
        self.x = x
        self.y = y
        self.z = z

    def get_distance(self, other_point: Vector3) -> float:
        return sqrt(
            (self.x - other_point.x) ** 2
            + (self.y - other_point.y) ** 2
            + (self.z - other_point.z) ** 2,
        )


with open("day08/input1.txt") as file:
    points = [
        Vector3(int(parts[0]), int(parts[1]), int(parts[2]))
        for parts in [line.split(",") for line in [x.strip() for x in file]]
    ]

distances: dict[str, float] = {}

for index1, point1 in enumerate(points):
    for index2, point2 in enumerate(points):
        if (
            index1 == index2
            or (str(index1) + "," + str(index2)) in distances
            or (str(index2) + "," + str(index1)) in distances
        ):
            continue

        distances[str(index1) + "," + str(index2)] = point1.get_distance(point2)

distance_list = [
    distance[0].split(",")
    for distance in sorted(distances.items(), key=lambda item: item[1])[:1000]
]

circuit_list: list[set[str]] = []

for point1, point2 in distance_list:
    combined_circuit: set[str] = {point1, point2}

    for circuit in circuit_list.copy():
        if point1 in circuit and point2 in circuit:
            combined_circuit.clear()
            break

        if point1 in circuit or point2 in circuit:
            combined_circuit = combined_circuit.union(circuit)
            circuit_list.remove(circuit)

    if len(combined_circuit) > 0:
        circuit_list.append(combined_circuit)

print(
    prod(
        [len(circuit) for circuit in sorted(circuit_list, key=len, reverse=True)[:3]],
    ),
)
