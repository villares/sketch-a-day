#*- coding: utf-8 -*-

"""
A simple Python graph class, demonstrating the essential facts and functionalities of graphs
based on https://www.python-course.eu/graphs_python.php
and https://www.python.org/doc/essays/graphs/
"""

from random import choice

class Graph(object):

    def __init__(self, graph_dict=None):
        """
        Initialize a graph object with dictionary provided,
        if none provided, create an empty one.
        """
        if graph_dict is None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def __len__(self):
        return len(self.__graph_dict)

    def __iter__(self):
        return iter(self.__graph_dict.keys())
        

    def vertices(self):
        """Return the vertices of graph."""
        return list(self.__graph_dict.keys())

    def edges(self):
        """Return the edges of graph """
        return self.__generate_edges()

    def add_vertex(self, v):
        """
        If the vertex "vertex" is not in self.__graph_dict,
        add key "vertex" with an empty list as a value,
        otherwise, do nothing.
        """
        if v not in self.__graph_dict:
            self.__graph_dict[v] = set([])  # a versão com lista permitia multiplas arestas entre os mesmo vertices

    def add_edge(self, edge):
        """
        Assuming that edge is of type set, tuple or list;
        add edge between vertices. Can't add multiple edges!
        """
        edge = set(edge)
        vertex1 = edge.pop()
        if edge:
            # not a loop
            vertex2 = edge.pop()
            if vertex1 in self.__graph_dict:
                self.__graph_dict[vertex1].add(vertex2)
            else:
                self.__graph_dict[vertex1] = {vertex2}
            if vertex2 in self.__graph_dict:
                self.__graph_dict[vertex2].add(vertex1)
            else:
                self.__graph_dict[vertex2] = {vertex1}
        else:
            # a loop
            if vertex1 in self.__graph_dict:
                self.__graph_dict[vertex1].add(vertex1)
            else:
                self.__graph_dict[vertex1] = {vertex1}

    def remove_vertex(self, vert):
        del self.__graph_dict[vert]
        for k in self.__graph_dict.keys():
            if vert in self.__graph_dict[k]:
                self.__graph_dict[k].remove(vert)

    def remove_edge(self, edge, check_first=True):
        edge = set(edge)
        if check_first and edge not in self.__generate_edges():
            return False
        vertex1 = edge.pop()
        if edge:
            vertex2 = edge.pop()
            self.__graph_dict[vertex1].remove(vertex2)
            self.__graph_dict[vertex2].remove(vertex1)
        else:
            self.__graph_dict[vertex1].remove(vertex1)
        return True

    def __generate_edges(self):
        """
        Generate the edges, represented as sets with one
        (a loop back to the vertex) or two vertices.
        """
        edges = []
        for v in self.__graph_dict:
            for neighbour in self.__graph_dict[v]:
                if {neighbour, v} not in edges:
                    edges.append({v, neighbour})
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res

    def find_isolated_vertices(self):
        """
        Return a list of isolated vertices.
        """
        graph = self.__graph_dict
        isolated = []
        for v in graph:
            print(isolated, v)
            if not graph[v]:
                isolated += [v]
        return isolated

    def find_path(self, start_vertex, end_vertex, path=[]):
        """
        Find a path from start_vertex to end_vertex in graph.
        """
        graph = self.__graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path
        if start_vertex not in graph:
            return []
        for v in graph[start_vertex]:
            if v not in path:
                extended_path = self.find_path(v, end_vertex, path)
                if extended_path:
                    return extended_path
        return []

    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        """
        Find all paths from start_vertex to end_vertex.
        """
        graph = self.__graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in graph:
            return []
        paths = []
        for v in graph[start_vertex]:
            if v not in path:
                extended_paths = self.find_all_paths(v,
                                                     end_vertex,
                                                     path)
                for p in extended_paths:
                    paths.append(p)
        return paths

    def is_connected(self,
                     vertices_encountered=None,
                     start_vertex=None):
        """Find if the graph is connected."""
        if vertices_encountered is None:
            vertices_encountered = set()
        gdict = self.__graph_dict
        vertices = list(gdict.keys())  # "list" necessary in Python 3
        if not start_vertex:
            # chosse a vertex from graph as a starting point
            start_vertex = vertices[0]
        vertices_encountered.add(start_vertex)
        if len(vertices_encountered) != len(vertices):
            for v in gdict[start_vertex]:
                if v not in vertices_encountered:
                    if self.is_connected(vertices_encountered, v):
                        return True
        else:
            return True
        return False

    def vertex_degree(self, v):
        """
        Return the number of edges connecting to a vertex (the number of adjacent vertices).
        Loops are counted once.
        """
        adj_vertices = self.__graph_dict[v]
        degree = len(adj_vertices) # + adj_vertices.count(v)
        return degree

    def degree_sequence(self):
        """Calculates the degree sequence."""
        seq = []
        for v in self.__graph_dict:
            seq.append(self.vertex_degree(v))
        seq.sort(reverse=True)
        return tuple(seq)

    @staticmethod
    def is_degree_sequence(sequence):
        """
        Return True, if the sequence is a degree sequence (non-increasing),
        otherwise return False.
        """
        return all(x >= y for x, y in zip(sequence, sequence[1:]))

    def delta(self):
        """Find minimum degree of vertices."""
        minimum = 100000000
        for v in self.__graph_dict:
            vertex_degree = self.vertex_degree(v)
            if vertex_degree < minimum:
                minimum = vertex_degree
        return minimum

    def Delta(self):
        """Finde maximum degree of vertices."""
        maximum = 0
        for v in self.__graph_dict:
            vertex_degree = self.vertex_degree(v)
            if vertex_degree > maximum:
                maximum = vertex_degree
        return maximum

    def density(self):
        """Calculate the graph density."""
        g = self.__graph_dict
        V = len(g.keys())
        E = len(self.edges())
        return 2.0 * E / (V * (V - 1))

    def diameter(self):
        """Calculates the graph diameter."""

        v = self.vertices()
        pairs = [
            (v[i],
             v[j]) for i in range(
                len(v)) for j in range(
                i + 1,
                len(v) - 1)]
        smallest_paths = []
        for (s, e) in pairs:
            paths = self.find_all_paths(s, e)
            smallest = sorted(paths, key=len)[0]
            smallest_paths.append(smallest)

        smallest_paths.sort(key=len)

        # longest path is at the end of list,
        # i.e. diameter corresponds to the length of this path
        diameter = len(smallest_paths[-1]) - 1
        return diameter

    @staticmethod
    def erdoes_gallai(dsequence):
        """
        Check if Erdoes-Gallai inequality condition is fullfilled.
        """
        if sum(dsequence) % 2:
            # sum of sequence is odd
            return False
        if Graph.is_degree_sequence(dsequence):
            for k in range(1, len(dsequence) + 1):
                left = sum(dsequence[:k])
                right = k * (k - 1) + sum([min(x, k) for x in dsequence[k:]])
                if left > right:
                    return False
        else:
            # sequence is increasing
            return False
        return True

    # Code by Eryk Kopczyński
    def find_shortest_path(self, start, end):
        from collections import deque
        graph = self.__graph_dict
        dist = {start: [start]}
        q = deque((start,))
        while len(q):
            at = q.popleft()
            for next in graph[at]:
                if next not in dist:
                    # dist[next] = [dist[at], next]
                    # less efficient but nicer output
                    dist[next] = dist[at] + [next]
                    q.append(next)
        return dist.get(end)

    ##############
    def is_cyclic(self):
        """
        Returns true if the graph contains a cycle, else false.
        """
        # Mark all the vertices as not visited
        visited = [False] * len(self)
        # Call helper function to detect cycle in different DFS trees
        for i, v in enumerate(visited):
            # Don't recur for u if it is already visited
            if v == False:
                if self.dfs(i, visited, -1):
                    return True
        return False

    def dfs(self, v, visited, parent):
        # Mark the current node as visited
        visited[v] = True
        # Recur for all the vertices adjacent to this vertex
        for i in self.__graph_dict[v]:
            # If the node is not visited then recurse on it
            if visited[i] == False:
                if(self.dfs(i, visited, v)):
                    return True
            # If an adjacent vertex is visited and not parent of current
            # vertex, then there is a cycle
            elif parent != i:
                return True
        return False

    ##############

    def get_random_vertex(self):
        return choice(self.vertices())

    @staticmethod
    def empty_graph(names):
        vertices = set(names)
        graph = Graph()
        for v in vertices:
                graph.add_vertex(v) 
        return graph 

    @staticmethod
    def random_graph(names,
                     connect_rate=.9,
                     allow_loops=True,
                     allow_cyclic=False,
                     connected=False):
        vertices = set(names)
        while True:
            graph = Graph()
            for v in vertices:
                graph.add_vertex(v)
                if random(1) < connect_rate:
                    if allow_loops:
                        names = list(vertices)
                    else:
                        names = list(vertices - set((v,)))
                    graph.add_edge({v, choice(names)})
            if not connected or graph.is_connected():
                if allow_cyclic or not graph.is_cyclic():
                    break
        return graph
