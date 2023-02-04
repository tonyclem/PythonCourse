import unittest
import script
import game


class TestMain(unittest.TestCase):
    def setUp(self):
        print('about to test a function')

    def test_do_stuff(self):
        test_param = 10
        result = script.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'string'
        result = script.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = script.do_stuff(test_param)
        self.assertEqual(result, 'Please provide Number')

    def test_do_stuff4(self):
        test_param = ''
        result = script.do_stuff(test_param)
        self.assertEqual(result, 'Please provide Number')

    def tearDown(self):
        print('cleaning up test')


class TestGame(unittest.TestCase):
    def test_input(self):
        answer = 5
        guess = 5
        result = game.run_guess(answer, guess)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        result = game.run_guess(5, 0)
        self.assertFalse(result)

    def test_input_wrong_number(self):
        result = game.run_guess(5, 11)
        self.assertFalse(result)

    def test_input_wrong_type(self):
        result = game.run_guess(5, 11)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
