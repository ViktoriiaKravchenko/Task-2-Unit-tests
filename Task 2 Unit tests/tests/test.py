import unittest
from anagrams import reverse


class TestAnagrams(unittest.TestCase):

    def setUp(self):
        self.param_list = [("rt5k ern!", "kt5r nre!"), ("abc3 *d?e", "cba3 *e?d"), ("d7k0 n1sa", "k7d0 a1sn")]

    def test_typical_behavior(self):
        for p1, p2 in self.param_list:
            self.assertEqual(reverse(p1), p2)

    def test_atypical_behavior(self):
        with self.assertRaises(TypeError):
            reverse(12345)
            reverse(12.5)


if __name__ == "__main__":
    unittest.main()
