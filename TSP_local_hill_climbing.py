#
# SimpleAI Traveling Salesman Problem
# Author: Aaron Hung
# Date: 5/05/15
# Purpose: Traveling Salesman Problem solution using SimpleAI's framework for state space search using Hill Climbing algorithm.
# 

from simpleai.search import SearchProblem, hill_climbing_random_restarts
from simpleai.search.viewers import ConsoleViewer
import random

class TspProblem(SearchProblem):
    def __init__(self, cities, distances):
        '''Traveling Salesman Problem Class Constructor'''
        self.numCities = cities
        self.cityDistances = distances
        self.tour = [1,2,3,4,5,6,7,8,9,10,11]
        super(TspProblem, self).__init__(initial_state=[[0] + random.sample(self.tour, len(self.tour)) + [0]])
        
    def actions(self, s):
        '''Return action list with action description[0] and resulting tour[1]'''
        actions = []
        
        x = random.randint(1, self.numCities-1)
        y = random.randint(1, self.numCities-1)
        
        # Choose 2 random points until valid for reversing tour edge
        while x == y or y == min(x, y):
            x = random.randint(1, self.numCities-1)
            y = random.randint(1, self.numCities-1)
        
        # Reverse edge
        s[0] = s[0][0:x+1] + list(reversed(s[0][x+1:y])) + s[0][y:]
        
        actions.append(('2-change at ' + str(x) + ' and ' + str(y), s))
        
        return actions

    def result(self, s ,a):
        '''Return resulting tour from action'''
        return a[1]
        
    def value(self, s):
        '''Return the length of the tour'''
        return self.__tour_length(s)
        
    def generate_random_state(self):
        '''Return a random generated tour'''
        return [[0] + random.sample(self.tour, len(self.tour))+ [0]]

    def __tour_length(self, s):
        '''Return length of state or total distance of tour'''
        total_dist = 0
        
        for i in range (0, self.numCities - 2):
            current_city = s[0][i]
            next_city = s[0][i + 1]
            current_dist = self.cityDistances[current_city][next_city]
            total_dist += current_dist
        
        # Add in distance for returning trip to origin of tour
        total_dist += self.cityDistances[s[0][self.numCities - 1]][s[0][0]]
        
        return total_dist



problem = TspProblem(12, [[0, 5, 7, 6, 8, 1, 3, 9, 14, 3, 2, 9], \
                          [5, 0, 6, 10, 4, 3, 12,14, 9, 1, 2, 7], \
                          [7, 6, 0, 2, 3, 4, 11, 13, 4, 8, 10, 5], \
                          [6, 10, 2, 0, 5, 7, 9, 11, 13, 5, 3, 1], \
                          [8, 4, 3, 5, 0, 9, 11, 14, 5, 8, 3, 8], \
                          [1, 3, 4, 7, 9, 0, 5, 6, 14, 18, 4, 7], \
                          [3, 12, 11, 9, 11, 5, 0, 19, 4, 3, 5, 6], \
                          [9, 14, 13, 11, 14, 6, 19, 0, 1, 4, 5, 7], \
                          [14, 9, 4, 13, 5, 14, 4, 1, 0, 8, 3, 1], \
                          [3, 1, 8, 5, 8, 18, 3, 4, 8, 0, 4, 5], \
                          [2, 2, 10, 3, 3, 4, 5, 5, 3, 4, 0, 1], \
                          [9, 7, 5, 1, 8, 7, 6, 7, 1, 5, 1, 0]])

#vw = ConsoleViewer()

#result = hill_climbing_random_restarts(problem, restarts_limit=200, viewer=vw)
result = hill_climbing_random_restarts(problem, restarts_limit=200)

print result
