import unittest
from unittest.mock import patch
from src.wordle_agile_spellcheck import get_response_for, parse_response, is_spelling_correct
from parameterized import parameterized

class TestAgileSpellcheck(unittest.TestCase):
    
    def test_get_response_takes_FAVOR_returns_response(self):
        self.assertEqual(type(get_response_for("FAVOR")), str)
    
    @parameterized.expand([
    ("true", True),
    ("false", False)
    ])
    def test_parse_response_takes_string_returns_boolean(self, response, spelled_correct):
        self.assertEqual(parse_response(response), spelled_correct)
      
    @patch('src.wordle_agile_spellcheck.get_response_for')
    @patch('src.wordle_agile_spellcheck.parse_response')
    def test_is_spelling_correct_calls_get_response_and_parse(self, parse_response, get_response_for):
        
        word = "FAVOR"
        response = "true"

        get_response_for.return_value = response
        parse_response.return_value = True

        self.assertEqual(is_spelling_correct(word), True)
    
        get_response_for.assert_called_with(word)
        parse_response.assert_called_with(response)


    @patch('src.wordle_agile_spellcheck.get_response_for')
    def test_is_spelling_correct_passes_exception_from_get_response_to_caller(self, get_response_for):

        get_response_for.side_effect = Exception

        with self.assertRaises(Exception):
            is_spelling_correct("FAVOR")
    
if __name__ == '__main__':
  unittest.main()