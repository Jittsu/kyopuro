# WA
N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))
T_min_idx = T.index(min(T))
update_T = T[T_min_idx:] + T[:T_min_idx]
update_S = S[T_min_idx:] + T[:T_min_idx]
for i in range(N):
    update_T[(i+1)%N] = min(update_T[(i+1)%N], update_T[i%N] + update_S[i%N])
if T_min_idx == 0:
    return_T = update_T
else:
    return_T = update_T[-(T_min_idx):] + update_T[:len(T)-(T_min_idx)]
for ans in return_T:
    print(ans)