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
    for parent_bag in graph.predecessors(bag):
        parent_bags.append(parent_bag)
        parent_bags += (get_all_predecessors(parent_bag, graph))

    return parent_bags


def get_all_successors(bag: str, graph: nx.MultiDiGraph) -> set:
    child_bags = []
    for child_bag in graph.successors(bag):
        succ = get_all_successors(child_bag, graph)

        for i in range(graph.number_of_edges(bag, child_bag)):
            child_bags.append(child_bag)
            child_bags += succ

    return child_bags


if __name__ == "__main__":

    with open(os.path.join(os.path.dirname(__file__), "input.txt")) as file:
        raw_bag = file.read()

    graph = create_graph(raw_bag)
    predecessors = get_all_successors("shiny gold", graph)
    print(len(predecessors))
