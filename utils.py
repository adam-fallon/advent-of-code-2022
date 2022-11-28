#!/usr/bin/env python3

# Files
def read_file(file):
    f = open(file, "r")
    data = f.read()
    f.close()
    return data

def read_file_as_str_array(file):
    with open(file, 'r') as open_file:
        return [str(line.strip()) for line in open_file.readlines()]


def read_file_as_int_array(file):
    with open(file, 'r') as open_file:
        return [int(number.strip()) for number in open_file.readlines()]

def chunked(arr, chunk_size):
    for i in range(0, len(arr), chunk_size):
        yield arr[i:i + chunk_size]

def convert_string_array_to_int_array(str_array):
    return list(map(int, str_array))

# Math
def round_num(decimal, places):
    return round(decimal, places)
