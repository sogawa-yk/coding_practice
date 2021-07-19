import sys

class UnionFInd():
    
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        self.size = [1] * n
        
    def root(self, x):
        # 根をたどる
        if self.parents[x] == -1: return x
        else: return self.root(self.parents[x])
        
    def issame(self, x, y):
        # xとyが同じグループかどうか
        return self.root(x) == self.root(y)
    
    def unite(self, x, y):
        # xを含むグループとyを含むグループを併合する
        x, y = self.root(x), self.root(y)
        
        if x == y: return False # すでに同じグループのときは何もしない
        
        if self.size[y] > self.size[x]: # yの集合のほうがxの集合より大きいとき
            x, y = y, x # swapする (y側のサイズが小さくなるようにする)

        self.parents[y] = x # yをxに結合
        self.size[x] += self.size[y]
        
        return True
    
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]
    
    def group_count(self):
        return len(self.roots())
    
sys.setrecursionlimit(100000)

N, M = map(int, input().split())
A, B, idxs = [], [], list(range(M))

for _ in range(M):
    tmp1, tmp2 = map(int, input().split())
    A.append(tmp1)
    B.append(tmp2)
results = [0 for _ in range(M+1)]
results[0] = N * (N-1) // 2
uf = UnionFInd(N)
i = 1
for a, b in zip(reversed(A), reversed(B)):
    if uf.issame(a-1, b-1): 
        result = results[i-1]
        results[i] = result
        i += 1
    else:
        diff = uf.size[uf.root(a-1)] * uf.size[uf.root(b-1)]
        result = results[i-1] - diff
        results[i] = result
        uf.unite(a-1, b-1)
        i += 1
        
for i in reversed(results[:-1]):
    print(i)
    