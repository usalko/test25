from unittest import TestCase

from basic2 import test177


class TestsBasic1Test177(TestCase):
    '''27. Progression Type and Next

Write a Python program to find the type of the progression (arithmetic progression / geometric progression) and the next successive member of the three successive members of a sequence.
According to Wikipedia, an arithmetic progression (AP) is a sequence of numbers such that the difference of any two successive members of the sequence is a constant. For instance, the sequence 3, 5, 7, 9, 11, 13, . . . is an arithmetic progression with common difference 2. For this problem, we will limit ourselves to arithmetic progression whose common difference is a non-zero integer.
On the other hand, a geometric progression (GP) is a sequence of numbers where each term after the first is found by multiplying the previous one by a fixed non-zero number called the common ratio. For example, the sequence 2, 6, 18, 54, . . . is a geometric progression with common ratio 3. For this problem, we will limit ourselves to geometric progression whose common ratio is a non-zero integer.
    '''

    def test_case1(self):
        self.assertListEqual(
            test177(2),
            0,
        )
