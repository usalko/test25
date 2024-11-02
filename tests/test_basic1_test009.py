from unittest import TestCase
from basic1 import test009
from datetime import datetime


class TestsBasic1Test009(TestCase):
    '''
    Write a Python program to display the examination schedule. (extract the date from exam_st_date).
    exam_st_date = (11, 12, 2014)
    Sample Output : The examination will start from : 11 / 12 / 2014
    '''

    def test_case1(self):
        self.assertEqual(
            test009((11, 12, 2014)),
            'The examination will start from : 11 / 12 / 2014',
        )