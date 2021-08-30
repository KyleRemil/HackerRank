input_file = open(r"input.txt")

def raw_input():
    return input_file.readline()


def main():
    # if __name__ == '__main__':
    students = []
    second_lowests = []
    counter = 1

    name = raw_input()
    score = float(raw_input())
    students.append([name, score])
    if counter > 1:
        for counter in len(students):
                # if student[1] > students[counter + 1][1]:
            print(counter)

    counter +=1

main()