"""
Given an array of time intervals (start, end) for classroom lectures (possibly overlapping),
find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""
import attr
from typing import List, Optional, Tuple


def min_smaller_than_max(instance, attribute, value):
    if value >= instance.max:
        raise ValueError("'min' has to be smaller than 'max'!")


@attr.s
class Interval:
    min: float = attr.ib(validator=[attr.validators.instance_of(int), min_smaller_than_max])
    max: float = attr.ib()

    def compute_intersection(self, other: 'Interval') -> Optional['Interval']:
        """

        :param other:
        :return:

        >>> Interval(0, 2).compute_intersection(Interval(1, 3))
        Interval(min=1, max=2)

        >>> Interval(1, 3).compute_intersection(Interval(0, 2))
        Interval(min=1, max=2)

        >>> Interval(1, 3).compute_intersection(Interval(0, 4))
        Interval(min=1, max=3)

        >>> Interval(0, 4).compute_intersection(Interval(1, 3))
        Interval(min=1, max=3)

        >>> Interval(0, 2).compute_intersection(Interval(3, 4))

        >>> Interval(3, 4).compute_intersection(Interval(0, 2))

        """
        try:
            return Interval(max(self.min, other.min), min(self.max, other.max))
        except ValueError:
            return None


@attr.s
class Intervals:
    intervals: List[Interval] = attr.ib(default=[])

    @classmethod
    def from_tuples(cls, tuples_intervals: List[Tuple[int, int]]) -> 'Intervals':
        intervals = cls()
        intervals.intervals = [
            Interval(*t_i)
            for t_i in tuples_intervals
        ]
        return intervals

    def count_max_overlapping(self):
        """
        Speed cost: O(n.log(n))
        Memory cost: O(1)

        :return:
        """
        max_overlapping = 0
        intersected_interval = None     # type: Optional[Interval]
        cur_overlapping = 0
        # Sort intervals: O(n*log(n))
        # Count overlapping and find the max: O(n)
        for interval in sorted(
            self.intervals,
            key=lambda i: i.min
        ):
            if intersected_interval:
                intersected_interval = intersected_interval.compute_intersection(interval)
                cur_overlapping += intersected_interval is not None
                max_overlapping = max(max_overlapping, cur_overlapping)
            else:
                intersected_interval = interval
                cur_overlapping = 0
        return max_overlapping

    def find_the_minimum_number_of_rooms_required(self):
        return self.count_max_overlapping() + 1


def main():
    intervals = Intervals.from_tuples([(30, 75), (0, 50), (60, 150)])
    expected_result = 2
    assert intervals.find_the_minimum_number_of_rooms_required() == expected_result

    intervals = Intervals.from_tuples([(30, 75), (0, 50), (60, 150), (35, 65)])
    expected_result = 3
    assert intervals.find_the_minimum_number_of_rooms_required() == expected_result


if __name__ == '__main__':
    main()
