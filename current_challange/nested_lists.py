students = []
input_file = open(r"input.txt")


def raw_input():
    return input_file.readline()


def create_raw_input_list():
    # if __name__ == '__main__':
    second_lowest = []
    for _ in range(int(raw_input())):
        student_name_and_score = []
        name = raw_input()
        score = float(raw_input())
        student_name_and_score.append(name)
        student_name_and_score.append(score)
        students.append(student_name_and_score)
        if len(students > 1):
            for student in students:

create_raw_input_list()