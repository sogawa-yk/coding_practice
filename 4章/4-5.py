N = int(input())
global cnt 

def func(N, cur, use):
    
    global cnt
    if cur > N:
        return
    if use == 0b111:
        cnt += 1
        
    func(N, cur*10+7, use|0b100)
    func(N, cur*10+5, use|0b010)
    func(N, cur*10+3, use|0b001)

cnt = 0
func(N, 0, 0)
print(cnt)