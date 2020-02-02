import random as rand
from abc import ABC, abstractmethod
from GraphGenerator import GraphGenerator


class Search(ABC):
    
    def three_color(self, g):
        pass

    def four_color(self, g):
        pass


class Backtracking(Search):
    
    def __init__(self, graph):
        self.g = graph

    #calls dfs with 3 colors
    def three_color(self, g):
        return super().three_color(g)

    #calls dfs with 4 colors
    def four_color(self, g):
        colors = [0] * g.size
        colors = dfs(rand.randint(0,g.size), null, colors, 4)
        return colors
    
    #backtracking search to find coloring
    def dfs(self, start, prev, colors, k):
        col = 1

        #assigns color to vertex after checking for conflicts
        while(col <= k):
            works = True

            #checks adjacent nodes for matching color
            for i in range(g.size):
                if g[start][i] == 1:
                    if colors[i] == col:
                        works = False
                        break
            
            if works == True:
                colors[start] = col

                for i in range(g.size):
                    if g[start][i] == 1 and i != prev:
                        colors = self.dfs(i, start, colors, k)

            if prev == null:
                return colors

            col += 1

        return colors

