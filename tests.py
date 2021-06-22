from unittest import TestCase
from unittest.mock import patch

from pandas import DataFrame

from levenshtein_calculation.apply_levenshtein import get_distance_words


class TestLevenshteinCalculation(TestCase):
    """Ensure apply_levenshtein script is working properly"""

    def test_get_distance_words(self):
        """Ensure levenshtein function is working properly"""
        df = DataFrame({"HUNDENAME": ["Luca", "Lucia", ""]})

        with patch("levenshtein_calculation.apply_levenshtein.read_csv", return_value=df):
            # If distance is 0 then name in list should be Luca
            self.assertEqual(get_distance_words("Luca", 0), ["Luca"])
            # If distance is 1 then result list should contain Lucia
            self.assertEqual(get_distance_words("Luca", 1), ["Lucia"])
            # If empty string gets processed levenshtein distance of 4 is used
            self.assertEqual(get_distance_words("Luca", 4), [""])
