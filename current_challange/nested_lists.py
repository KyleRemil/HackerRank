raw_input_list = []
input_file = open(r"input.txt")


def raw_input():
    return input_file.readline()


def create_raw_input_list():
    # if __name__ == '__main__':
    for _ in range(int(raw_input())):
        student_name_and_score = []
        name = raw_input()
        score = float(raw_input())
        student_name_and_score.append(name)
        student_name_and_score.append(score)
        raw_input_list.append(student_name_and_score)