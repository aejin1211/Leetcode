import collections
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)

        for x, y in prerequisites:
            graph[x].append(y)

        traced = set()   # 현재 탐색 중인 경로
        visited = set()  # 이미 탐색 완료된 노드
        
        def dfs(i):
            if i in traced:     # 현재 경로에 다시 등장 → 사이클
                return False
            if i in visited:    # 이미 탐색 완료된 노드 → 바로 True
                return True

            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            traced.remove(i)
            visited.add(i)      # 탐색 완료 기록

            return True

        for x in range(numCourses):  # 모든 노드 확인해야 함
            if not dfs(x):
                return False
        return True

