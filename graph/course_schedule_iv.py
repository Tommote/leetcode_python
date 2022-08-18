from typing import List


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        N = numCourses

        self.dp_arr = [[0]*N for _ in range(N)] 

        