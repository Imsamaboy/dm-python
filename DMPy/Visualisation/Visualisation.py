""" Модуль с функциями для визуализаций """
import matplotlib.pyplot as plt
import networkx as nx


def draw_cycle_tree(edge_list, node_size_multiplier=30000):
    """ Рисовалка для циклодеревьев. """
    G = nx.DiGraph(edge_list)
    nodes = list(zip(*edge_list))
    loop_nodes = []
    for index, edge in enumerate(edge_list):
        if edge[0] == edge[1]:
            loop_nodes.append(edge[0])

    # source_only_nodes = set(nodes[0]) - set(nodes[1])
    # edge_list = [edge for edge in edge_list if
    #              edge[0] not in source_only_nodes]
    in_degrees = []
    loop_nodes_degree = []
    for node, deg in G.in_degree(G.nodes):
        in_degrees.append(deg)
        if node in loop_nodes:
            loop_nodes_degree.append(deg)
    pos = nx.random_layout(G)
    nx.draw_networkx_nodes(G, pos,
                           node_color=in_degrees,
                           cmap=plt.cm.Blues,
                           node_size=[
                               node_size_multiplier * degree / len(edge_list)
                               for degree in in_degrees]
                           )
    nx.draw_networkx_nodes(G, pos,
                           nodelist=loop_nodes,
                           node_color='red',
                           node_size=[
                               node_size_multiplier * degree / len(edge_list)
                               for degree in
                               loop_nodes_degree],
                           alpha=1.0,
                           node_shape='d')
    plt.axis("off")
    plt.show()


def draw_cayley_table(op):
    pass
