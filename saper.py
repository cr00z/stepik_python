# input [from 1 to ...]
# x y num_of_mines
# mine1_x mine1_y
# mine2_x mine2_y
# ...
rows, cols, mines_num = [int(i) for i in input().split()]
saper_field = [[0 for j in range(cols)] for i in range(rows)]
for m in range(mines_num):
    mine_r, mine_c = [int(m) for m in input().split()]
    mine_x, mine_y = mine_r - 1, mine_c - 1
    saper_field[mine_x][mine_y] = '*'
    for i in range(mine_x - 1, mine_x + 2):
        if i < 0 or i > rows - 1:
            continue
        for j in range(mine_y - 1, mine_y + 2):
            if j < 0 or j > cols - 1:
                continue
            if saper_field[i][j] == '*':
                continue
            saper_field[i][j] += 1
for i in range(rows):
    print(*saper_field[i])
