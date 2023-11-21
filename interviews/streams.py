"""
Write a function that takes n (sorted) streams as input and outputs a sorted stream.

Each sorted stream consists of positive integers.
Streams can be bounded (terminated) or unbounded (nonterminating).
"""
import random
from typing import Generator, List, Optional

def merge_sorted_lists(output_stream: List[int], input_streams: List[List[int]]) -> None:
    """
    Note: This is not answering the question...
    but this is a solid starting place because it answers a similar question.
    """
    assert len(input_streams) > 1

    for i in input_streams:
        output_stream[:] = merge_two_lists(output_stream, i)


def merge_two_lists(a: List[int], b: List[int]) -> List[int]:
    """
    The merge step for merge sort.
    """
    a_index = 0
    b_index = 0

    result = []
    while a_index < len(a) and b_index < len(b):
        if a[a_index] < b[b_index]:
            result.append(a[a_index])
            a_index = a_index + 1
        else:
            result.append(b[b_index])
            b_index = b_index + 1
    
    if a_index < len(a):
        result = result + a[a_index:]
    
    if b_index < len(b):
        result = result + b[b_index:]
    
    return result


def even_numbers() -> Generator[int, None, None]:
    even_num = 0
    while True:
        yield even_num
        even_num = even_num + 2


def odd_numbers() -> Generator[int, None, None]:
    odd_num = 1
    while True:
        yield odd_num
        odd_num = odd_num + 2


def random_numbers(last_num: int) -> Generator[int, None, str]:
    """
    A generator that creates random numbers up until a range. Once that's hit, it returns.
    """
    rand = 0
    while True:
        yield rand
        rand = rand + random.randint(0, 5)
        if rand > last_num:
            break
    return "FINISHED"


def generate_sorted_stream(start: int, step: int) -> Generator[int, None, None]:
    """
    Just to really drive home that I know really know how to create these streams...
    """
    value = start
    while True:
        yield value
        value += step


def merge_sorted_streams(input_streams: List[Generator[int, None, Optional[str]]]) -> Generator[int, None, None]:
    values = []
    for gen in input_streams:
        values.append(next(gen))

    while True:
        next_smallest_value = values[0]
        index = 0

        for i, value in enumerate(values):
            if value < next_smallest_value:
                next_smallest_value = value
                index = i

        try:
            values[index] = next(input_streams[index])
        except StopIteration:
            values.pop(index)
            input_streams.pop(index)

        yield next_smallest_value


stream1 = generate_sorted_stream(2, 3)  # 2, 5, 8, 11, 14...
stream2 = generate_sorted_stream(3, 4)  # 3, 7, 11, 15, 19...
streamr = random_numbers(8)            # ??????????????????
stream3 = odd_numbers()                 # 1, 3, 5, 7, 9, 11...
stream4 = random_numbers(15)            # ??????????????????


a = merge_sorted_streams([stream1, stream2, streamr, stream3, stream4])
for i in range(25):
    print(next(a))
