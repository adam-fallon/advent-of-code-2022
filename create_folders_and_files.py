#!/usr/bin/env python3

import os

if __name__ == "__main__":
    for day in range(1,26):
        folder = f"day{day}"
        cwd = os.getcwd()

        print(f"mkdir {cwd}/{folder}")
        os.makedirs(f"{cwd}/{folder}", exist_ok=True)

        print(f"touch {cwd}/{folder}/day{day}.py")
        os.close(os.open(f"{cwd}/{folder}/day{day}.py", os.O_CREAT))

        print(f"touch {cwd}/{folder}/day{day}.txt")
        os.close(os.open(f"{cwd}/{folder}/day{day}.txt", os.O_CREAT))
