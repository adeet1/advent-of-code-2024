# Go through each page ordering rule
# 47 < 53
# 97 < 13
# ...
#
# Sort all of the numbers in the page ordering rules, based on the rules
#
# Then go through each update and make sure it's sorted according to the rules

import networkx as nx
import matplotlib.pyplot as plt

rules = []
with open("input/day5.txt", "r") as file:
    for line in file:
        if line == "\n":
            break
        
        rules.append(line[:-1].split("|"))

for rule in sorted(rules):
    print(rule)

# Create a directed graph (DAG)
dag = nx.DiGraph()

# Add nodes and edges
dag.add_edges_from(rules)

# # Draw the graph
# plt.figure(figsize=(8, 6))  # Set the figure size
# pos = nx.spring_layout(dag)  # Define the layout of nodes
# nx.draw(dag, pos, with_labels=True, node_color="lightblue", edge_color="gray", node_size=2000, font_size=15)

# # Show the graph
# plt.title("Directed Acyclic Graph (DAG)")
# plt.show()

print(nx.is_directed_acyclic_graph(dag))
# print(list(nx.topological_sort(dag)))