from os import remove
from profile import Profile
from tempfile import NamedTemporaryFile
from unittest import TestCase

from basic1 import get_statistics, test051


class TestsBasic1Test051(TestCase):
    '''
    Write a Python program to determine the profiling of Python programs.
    Note: A profile is a set of statistics that describes how often and for how long various parts of the program executed.
    These statistics can be formatted into reports via the pstats module.
    '''
    
    test_program: str = ''

    def tearDown(self) -> None:
        if self.test_program:
            remove(self.test_program)
        return super().tearDown()

    def test_case1(self):
        script = '''
# There is the test program for test051

def long_running_function():
    result = 0
    for i in range(0, 1000000):
        result += i
    return result

def short_running_function():
    result = 1
    for i in range(1, 10):
        result *= i
    return result

if __name__ == '__main__':
    short_running_function()
    long_running_function()

                         '''
        with NamedTemporaryFile(delete=False, prefix='test051', suffix='.py') as writer:
            writer.write(bytes(script, encoding='utf-8'))
            self.test_program = writer.name
        
        self.assertTrue(self.test_program)
        
        profile = Profile().run(script)
        profile.create_stats()
        
        stats = get_statistics(profile, lines_count=5)        


        self.assertTrue(
            'long_running_function' in test051(self.test_program, lines_count=5) and \
            'long_running_function' in stats,
        )

