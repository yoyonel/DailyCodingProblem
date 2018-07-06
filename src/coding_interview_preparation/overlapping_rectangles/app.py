"""
by Amozon (interview):

You're given 2 over-lapping rectangles on a plane.
For each rectangle, you're given its bottom-left and top-right points.
How would you find the area of their overlap?

Input:- Rect1((2, 1), (5, 5))
        Rect2((3, 2), (5, 7))

Result:- Area of overlapping region
"""
import attr


@attr.s
class Point:
    x: float = attr.ib()
    y: float = attr.ib()


@attr.s
class Interval:
    min: float = attr.ib()
    max: float = attr.ib()

    def compute_overlapping_area(self, other: 'Interval') -> float:
        """
        Return length of the intersection between intervals else 0

        :param other:
        :return:

        >>> Interval(0, 2).compute_overlapping_area(Interval(1, 3))
        1
        >>> Interval(1, 3).compute_overlapping_area(Interval(0, 2))
        1
        >>> Interval(1, 3).compute_overlapping_area(Interval(0, 4))
        2
        >>> Interval(0, 4).compute_overlapping_area(Interval(1, 3))
        2
        >>> Interval(0, 2).compute_overlapping_area(Interval(3, 4))
        0
        >>> Interval(3, 4).compute_overlapping_area(Interval(0, 2))
        0
        """
        length_intersected_segment = min(self.max, other.max) - max(self.min, other.min)
        return length_intersected_segment * (length_intersected_segment > 0)


@attr.s
# class AABox:
class Rectangle:
    bottom_left: Point = attr.ib()
    top_right: Point = attr.ib()

    def get_xaxis_interval(self) -> Interval:
        return Interval(self.bottom_left.x, self.top_right.x)

    def get_yaxis_interval(self) -> Interval:
        return Interval(self.bottom_left.y, self.top_right.y)

    def compute_overlapping_area(self, other: 'Rectangle') -> float:
        """
        Return overlapping area between 2 rectangles if overlop else 0
        :param other:
        :return:

        >>> Rectangle(Point(2, 1), Point(5, 5)).compute_overlapping_area(Rectangle(Point(3, 2), Point(5, 7)))
        6
        """
        return self.get_xaxis_interval().compute_overlapping_area(other.get_xaxis_interval()) * \
               self.get_yaxis_interval().compute_overlapping_area(other.get_yaxis_interval())


def main():
    # INPUTS
    rect1 = Rectangle(Point(2, 1), Point(5, 5))
    rect2 = Rectangle(Point(3, 2), Point(5, 7))

    # EXPECTED RESULT
    expected_overlapping_area = 3 * 2

    # COMPUTE
    overlapping_area = rect1.compute_overlapping_area(rect2)

    # TEST
    assert overlapping_area == expected_overlapping_area


if __name__ == '__main__':
    main()
