import csv
import doctest

from typing import Any


class FindNumber:
    """
    >>> array = FindNumber.from_csv("MOCK_DATA_sorted.csv")
    >>> FindNumber.from_list(array, "99996")
    999
    >>> array = FindNumber.from_csv("MOCK_DATA.csv")
    >>> FindNumber.from_list(array, "99996")
    972
    """
    #>>> FindNumber.from_sorted(array, "99996")
    #972
    #"""
    @staticmethod
    def from_csv(file: str) -> list:
        with open(file, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            contents = []
            line_count = 0
            for row in csv_reader:
                contents.extend(row)
                if line_count == 0:
                    line_count += 1
                line_count += 1
            return contents

    @staticmethod
    def from_list(array: list, element: Any) -> int:
        for i in range(len(array)):
            if array[i] == element:
                return i
        return -1

    @staticmethod
    def from_sorted(array: list, element: Any) -> int:
        n = int(len(array) / 2)
        print(f"First n: {n}")
        while array[n] != element:
            print(n)
            print(f"Array len: {len(array)}")
            if array[n] == element:
                break
            elif array[n] > element:
                array = array[:n]
            else:
                array = array[n:]
            if len(array) <= 2:
                n = 0
            else:
                n = int(len(array) / 2)
            print(n)
            print(f"Array len: {len(array)}")
        print(array)
        return n


#nums = FindNumber.from_csv("MOCK_DATA.csv")
#print(FindNumber.from_sorted(nums, "99996"))


doctest.run_docstring_examples(FindNumber, globals())

