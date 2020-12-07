from dev.Day7 import day7


def test_example1():
    raw_bag = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""
    graph = day7.create_graph(raw_bag)
    predecessors = day7.get_all_predecessors("shiny gold", graph)
    assert 4 == (len(set(predecessors)))


def test_example2():
    raw_bag = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
"""
    graph = day7.create_graph(raw_bag)
    predecessors = day7.get_all_predecessors("shiny gold", graph)
    assert 0 == (len(set(predecessors)))
    successors = day7.get_all_successors("shiny gold", graph)
    assert 126 == len(successors)
