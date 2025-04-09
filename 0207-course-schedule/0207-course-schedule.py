from typing import List
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        WHITE = 1
        GRAY = 2
        BLACK = 3

        # Create the adjacency list
        adj_list = defaultdict(list)
        for course, pre in prerequisites:
            adj_list[pre].append(course)

        # Set all nodes to WHITE initially
        color = {i: WHITE for i in range(numCourses)}
        self.no_cycle = True

        def dfs(node):
            if not self.no_cycle:
                return

            color[node] = GRAY

            for neighbor in adj_list[node]:
                if color[neighbor] == WHITE:
                    dfs(neighbor)
                elif color[neighbor] == GRAY:
                    # Found a back edge → cycle
                    self.no_cycle = False

            color[node] = BLACK

        # Call DFS on each course
        for course in range(numCourses):
            if color[course] == WHITE:
                dfs(course)

        return self.no_cycle
