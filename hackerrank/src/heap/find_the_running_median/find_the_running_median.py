#!/bin/python3
from dataclasses import dataclass, field
from heapq import heappop, heappush

from typing import List, Optional


@dataclass
class RunningMedian:
    max_lower_heap: List[int] = field(default_factory=list)
    min_upper_heap: List[int] = field(default_factory=list)
    item_count: int = 0

    @property
    def current(self) -> Optional[float]:
        if self.item_count == 0:
            return None
        size_max = len(self.max_lower_heap)
        size_min = len(self.min_upper_heap)

        if size_max == size_min:
            sliced = float(self.max_lower_side + self.min_upper_side)
            med = float(sliced) / 2.0
        elif size_max > size_min:
            med = float(self.max_lower_side)
        else:
            med = float(self.min_upper_side)

        return round(med, 1)

    def update(self, new_item) -> None:
        if self.item_count == 0:
            self.push_max(new_item)
        elif self.item_count == 1:
            if self.max_lower_side > new_item:
                last_item = self.pop_max()
                self.push_max(new_item)
                self.push_min(last_item)
            else:
                self.push_min(new_item)
        else:
            if new_item < self.current:
                self.push_max(new_item)
            else:
                self.push_min(new_item)

        size_max = len(self.max_lower_heap)
        size_min = len(self.min_upper_heap)
        if abs(size_max - size_min) > 1:
            if size_max > size_min:
                item = self.pop_max()
                self.push_min(item)
            else:
                item = self.pop_min()
                self.push_max(item)

        self.item_count += 1

    def push_max(self, item):
        heappush(self.max_lower_heap, -item)

    def push_min(self, item):
        heappush(self.min_upper_heap, item)

    def pop_max(self):
        return -heappop(self.max_lower_heap)

    def pop_min(self):
        return heappop(self.min_upper_heap)

    @property
    def max_lower_side(self):
        return -self.max_lower_heap[0]

    @property
    def min_upper_side(self):
        return self.min_upper_heap[0]


def runningMedian(a):
    medians = []
    median = RunningMedian()
    for item in a:
        median.update(item)
        # print("-----")
        # print(f"Max Lower: {median.max_lower_heap}")
        # print(f"Min upper: {median.min_upper_heap}")
        # print(f"Min upper: {median.current}")
        medians.append(median.current)
    return medians


# Expected:
# 12.0
# 8.0
# 5.0
# 4.5
# 5.0
# 6.0
TEST_CASE_1 = [12, 4, 5, 3, 8, 7]


def main():
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # a_count = int(input())
    # a = []
    # for _ in range(a_count):
    #     a_item = int(input())
    #     a.append(a_item)
    result = runningMedian(TEST_CASE_1)
    print('\n'.join(map(str, result)))
    # fptr.write('\n')
    # fptr.close()


if __name__ == '__main__':
    main()
