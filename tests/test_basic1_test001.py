from unittest import TestCase
from basic1 import test001


class TestsBasic1Test001(TestCase):
    '''
    Write a Python program to print the following string in a specific format (see the output).
    Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
    Output :

    Twinkle, twinkle, little star,
        How I wonder what you are!
            Up above the world so high,
            Like a diamond in the sky.
    Twinkle, twinkle, little star, 
        How I wonder what you are
    '''
    
    def test_case1(self):
        self.assertEqual(
                    test001('Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are'),
                    '''Twinkle, twinkle, little star,
    How I wonder what you are!
        Up above the world so high,
        Like a diamond in the sky.
Twinkle, twinkle, little star,
    How I wonder what you are''')
