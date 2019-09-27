import unittest
from models import movie
Movie = movie.Movie

class pitchTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.pitch = Pitch(1,'technology','technology is growing','technology',,129993)

    def test_instance(self):
        self.assertTrue(isinstance(self.pitch,Pitch))


if __name__ == '__main__':
    unittest.main()

    