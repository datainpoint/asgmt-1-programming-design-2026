import unittest
import importlib

class TestAssignmentOne(unittest.TestCase):
    def test_01(self):
        self.assertTrue(asgmt.is_return_necessary_for_assignments())
    def test_02(self):
        self.assertEqual(asgmt.calculate_movie_minutes(2, 22), 142)
        self.assertEqual(asgmt.calculate_movie_minutes(2, 55), 175)
        self.assertEqual(asgmt.calculate_movie_minutes(2, 32), 152)
        self.assertEqual(asgmt.calculate_movie_minutes(2, 1), 121)
        self.assertEqual(asgmt.calculate_movie_minutes(1, 2), 62)
    def test_03(self):
        self.assertEqual(asgmt.say_hello_to_anyone("world"), 'Hello World!')
        self.assertEqual(asgmt.say_hello_to_anyone("python"), 'Hello Python!')
        self.assertEqual(asgmt.say_hello_to_anyone("tony"), 'Hello Tony!')
    def test_04(self):
        self.assertEqual(asgmt.format_number_of_assignments_exams_bonuses(6, 2, 2), '6 assignments 2 examinations 2 bonuses.')
    def test_05(self):
        self.assertEqual(asgmt.repeat_n_times("Important!", 3), 'Important!Important!Important!')
        self.assertEqual(asgmt.repeat_n_times("Go!", 3), 'Go!Go!Go!')
        self.assertEqual(asgmt.repeat_n_times("Awesome!", 2), 'Awesome!Awesome!')
        self.assertEqual(asgmt.repeat_n_times("Fantastic!", 5), 'Fantastic!Fantastic!Fantastic!Fantastic!Fantastic!')
        self.assertEqual(asgmt.repeat_n_times("Run! Forrest, run!", 1), 'Run! Forrest, run!')
    def test_06(self):
        self.assertEqual(asgmt.format_temperature_degrees(0), "0 Degrees Celsius = 32.0 Degrees Fahrenheit")
        self.assertEqual(asgmt.format_temperature_degrees(100), "100 Degrees Celsius = 212.0 Degrees Fahrenheit")
    def test_07(self):
        self.assertEqual(asgmt.format_integer_with_dollar_sign_and_commas(1000), "$1,000")
        self.assertEqual(asgmt.format_integer_with_dollar_sign_and_commas(1000000), "$1,000,000")
        self.assertEqual(asgmt.format_integer_with_dollar_sign_and_commas(1000000000), "$1,000,000,000")
        self.assertEqual(asgmt.format_integer_with_dollar_sign_and_commas(10000), "$10,000")
        self.assertEqual(asgmt.format_integer_with_dollar_sign_and_commas(100000), "$100,000")
    def test_08(self):
        self.assertFalse(asgmt.is_positive(-2))
        self.assertFalse(asgmt.is_positive(-1))
        self.assertFalse(asgmt.is_positive(0))
        self.assertTrue(asgmt.is_positive(1))
        self.assertTrue(asgmt.is_positive(2))
    def test_09(self):
        self.assertFalse(asgmt.is_even(1))
        self.assertFalse(asgmt.is_even(3))
        self.assertFalse(asgmt.is_even(5))
        self.assertTrue(asgmt.is_even(0))
        self.assertTrue(asgmt.is_even(2))
    def test_10(self):
        self.assertFalse(asgmt.are_vowels_contained('pythn'))
        self.assertFalse(asgmt.are_vowels_contained('ncnd'))
        self.assertFalse(asgmt.are_vowels_contained('rtclt'))
        self.assertTrue(asgmt.are_vowels_contained('anaconda'))
        self.assertTrue(asgmt.are_vowels_contained('reticulate'))

asgmt = importlib.import_module("answers")
suite = unittest.TestLoader().loadTestsFromTestCase(TestAssignmentOne)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)
number_of_failures = len(test_results.failures)
number_of_errors = len(test_results.errors)
number_of_test_runs = test_results.testsRun
number_of_successes = number_of_test_runs - (number_of_failures + number_of_errors)
print("You've got {} successes among {} questions.".format(number_of_successes, number_of_test_runs))