from collections import defaultdict
import queue
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:

        graph , in_number = defaultdict(), defaultdict()


        for word in words:
            for ch in word:
                if ch not in in_number:
                    in_number[ch] = 0

        for i in range(1, len(words)):

            s1 , s2 = words[i-1], words[i]

            if s1==s2:
                continue

            curr = 0
            while curr<len(s1) and curr<len(s2) and s1[curr]==s2[curr] :
                curr += 1
            
            if curr==len(s1):
                continue 
            elif curr==len(s2):
                return ''
            else:
                if s1[curr] in graph:
                    graph[s1[curr]].append(s2[curr])
                else:
                    graph[s1[curr]] = [s2[curr]]
                # graph.get(s1[curr], list()).append( s2[curr])
                # if s2[curr] in in_number:
                in_number[s2[curr]] += 1
                # else:
                #     in_number[s2[curr]] = 1

                # if s1[curr] not in in_number:
                #     in_number[s1[curr]] = 0

        ret = ''
        queue_node = queue.Queue()        
        print(graph, in_number)
        for key in in_number.keys() :
            if in_number[key] == 0 :
                queue_node.put(key)
        
        while not queue_node.empty():

            ch = queue_node.get()

            ret += ch 

            if ch not in graph:
                in_number.pop(ch)
                continue

            for ch_i in graph[ch]:

                in_number[ch_i] -= 1
                if in_number[ch_i]==0:
                    queue_node.put(ch_i)
            in_number.pop(ch)

        return ret if len(in_number)==0 else ''
                
            
            
s = Solution()
print(s.alienOrder(words = ["wrt","wrf","er","ett","rftt"]))