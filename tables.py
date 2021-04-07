out = {}

def insert_tbl(cmd, result):
    row = out.setdefault(cmd, [0] * 5)
    out[cmd] = [row[i] + result[i] for i in range(len(result))]

num = int(input())
for i in range(num):
    cmd1, goals1, cmd2, goals2 = input().split(';')
    if int(goals1) > int(goals2):
        insert_tbl(cmd1, [1, 1, 0, 0, 3])
        insert_tbl(cmd2, [1, 0, 0, 1, 0])
    elif int(goals1) < int(goals2):
        insert_tbl(cmd1, [1, 0, 0, 1, 0])
        insert_tbl(cmd2, [1, 1, 0, 0, 3])
    else:
        insert_tbl(cmd1, [1, 0, 1, 0, 1])
        insert_tbl(cmd2, [1, 0, 1, 0, 1])

for key, value in out.items():
    print(key+':', ' '.join([str(i) for i in value]), sep='')