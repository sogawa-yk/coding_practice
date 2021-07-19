from typing import Union
from unionfind import UnionFInd

N, M = map(int, input().split())
idxs = list(range(M))
a, b = [], []
for _ in range(M):
    tmp_a, tmp_b = map(int, input().split())
    a.append(tmp_a)
    b.append(tmp_b)

cnt = 0    

for m in range(M):
    uf = UnionFInd(N)
    for idx, i, j in zip(idxs, a, b):
        if idx == m:
            continue
        uf.unite(i-1, j-1)
    if uf.group_count() != 1:
        cnt += 1
    
print(cnt)
