import sys
sys.path.append('./')
import utils

def solution(file):
    data = utils.read_file_as_str_array(file)
    d = {}
    sum = 0
    idx = 1

    for v in data:
        if v == "":
            d[idx] = sum
            idx += 1
            sum = 0
        else:
            sum += int(v)
    
    d = dict(sorted(d.items(), key=lambda x:x[1], reverse=True))
    return list(d.values())[:3]

if __name__ == "__main__":
    one = solution("./day2/day2.txt")
    two = solution("./day2/day2.txt")
    print(max(one))
    print(sum(two))
