YEAR = 2017
MONTH = 12
URL = f'https://adventofcode.com/{YEAR}'
USER_AGENT = f'email:sfmalloy.dev@gmail.com repo:https://github.com/sfmalloy/advent-of-code-{YEAR}'

def solution_template(day_number: int) -> str:
    return f'''from lib import advent
from io import TextIOWrapper
from collections import deque, defaultdict


@advent.parser({day_number})
def parse(file: TextIOWrapper):
    return [line.strip() for line in file.readlines()]


@advent.solver({day_number}, part=1)
def solve1(ipt):
    return 0


@advent.solver({day_number}, part=2)
def solve2(ipt):
    return 0
'''
