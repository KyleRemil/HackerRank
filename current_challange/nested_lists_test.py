import functools
import nested_lists as nl

input_file = open(r"input.txt")

assert functools.reduce(lambda a, b: a and b, map(lambda x, y: x == y, nl.raw_input_list, input_file.readlines()))
