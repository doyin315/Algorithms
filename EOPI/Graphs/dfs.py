graph ={'A': set(['B','C']),
        'B': set(['A','D','E']),
        'C': set(['A','F']),
        'D': set(['B']),
        'E': set(['B','F']),
        'F': set(['C','E'])}
visited=set()

def dfs(visited,graph,vertex):
    if vertex not in visited:
        print(vertex,visited)
        visited.add(vertex)
        for v in graph[vertex]:
            dfs(visited,graph,v)

dfs(visited,graph,'A')
test1=[[1,0 ,1, 1, 0],[1 ,1, 0, 0, 1],[0, 1, 1, 1, 0],[0, 0, 0, 0, 1],[1, 1, 1, 0, 0]]