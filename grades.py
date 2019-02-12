# read in grades.txt
# print out a list of students
# and their avg grade for class
# and rank them in order
# from high to low
# i.e., bob 98, sue 97, sara 76


def avg():
    names = {}
    names_count = {}
    with open("grades.txt") as f:
        for row in f:
            name, grade = row.strip().split(' ')
            if name not in names:
                names[name] = float(grade)
                names_count[name] = 1
            else:
                names[name] += float(grade)
                names_count[name] += 1

        for i in names:
            names[i] = names[i] / names_count[i]
        sorting(names)


def sorting(names):
    for key, value in sorted(names.items(), key=lambda k: (k[1], k[0]), reverse=True):
        print(key, value)


avg()
