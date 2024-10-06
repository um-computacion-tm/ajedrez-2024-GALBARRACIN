import unittest
from pieces.knight import Knight

class TestKnight(unittest.TestCase):

    def setUp(self):
        self.__white_knight__ = Knight('__white__')
        self.__black_knight__ = Knight('__black__')

    def test_symbol(self):
        self.assertEqual(self.__white_knight__.symbol(), 'N')
        self.assertEqual(self.__black_knight__.symbol(), 'n')

    def test_valid_move(self):
        self.assertTrue(self.__white_knight__.is_valid_move(4, 4, 6, 5, None))
        self.assertTrue(self.__white_knight__.is_valid_move(4, 4, 2, 5, None))
        self.assertTrue(self.__black_knight__.is_valid_move(3, 3, 5, 2, None))
        self.assertTrue(self.__black_knight__.is_valid_move(7, 7, 6, 5, None))

    def test_invalid_move(self):
        self.assertFalse(self.__white_knight__.is_valid_move(4, 4, 4, 5, None))
        self.assertFalse(self.__white_knight__.is_valid_move(4, 4, 5, 4, None))
        self.assertFalse(self.__black_knight__.is_valid_move(3, 3, 4, 4, None))
        self.assertFalse(self.__black_knight__.is_valid_move(7, 7, 5, 7, None))

if __name__ == '__main__':
    unittest.main()
