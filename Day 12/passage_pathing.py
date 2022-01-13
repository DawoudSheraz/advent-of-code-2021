"""
Day 12: Passage Pathing.
"""

TEST_DATA = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

TEST_DATA_1 = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""

PUZZLE_INPUT = """end-MY
MY-xc
ho-NF
start-ho
NF-xc
NF-yf
end-yf
xc-TP
MY-qo
yf-TP
dc-NF
dc-xc
start-dc
yf-MY
MY-ho
EM-uh
xc-yf
ho-dc
uh-NF
yf-ho
end-uh
start-NF"""


class Graph:
    """
    Graph data structure representation with dict.
    """

    END_NODE = 'end'
    START_NODE = 'start'
    MAX_CAVE_VISIT = 2

    def __init__(self):
        self.graph = {}
        self.path_count = 0

    def reset_path_count(self):
        self.path_count = 0

    def add_edge(self, node_1, node_2):
        if node_1 not in self.graph:
            self.graph[node_1] = []
        if node_2 not in self.graph:
            self.graph[node_2] = []
        self.graph[node_1].append(node_2)
        self.graph[node_2].append(node_1)

    def build_graph(self, input_str):
        edges = input_str.splitlines()
        for edge in edges:
            node_1, node_2 = edge.split('-')
            self.add_edge(node_1, node_2)

    def find_paths(self, current_node, path, visited):
        """
        Part 1 where a simple list is used to keep track of small caves visited.
        """
        if current_node.islower() and current_node not in visited:
            visited.append(current_node)
        elif current_node.islower() and current_node in visited:
            return False

        path += ',' + current_node

        if current_node == self.END_NODE:
            self.path_count += 1
            return True

        for connected_node in self.graph[current_node]:
            current_path = path
            current_visited = visited.copy()
            self.find_paths(connected_node, current_path, current_visited)
        return True

    def find_paths_part_2(self, current_node, path, visited):
        """
        Part 2 uses dict to track visit count of small cave and ensures only
        one small cave is visited twice.
        """
        if current_node == self.END_NODE:
            self.path_count += 1
            return True

        if current_node.islower() and current_node not in visited:
            visited[current_node] = 1
        elif current_node.islower() and current_node in visited:
            if (self.MAX_CAVE_VISIT in list(visited.values())) \
                    or visited[current_node] == self.MAX_CAVE_VISIT\
                    or current_node == self.START_NODE:
                return False
            visited[current_node] += 1

        path += ',' + current_node

        for connected_node in self.graph[current_node]:
            current_path = path
            current_visited = visited.copy()
            self.find_paths_part_2(connected_node, current_path, current_visited)
        return True


graph = Graph()
graph.build_graph(PUZZLE_INPUT)
graph.find_paths('start', '', [])
print("Part 1:", graph.path_count)
graph.reset_path_count()
graph.find_paths_part_2('start', '', {})
print("Part 2:", graph.path_count)
