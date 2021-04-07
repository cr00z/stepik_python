with open('dataset_3363_3.txt') as inf:
    lines = [line.strip().lower() for line in inf]
wdict = dict()
for line in lines:
    words = line.split(' ')
    for word in words:
        wdict[word] = wdict.get(word, 0) + 1
sdict = sorted(wdict.items(), key=lambda x: (-x[1], x[0]))
print(sdict[0][0], sdict[0][1])


# with open('out.txt', 'w') as ouf:
#     ouf.write(out)

