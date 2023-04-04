"""
## Question

In a university, your attendance determines whether you will be
allowed to attend your graduation ceremony.
You are not allowed to miss classes for four or more consecutive days.
Your graduation ceremony is on the last day of the academic year,
which is the Nth day.

Your task is to determine the following:

1. The number of ways to attend classes over N days.
2. The probability that you will miss your graduation ceremony.

Represent the solution in the string format as "Answer of (2) / Answer
of (1)", don't actually divide or reduce the fraction to decimal

Test cases:

for 5 days: 14/29

for 10 days: 372/773
"""

import sys


class Solution:
    def __init__(self, days):
        self.days = days
        self.ways_to_attend_class = self.get_ways_to_attend_class()
        self.invalid_ways_to_attend_class = self.get_invalid_ways_to_attend_class()

    def get_ways_to_attend_class(self):
        result = []
        stack = ["P", "A"]

        while stack:
            node = stack.pop()

            for i in ["A", "P"]:
                new_node = node + i

                if len(new_node) < self.days:
                    stack.append(new_node)
                else:
                    result.append(new_node)

        return result

    def get_invalid_ways_to_attend_class(self):
        result = []

        for w in self.ways_to_attend_class:
            if 'AAAA' in w:
                result.append(w)

        return result

    def num_of_valid_ways_to_attend_class(self):
        return len(self.ways_to_attend_class) - len(self.invalid_ways_to_attend_class)

    def num_of_ways_student_can_miss_ceremony(self):
        ans = 0

        for w in self.ways_to_attend_class:
            if w.endswith("A") and w not in self.invalid_ways_to_attend_class:
                ans += 1

        return ans


if __name__ == "__main__":
    try:
        days = int(sys.argv[1])
        print("Number of days = {}".format(days))
    except ValueError:
        print("'Days' argument must be of integer type")
    except IndexError:
        print("Please pass 'days' argument in command line")
    except Exception as e:
        print(e)
    else:
        solution = Solution(days)
        print(f"{solution.num_of_ways_student_can_miss_ceremony()}/{solution.num_of_valid_ways_to_attend_class()}")
