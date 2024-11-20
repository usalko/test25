from io import StringIO
from unittest import TestCase

from basic1 import test052


class TestsBasic1Test052(TestCase):
    '''
    Write a Python program to print to STDERR.
    '''

    def test_case1(self):
        new_stderr = StringIO()
        import sys
        old_stderr = sys.stderr
        try:
            sys.stderr = new_stderr
            test052('Test')
            new_stderr.seek(0)
            self.assertEqual(
                new_stderr.readline(),
                'Test\n',
            )
        finally:
            sys.stderr = old_stderr
