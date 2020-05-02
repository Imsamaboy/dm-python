""" Модуль класса для графов"""

import datetime
import os
from typing import List, Optional

import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing import nx_agraph


# петли и кратные ребра разрешены
class DMGraph(nx.DiGraph):
    """
    На данный момент будем поддерживать только инициализацию списком ребер, т.к.
    это самый распространенный случай использования. В дальнейшем мб стоит изменить
     """

    def __init__(self, edge_initialization: Optional[List] = None):
        """
        :param edge_initialization: список ребер (допускает петли и кратные ребра)
        """

        super(DMGraph, self).__init__(edge_initialization)

    def visualise(self, save_file: Optional[bool] = False, file_path: Optional[str] = None) -> None:
        """
        Нарисовать граф с помощью pygraphviz+matplotlib. pygraphviz используется как
        единственная найденная мной крупная библиотека визуализации графов, способная надежно
        рисовать петли и кратные ребра без танцев с бубном. Единственный недостаток - она создает
        файл картинки и по-другому не может, приходится это обходить

        :param save_file: True or False. Сохранить файл или нет
        :param file_path: Путь к файлу. Если предоставлен, то картнка сохраняется и после вызова функции
        """
        if file_path:
            save_file = True
            filename = file_path
        else:
            filename = f'DMGraph_{datetime.datetime.now().strftime("%H.%M.%S")}.png'
        agraph_instance = nx_agraph.to_agraph(self)  # AGraph - типа для графа в pygraphviz
        agraph_instance.layout(prog='dot')
        agraph_instance.draw(filename)
        graph_img = plt.imread(filename)
        plt.axis('off')
        plt.imshow(graph_img)
        plt.show()
        if not save_file:
            os.remove(filename)


if __name__ == "__main__":
    t = DMGraph([(1, 2), (2, 3), (3, 3), (8, 9), (9, 10), (10, 8)])
    t.visualise()
