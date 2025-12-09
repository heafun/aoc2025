with open("day09/input1.txt") as file:
    points = [
        [int(axis) for axis in point]
        for point in [line.strip().split(",") for line in file]
    ]

max_area = 0

for index1, point1 in enumerate(points):
    for point2 in points[index1 + 1 :]:
        area = (abs(point1[0] - point2[0]) + 1) * (abs(point1[1] - point2[1]) + 1)

        max_area = max(area, max_area)

print(max_area)
