from unittest import TestCase

from basic1 import test079


class TestsBasic1Test079(TestCase):
    '''
    Write a Python program to get the size of an object in bytes.
    '''

    def test_case1(self):
        int1 = 1
        self.assertEqual(
            test079(int1),
            28,
        )

    def test_case2(self):
        str16 = '0123456789ABCDEF'
        self.assertEqual(
            test079(str16),
            57,
        )

    def test_case3(self):
        list_int_16 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0xA, 0xB, 0xC, 0xD, 0xE, 0xF]
        self.assertEqual(
            test079(list_int_16),
            184,
        )

    def test_case4(self):
        list_str_16 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        self.assertEqual(
            test079(list_str_16),
            184,
        )
