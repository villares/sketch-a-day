#*- coding: utf-8 -*-

"""
A simple Python graph class, demonstrating the essential facts and functionalities of graphs
based on https://www.python-course.eu/graphs_python.php and https://www.python.org/doc/essays/graphs/
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
    
    def __getitem__(self, i):
        return self.__graph_dict[i]

    def vertices(self):
        """Return the vertices of graph."""
        return list(self.__graph_dict.keys())

    def edges(self):
        """Return the edges of graph """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """
        If the vertex "vertex" is not in self.__graph_dict,
        add key "vertex" with an empty list as a value,
        otherwise, do nothing.
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        """
        Assuming that edge is of type set, tuple or list;
        add edge between vertices. Can add multiple edges!
        """
        edge = set(edge)
        vertex1 = edge.pop()
        if edge:
            # not a loop
            vertex2 = edge.pop()
            if vertex1 in self.__graph_dict:
                self.__graph_dict[vertex1].append(vertex2)
            else:
                self.__graph_dict[vertex1] = [vertex2]
            if vertex2 in self.__graph_dict:
                self.__graph_dict[vertex2].append(vertex1)
            else:
                self.__graph_dict[vertex2] = [vertex1]
        else:
            # a loop
            if vertex1 in self.__graph_dict:
                self.__graph_dict[vertex1].append(vertex1)
            else:
                self.__graph_dict[vertex1] = [vertex1]        


    def remove_vertex(self, vert):
        raise NotImplemented
      
    def remove_edge(self, vert):
        raise NotImplemented
    
    def __generate_edges(self):
        """
        Generate the edges, represented as sets with one
        (a loop back to the vertex) or two vertices.
        """
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
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
        for vertex in graph:
            print(isolated, vertex)
            if not graph[vertex]:
                isolated += [vertex]
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
            return None
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(vertex,
                                               end_vertex,
                                               path)
                if extended_path:
                    return extended_path
        return None

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
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_paths = self.find_all_paths(vertex,
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
            for vertex in gdict[start_vertex]:
                if vertex not in vertices_encountered:
                    if self.is_connected(vertices_encountered, vertex):
                        return True
        else:
            return True
        return False

    def vertex_degree(self, vertex):
        """
        Return the number of edges connecting to a vertex (the number of adjacent vertices).
        Loops are counted double, i.e. every occurence of vertex in the list of adjacent vertices.
        """
        adj_vertices = self.__graph_dict[vertex]
        degree = len(adj_vertices) + adj_vertices.count(vertex)
        return degree

    def degree_sequence(self):
        """Calculates the degree sequence."""
        seq = []
        for vertex in self.__graph_dict:
            seq.append(self.vertex_degree(vertex))
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
        min = 100000000
        for vertex in self.__graph_dict:
            vertex_degree = self.vertex_degree(vertex)
            if vertex_degree < min:
                min = vertex_degree
        return min

    def Delta(self):
        """Finde maximum degree of vertices."""
        max = 0
        for vertex in self.__graph_dict:
            vertex_degree = self.vertex_degree(vertex)
            if vertex_degree > max:
                max = vertex_degree
        return max

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
        q = deque(start)
        while len(q):
            at = q.popleft()
            for next in graph[at]:
                if next not in dist:
                    #dist[next] = [dist[at], next] 
                    dist[next] = dist[at]+[next]   # less efficient but nicer output
                    q.append(next)
        return dist.get(end)
    
    
    def get_random_vertex(self):
        return choice(self.vertices())
    
    @staticmethod            
    def random_graph(names, connect_rate=.9, allow_loops=True):
        vertices = set(names)
        graph = Graph()
        for v in vertices:
            graph.add_vertex(v)
            if random(1) < connect_rate:
                if allow_loops:
                    pool = list(vertices)
                else:
                    pool = list(vertices - set((v,)))
                graph.add_edge({v, choice(pool)})    
        return graph
