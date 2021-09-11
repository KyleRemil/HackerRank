input_file = open(r"input.txt")

def raw_input():
    return input_file.readline()

if __name__ == '__main__':
    students = []
    second_lowests = []
    lowest = None

    for _ in range(int(raw_input())):

        name = raw_input()
        score = float(raw_input())
        students.append([name, score])
        if students > 1:
            lowest = None
            second_lowest = None
            for student in students: