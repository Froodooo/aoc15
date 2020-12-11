import unittest

import lib.day1


class TestDay1(unittest.TestCase):
    def test_run_a_example_1(self):
        output = lib.day1.run_a('input/1_example_1.txt')
        self.assertEqual(output, 0)
    
    def test_run_a_example_2(self):
        output = lib.day1.run_a('input/1_example_2.txt')
        self.assertEqual(output, 3)
    
    def test_run_a(self):
        output = lib.day1.run_a('input/1.txt')
        self.assertEqual(output, 280)
    
    def test_run_b_example_3(self):
        output = lib.day1.run_b('input/1_example_3.txt')
        self.assertEqual(output, 5)


if __name__ == '__main__':
    unittest.main()
