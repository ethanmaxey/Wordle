import unittest
from unittest.mock import patch
from src.agile_word_picker import *

class TestAgileWordPicker(unittest.TestCase):
  
    def test_get_response_for_list_returns_string(self):
      self.assertEqual(type(get_response_for_list()), str)

    def test_parse_response_takes_string_returns_list_of_words(self):
      self.assertEqual(parse_response("[FAVOR, RIVER,PRINT]"), ["FAVOR", "RIVER", "PRINT"])
      
    def test_parse_takes_empty_string_returns_empty_list(self):
      self.assertEqual(parse_response("[]"), [])
      
    def test_parse_throws_exception_if_string_has_no_list(self):
      
      with self.assertRaises(Exception):
        parse_response("FAVOR, RIGOR, SUGAR")

    def test_get_random_word_with_seed(self):
      
      words = ["FAVOR", "RIVER", "PRINT"]
            
      self.assertTrue(get_random_word_with_seed(30, words) in words)
      
    def test_get_two_random_words_with_same_seed(self):
    
      seed = 30
      words = ["FAVOR", "RIVER", "PRINT"]
      
      self.assertNotEqual(get_random_word_with_seed(seed, words), get_random_word_with_seed(seed, words))
        
    @patch('src.agile_word_picker.get_response_for_list')
    @patch('src.agile_word_picker.parse_response')
    @patch('src.agile_word_picker.get_random_word_with_seed')
    def test_get_a_random_word_calls_dependencies(self, get_random_word_with_seed, parse_response, get_response_for_list):
    
      get_response_for_list.return_value = "[FAVOR, RIGOR, SUGAR]"
      parse_response.return_value = ["FAVOR", "RIGOR", "SUGAR"]
      get_random_word_with_seed.return_value = "FAVOR"

      self.assertEqual(get_random_word(), "FAVOR")

      get_response_for_list.assert_called_once()
      parse_response.assert_called_once_with("[FAVOR, RIGOR, SUGAR]")

      calls = get_random_word_with_seed.mock_calls

      self.assertEqual(type(calls[0][1][0]), float)
      self.assertEqual(calls[0][1][1], ["FAVOR", "RIGOR", "SUGAR"])    
        
    @patch('src.agile_word_picker.get_random_word_with_seed')
    def test_get_a_random_word_calls_get_random_word_with_a_seed(self, get_random_word_with_seed):
      
      get_random_word()
      
      calls = get_random_word_with_seed.mock_calls

      self.assertEqual(type(calls[0][1][0]), float)
      
      self.assertEqual(calls[0][1][1], parse_response(get_response_for_list())) 
    
    @patch('src.agile_word_picker.get_random_word_with_seed')
    def test_get_a_random_word_calls_get_random_word_with_two_different_seeds_if_called_twice(self, get_random_word_with_seed):
            
      get_random_word()

      first_call = get_random_word_with_seed.mock_calls
      
      get_random_word()

      second_call = get_random_word_with_seed.mock_calls
      
      self.assertNotEqual(first_call[0][1][0], second_call[0][1][1])
    
    def test_random_word_length_is_5(self):
      self.assertEqual(len(get_random_word()), 5)
    
    @patch('src.agile_word_picker.parse_response')
    def test_random_word_is_all_caps(self, parse_response):
      
      parse_response.return_value = ["print"]
      
      random_word = get_random_word()
      
      self.assertEqual(random_word, random_word.upper())
    
if __name__ == '__main__':
  unittest.main()