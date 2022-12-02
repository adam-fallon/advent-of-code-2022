import sys
sys.path.append('./')
import utils

strategy_1 = {
    'A X': 1 + 3,
    'A Y': 2 + 6,
    'A Z': 3 + 0,
    'B X': 1 + 0,
    'B Y': 2 + 3,
    'B Z': 3 + 6,
    'C X': 1 + 6,
    'C Y': 2 + 0,
    'C Z': 3 + 3,
}

strategy_2 = {
    'A X': 3 + 0,
    'A Y': 1 + 3,
    'A Z': 2 + 6,
    'B X': 1 + 0,
    'B Y': 2 + 3,
    'B Z': 3 + 6,
    'C X': 2 + 0,
    'C Y': 3 + 3,
    'C Z': 1 + 6,
}

def main(data: list, strategy: dict) -> int:
    sum = 0
    for round in data:
        sum += strategy[round]
    return sum

if __name__ == "__main__":
    print(main(utils.read_file_as_str_array("./day2/day2.txt"), strategy_1))
    print(main(utils.read_file_as_str_array("./day2/day2.txt"), strategy_2))
