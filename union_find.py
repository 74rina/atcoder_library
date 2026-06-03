class UnionFind():
    def __init__(self, n):
        self.parent = [-1] * n
    
    # x, y のノードを連結する
    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        
        if rx == ry:
            return False
        
        if self.parent[rx] > self.parent[ry]:
            rx, ry = ry, rx
        
        self.parent[rx] += self.parent[ry]
        self.parent[ry] = rx
        
        return True
        
        
    # x の根を返す
    def find(self, x):
        while self.parent[x] >= 0:
            x = self.parent[x]
        return x
    
    
    # x, y が同一集合か調べる
    def is_same(self, x, y):
        return self.find(x) == self.find(y)
    
    
    # x の属する集合のサイズ
    def size(self, x):
        return -self.parent[self.find(x)]
