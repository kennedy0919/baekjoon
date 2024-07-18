# import sys
# sys.stdin = open("input.txt", "r")

[0, 1, 1, 0, 1, 0, 0]
[0, 1, 1, 0, 1, 0, 1]
[1, 1, 1, 0, 1, 0, 1]
[0, 0, 0, 0, 1, 1, 1]
[0, 1, 0, 0, 0, 0, 0]
[0, 1, 1, 1, 1, 1, 0]
[0, 1, 1, 1, 0, 0, 0]

def dfs(r, c):
    global cnt
    arr[r][c] = 0
    for d in range(0, 4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 1:
            arr[nr][nc] = 0
            cnt = cnt + 1
            dfs(nr, nc)
            
            


N = int(input())

arr_o = [list(map(str, input().split())) for _ in range(0, N)]
arr = []
ans = []
cnt_vill = 0
# visited = [[0] * (N) for _ in range(0, N)]


for row in arr_o:
    arr_1 = []
    for char in row[0]:
        num = int(char)
        arr_1.append(num)
    arr.append(arr_1)


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for i in range(0, N):
    for j in range(0, N):
        if arr[i][j] == 1:
            cnt = 1
            cnt_vill = cnt_vill + 1
            dfs(i, j)
            ans.append(cnt)

ans.sort()

print(cnt_vill)
for answer in ans:
    print(answer)