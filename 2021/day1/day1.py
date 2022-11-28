#!/usr/bin/env python3

import utils

def solution(file, r=1):
    depths = utils.read_file_as_int_array(file)
    return sum([1 for i in range(r, len(depths), r) if depths[i] > depths[i-r]])


if __name__ == "__main__":
    one = solution('day1.txt')
    two = solution('day1.txt', 3)
    print(one)
    print(two)
