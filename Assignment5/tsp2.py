
'''
In this assignment you will implement one or more algorithms for the traveling salesman problem, such as the dynamic programming algorithm covered in the video lectures. Here is a data file describing a TSP instance.

tsp.txt
The first line indicates the number of cities. Each city is a point in the plane, and each subsequent line indicates the x- and y-coordinates of a single city.

The distance between two cities is defined as the Euclidean distance --- that is, two cities at locations (x,y) and (z,w) have distance .... between them.

In the box below, type in the minimum cost of a traveling salesman tour for this instance, rounded down to the nearest integer.

OPTIONAL: If you want bigger data sets to play with, check out the TSP instances from around the world here. The smallest data set (Western Sahara) has 29 cities, and most of the data sets are much bigger than that. What's the largest of these data sets that you're able to solve --- using dynamic programming or, if you like, a completely different method?

HINT: You might experiment with ways to reduce the data set size. For example, trying plotting the points. Can you infer any structure of the optimal solution? Can you use that structure to speed up your algorithm?
'''


import numpy as np
import random


# Cities are represented as Points, which are represented as complex numbers
Point = complex
City = Point


def X(point):
    "The x coordinate of a point."
    return point.real


def Y(point):
    "The y coordinate of a point."
    return point.imag


def distance(A, B):
    "The distance between two points."
    return abs(A - B)


def read_cities(fname):
    cities_mat = np.loadtxt(fname, skiprows=1)
    return frozenset(np.apply_along_axis(lambda x: City(x[0], x[1]),
                                         axis=1, arr=cities_mat))


def sample(population, k, seed=42):
    "Return a list of k elements sampled from population. Set random.seed with seed."
    if k is None or k > len(population):
        return population
    random.seed(len(population) * k * seed)
    return random.sample(population, k)


def tour_length(tour):
    '''
    A tour is a list of cities. This function returns the total length of the tour.
    '''
    return sum(distance(tour[i], tour[i - 1])
               for i in range(len(tour)))


def shortest_tour(tours):
    "Choose the tour with the minimum tour length."
    return min(tours, key=tour_length)


def nearest_neighbor(A, cities):
    "Find the city in cities that is nearest to city A."
    return min(cities, key=lambda c: distance(c, A))


def reverse_segment_if_better(tour, i, j):
    "If reversing tour[i:j] would make the tour shorter, then do it."
    # Given tour [...A-B...C-D...], consider reversing B...C to get
    # [...A-C...B-D...]
    A, B, C, D = tour[i - 1], tour[i], tour[j - 1], tour[j % len(tour)]
    # Are old edges (AB + CD) longer than new ones (AC + BD)? If so, reverse
    # segment.
    if distance(A, B) + distance(C, D) > distance(A, C) + distance(B, D):
        tour[i:j] = reversed(tour[i:j])


def alter_tour(tour):
    "Try to alter tour for the better by reversing segments."
    original_length = tour_length(tour)
    for (start, end) in all_segments(len(tour)):
        reverse_segment_if_better(tour, start, end)
    # If we made an improvement, then try again; else stop and return tour.
    if tour_length(tour) < original_length:
        return alter_tour(tour)
    return tour


def all_segments(N):
    "Return (start, end) pairs of indexes that form segments of tour of length N."
    return [(start, start + length)
            for length in range(N, 2 - 1, -1)
            for start in range(N - length + 1)]


def nn_tsp(cities, start=None):
    """Start the tour at the first city; at each step extend the tour 
    by moving from the previous city to its nearest neighbor 
    that has not yet been visited."""
    if (start == None):
        start = iter(cities).next()
    tour = [start]
    unvisited = set(cities - {start})
    while unvisited:
        C = nearest_neighbor(tour[-1], unvisited)
        tour.append(C)
        unvisited.remove(C)
    return tour


def altered_nn_tsp(cities):
    "Run nearest neighbor TSP algorithm, and alter the results by reversing segments."
    return alter_tour(nn_tsp(cities))


def repeated_altered_nn_tsp(cities, repetitions=20):
    "Use alteration to improve each repetition of nearest neighbors."
    return shortest_tour(alter_tour(nn_tsp(cities, start))
                         for start in sample(cities, repetitions))


def main():
    fname = "tsp.txt"
    cities = read_cities(fname)
    print cities


if __name__ == "__main__":
    main()
