with open('dataset_3363_4.txt') as inf, open('out.txt','w') as ouf:
    students = [line.strip().lower().split(';') for line in inf]
    mathem, phys, rus = 0, 0, 0
    for student in students:
        ouf.write(str((int(student[1]) + int(student[2]) + int(student[3])) / 3) + '\n')
        mathem += int(student[1])
        phys += int(student[2])
        rus += int(student[3])
    ouf.write(str(mathem / len(students)) + ' ' + str(phys / len(students)) + ' ' + str(rus / len(students)))
# with open('out.txt', 'w') as ouf:
#     ouf.write(out)

