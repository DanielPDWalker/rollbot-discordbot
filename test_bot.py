import unittest
import bot as b


class TestingDiceRolling(unittest.TestCase):

    def test_range_with_plus(self):
        holder = [2, 4, 1]
        for i in range(0, 1000):
            h = b.roll(1, holder)
            if h[-1] < 2:
                self.fail(f'Testing 2d4+1 somehow ended up with a {h[-1]}')
            elif h[-1] > 9:
                self.fail(f'Testing 2d4+1 Somehow ended up with a {h[-1]}')

    def test_range_with_minus(self):
        holder = [2, 4, 1]
        for i in range(0, 1000):
            h = b.roll(2, holder)
            if h[-1] < 1:
                self.fail(f'Testing 2d4-1 somehow ended up with a {h[-1]}')
            elif h[-1] > 7:
                self.fail(f'Testing 2d4-1 Somehow ended up with a {h[-1]}')

    def test_range_no_extra(self):
        holder = [2, 4, 1]
        for i in range(0, 1000):
            h = b.roll(0, holder)
            if h[-1] < 2:
                self.fail(f'Testing 2d4+1 somehow ended up with a {h[-1]}')
            elif h[-1] > 9:
                self.fail(f'Testing 2d4+1 Somehow ended up with a {h[-1]}')


if __name__ == '__main__':
    unittest.main()
