import random
import numpy as np


class Graph:


    def __init__(self, adj_matrix):
        self.adj_matrix = adj_matrix
        self.already_seen = []

    def has_eulerian_tour(self):

        for row in self.adj_matrix:
            count = 0
            for i in row:
                if i == 1:
                    count += 1
            if count % 2 != 0: #graph does not have vertices of even degree
                return False
            elif count == 0: #graph is not connected
                return False

        return True


    def add_edge(self, v1, v2):
        self.adj_matrix[v1][v2] = 1
        self.adj_matrix[v2][v1] = 1

    def rm_edge(self, v1, v2):
        self.adj_matrix[v1][v2] = 0
        self.adj_matrix[v2][v1] = 0

    def one_indices(self, vertex):
        result = []
        for i in range(len(self.adj_matrix[vertex])):
            if self.adj_matrix[vertex][i] == 1 and (vertex, i) not in self.already_seen:
                result.append(i)
        return result

    def random_one(self, vertex):
        ones = self.one_indices(vertex)
        if not ones:
            return ones
        return random.choice(ones)

    def reset_alreadyseen(self):
        self.already_seen = []

    def reset(self):
        for pair in self.already_seen:
            self.add_edge(pair[0], pair[1])
        self.reset_alreadyseen()

    def find_tour(self, vertex):
        result = []
        curr_vertex = vertex
        rand_idx = self.random_one(curr_vertex) #random index of a one in this vertex's row in adj_matrix that isn't in already_seen
        while rand_idx != []:
            result.append((curr_vertex, rand_idx))
            self.already_seen.append((curr_vertex, rand_idx))
            self.already_seen.append((rand_idx, curr_vertex))
            self.rm_edge(curr_vertex, rand_idx)
            curr_vertex = rand_idx
            rand_idx = self.random_one(curr_vertex)
        return result

    def is_lone_vertex(self, vertex):
        for k in self.adj_matrix[vertex]:
            if k != 0:
                return False
        return True



    def splice(self, tour1, tour2):
        node_to_splice = tour2[0][0]
        k = 0
        curr_vertex = tour1[k][0]
        while curr_vertex != node_to_splice:
            k+=1
            curr_vertex = tour1[k][0]

        for item in tour2[::-1]:
            tour1.insert(k, item)

        return tour1



    def euler(self, vertex):

        tour1 = self.find_tour(vertex)
        copy = tour1.copy()

        for edge in copy:

            if not self.is_lone_vertex(edge[1]):
                tour2 = self.euler(edge[1])
                tour1 = self.splice(tour1, tour2)


        return tour1

    def find_euler_tour(self, vertex):
        assert self.has_eulerian_tour(), "Graph must be connected and every vertex must have even degree"
        tour = self.euler(vertex)
        self.reset()
        return tour

    def is_planar(self):
        return



g = Graph([[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]])

big_g = np.eye(51)
big_g[big_g == 0] = 1
for i in range(len(big_g)):
    big_g[i][i] = 0
big_g = Graph(big_g)

fat_g = np.eye(101)
fat_g[fat_g == 0] = 1
for i in range(len(fat_g)):
    fat_g[i][i] = 0
fat_g = Graph(fat_g)

def sum_fact(n):
    total = 0
    while n > 0:
        total += n
        n -= 1
    return total


