arr = []
max_prod = 0
prod = 0

for i in range(20):
    arr.append(map(int, raw_input().split()))

# Horizontal 
for i in range(20):
    for j in range(17):
        prod = arr[i][j] * arr[i][j+1] * arr[i][j+2] * arr[i][j+3]
        if max_prod < prod:
            max_prod = prod
        prod = arr[j][i] * arr[j+1][i] * arr[j+2][i] * arr[j+3][i]
        if max_prod < prod:
            max_prod = prod

# Diagonals
for i in range(17):
    for j in range(17):
        prod = arr[i][j] * arr[i+1][j+1] * arr[i+2][j+2] * arr[i+3][j+3]
        if max_prod < prod:
            max_prod = prod
        prod = arr[i][j+3] * arr[i+1][j+2] * arr[i+2][j+1] * arr[i+3][j]
        if max_prod < prod:
            max_prod = prod
print max_prod                   
