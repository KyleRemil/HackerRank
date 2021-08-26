import functools
import nested_lists as nl

input_file = open(r"input.txt")
input_list = input_file.readlines()



def test_raw_input_list():
    nl.raw_input_list
    # raw_input_list = []
    # for _ in range(int(nl.raw_input())):
    #     # temp_input_list = []
    #     name = nl.raw_input()
    #     raw_input_list.append(name)
    #     score = float(nl.raw_input())
    #     raw_input_list.append(score)
    # print(functools.reduce(lambda a, b: a and b, map(lambda x, y: x == y, raw_input_list, input_list)))


test_raw_input_list()