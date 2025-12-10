# For visualizing the test case
def test_print(size: int) -> None:
    for y in range(size):
        for x in range(size):
            if (x, y) in edges:
                print("#", end="")
            elif (x, y) in outside_points:
                print("O", end="")
            else:
                print(".", end="")
        print()


def draw_edge(start: tuple[int, int], end: tuple[int, int]) -> None:
    if start[0] == end[0]:  # vertical edge
        offset = -1 if start[1] < end[1] else 1

        edges.update({(start[0], y) for y in range(start[1], end[1], offset * -1)})
        outside_points.update(
            {
                (start[0] - offset, y)
                for y in range(start[1], end[1] - offset, offset * -1)
            },
        )

    else:  # horizontal edge
        offset = -1 if start[0] < end[0] else 1

        edges.update({(x, start[1]) for x in range(start[0], end[0], offset * -1)})
        outside_points.update(
            {
                (x, start[1] + offset)
                for x in range(start[0], end[0] - offset, offset * -1)
            },
        )


def is_valid_rectangle(corner1: tuple[int, int], corner2: tuple[int, int]) -> bool:
    if corner1[0] == corner2[0] or corner1[1] == corner2[1]:
        return is_valid_edge(corner1, corner2)

    corners = [corner1, (corner1[0], corner2[1]), corner2, (corner2[0], corner1[1])]

    for index in range(len(corners)):
        if not is_valid_edge(corners[index], corners[(index + 1) % 4]):
            return False

    return True


def is_valid_edge(start: tuple[int, int], end: tuple[int, int]) -> bool:
    if start[0] == end[0]:  # vertical edge
        offset = -1 if start[1] < end[1] else 1

        return outside_points.isdisjoint(
            {(start[0], y) for y in range(start[1], end[1], offset * -1)},
        )

    # horizontal edge
    offset = -1 if start[0] < end[0] else 1

    return outside_points.isdisjoint(
        {(x, start[1]) for x in range(start[0], end[0], offset * -1)},
    )


def no_points_inside(corner1: tuple[int, int], corner2: tuple[int, int]) -> bool:
    if corner1[0] == corner2[0] or corner1[1] == corner2[1]:
        return True

    min_x = min(corner1[0], corner2[0])
    max_x = max(corner1[0], corner2[0])
    min_y = min(corner1[1], corner2[1])
    max_y = max(corner1[1], corner2[1])

    for point in points:
        if min_x < point[0] < max_x and min_y < point[1] < max_y:
            return False

    return True


with open("day09/input1.txt") as file:
    points = [
        (int(point[0]), int(point[1]))
        for point in [line.strip().split(",") for line in file]
    ]

# Prepare points so that left side of an edge is outside
most_left_pos = min([point[0] for point in points])
start, end = [point for point in points if point[0] == most_left_pos][:2]

if start[1] < end[1]:  # Leading down -> left is inside
    points.reverse()

# Prepare outside points for validation
edges: set[tuple[int, int]] = set()
outside_points: set[tuple[int, int]] = set()

for index in range(len(points) - 1):
    draw_edge(points[index], points[index + 1])

draw_edge(points[-1], points[0])

outside_points.difference_update(edges)

# Get max valid rectangle
areas = []

points_length = len(points)

for index1, point1 in enumerate(points):
    for point2 in points[index1 + 1 :]:
        area = (abs(point1[0] - point2[0]) + 1) * (abs(point1[1] - point2[1]) + 1)

        if no_points_inside(point1, point2):
            areas.append([area, point1, point2])

areas.sort(key=lambda entry: entry[0], reverse=True)

for area in areas:
    if is_valid_rectangle(area[1], area[2]):
        print(area[0])
        break
