import sys
sys.path.append('../')
import utils

def solution(file):
    data = utils.read_file(file)
    return data

if __name__ == "__main__":
        one = solution("day1.txt")
        two = solution("day1.txt")
        print(one)
        print(two)
