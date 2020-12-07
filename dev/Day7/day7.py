import os
import networkx as nx  # https://networkx.org/
import re


def create_graph(raw_bag: str) -> nx.MultiDiGraph:
    graph = nx.MultiDiGraph()

    lines = raw_bag.splitlines()
    for line in lines:
        if "contain no other bag" in line:
            continue

        definition_bag, raw_containing_bags = line.split(" bags contain ")
        graph.add_node(definition_bag)

        raw_containing_bags = raw_containing_bags.split(", ")
        for bag in raw_containing_bags:
            definition = bag.split(" bag")[0]

            match = re.match(r"([0-9]+) *([a-z ]+)", definition)
            num, color_bag = match.groups()
            graph.add_node(color_bag)
            for i in range(int(num)):
                graph.add_edge(definition_bag, color_bag)
    return graph


def get_all_predecessors(bag: str, graph: nx.MultiDiGraph) -> set:
    parent_bags = []
    for contain_bag in graph.predecessors(bag):
        parent_bags.append(contain_bag)
        parent_bags += (get_all_predecessors(contain_bag, graph))

    return parent_bags


if __name__ == "__main__":

    with open(os.path.join(os.path.dirname(__file__), "input.txt")) as file:
        raw_bag = file.read()

    graph = create_graph(raw_bag)
    predecessors = get_all_predecessors("shiny gold", graph)
    print(len(set(predecessors)))
