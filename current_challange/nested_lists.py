input_file = open(r"input.txt")

def raw_input():
    return input_file.readline()


def create_raw_input_list():
    # if __name__ == '__main__':
    students = []
    second_lowests = []
    counter = 0

    name = raw_input()
    score = float(raw_input())
    students.append([name, score])
    if counter > 1:
        for student in students:
            for counter in len(students):
                if student[1] > students[counter + 1][1]:

    counter +=1




create_raw_input_list()