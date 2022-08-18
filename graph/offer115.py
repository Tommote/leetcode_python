from typing import List


class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:

        graph = dict() 

        for seq in seqs:
            for ch in seq :
                if ch not in graph:
                    graph[ch] = []
        

        if len(org) != len(graph):
            return False 
        
        in_number = [0]*len(graph)

        for seq in seqs :

            for i in range( 1 , len(seq)):
                pass 
