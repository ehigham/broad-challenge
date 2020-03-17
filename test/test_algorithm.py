# -*- coding: utf-8 -*-

import unittest
import networkx

from challenge.algorithm import dijkstras_shortest_path

class TestAlgorithmModule(unittest.TestCase):

    def test_empty_graph(self):
        """Nodes are memebers of graph.nodes"""
        graph = networkx.Graph()

        with self.assertRaises(ValueError):
            dijkstras_shortest_path(graph, 'A', 'C')

    def test_disjoint_graph(self):
        graph = networkx.Graph()
        graph.add_nodes_from(['A', 'B'])
        path = dijkstras_shortest_path(graph, 'A', 'B')
        self.assertListEqual(path, [])

    def test_path_to_itself(self):
        """A"""
        graph = networkx.Graph()
        graph.add_edges_from([('A', 'B'), ('B', 'C')])
        path = dijkstras_shortest_path(graph, 'A', 'A')
        self.assertListEqual(path, [])

    def test_simple_shortest_path(self):
        """A - B - C """
        graph = networkx.Graph()
        graph.add_edges_from([('A', 'B'), ('B', 'C')])
        path = dijkstras_shortest_path(graph, 'A', 'C')
        self.assertListEqual(path, ['A', 'B', 'C'])

    def test_shortcut_path(self):
        """
        A - B - C - D - E - F
             \\            /
                --- G ---
        """
        graph = networkx.Graph()
        graph.add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'F')])
        graph.add_edges_from([('B', 'G'), ('G', 'E')])
        path = dijkstras_shortest_path(graph, 'A', 'F')
        self.assertListEqual(path, ['A', 'B', 'G', 'E', 'F'])

    def test_cyclic_graph_path(self):
        """
        A - B - C - D - E
            |       |
              - G -
        """
        graph = networkx.Graph()
        graph.add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E')])
        graph.add_edges_from([('C', 'G'), ('G', 'B')])
        path = dijkstras_shortest_path(graph, 'A', 'E')
        self.assertListEqual(path, ['A', 'B', 'C', 'D', 'E'])

if __name__ == '__main__':
    unittest.main()
