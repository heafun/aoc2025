class Node:
    def __init__(self, beam_index: int) -> None:
        self.beam_index = beam_index
        self.children: list[Node] = []
        self.visited = False
        self.possibilities: int = 0


def count_possibilities(node: Node) -> int:
    if len(node.children) == 0:
        return 1

    if node.visited:
        return node.possibilities

    possiblities = sum([count_possibilities(child) for child in node.children])

    node.possibilities = possiblities
    node.visited = True
    return possiblities


with open("day07/input1.txt") as file:
    lines = [x.strip() for x in file]

root_node = Node(lines[0].index("S"))
tree_leaves: dict[int, Node] = {}

tree_leaves[root_node.beam_index] = root_node

for line in lines:
    for leave in tree_leaves.copy().values():
        if line[leave.beam_index] == "^":
            tree_leaves.pop(leave.beam_index)

            if leave.beam_index - 1 in tree_leaves:
                leave.children.append(tree_leaves[leave.beam_index - 1])
            else:
                new_leave = Node(leave.beam_index - 1)
                leave.children.append(new_leave)
                tree_leaves[new_leave.beam_index] = new_leave

            if leave.beam_index + 1 in tree_leaves:
                leave.children.append(tree_leaves[leave.beam_index + 1])
            else:
                new_leave = Node(leave.beam_index + 1)
                leave.children.append(new_leave)
                tree_leaves[new_leave.beam_index] = new_leave

print(count_possibilities(root_node))
