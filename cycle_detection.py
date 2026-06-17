# ノードは、未探索0・探索中1・探索済み2 の3状態を持つ
# 探索中の経路で、「探索中」の状態のノードに行き着いたら、それはサイクルになってる
# graphは隣接ノード、Nはノード数
# O(N + E)

def is_acyclic(graph, N):
    state = [0] * N
    
    for start in range(N):
        if state[start] != 0:
            continue
        
        searching = [(start, False)]
    
        while searching:
            cur_node, path_finished = searching.pop()
            
            if path_finished:
                state[cur_node] = 2
                continue

            state[cur_node] = 1
            searching.append((cur_node, True))
            
            for nxt_node in graph[cur_node]:
                if state[nxt_node] == 2:
                    continue
                elif state[nxt_node] == 1:
                    return False
                elif state[nxt_node] == 0:
                    searching.append((nxt_node, False))
            
    return True