import unittest
from src.wordle import *
from parameterized import parameterized

class TestWordle(unittest.TestCase):
  
  @parameterized.expand([
    ([EXACT, EXACT, EXACT, EXACT, EXACT], "FAVOR", "FAVOR"),
    ([ABSENT, ABSENT, ABSENT, ABSENT, ABSENT], "TESTS", "FAVOR"),
    ([EXISTS, EXACT, ABSENT, ABSENT, ABSENT], "RAPID", "FAVOR"),
    ([ABSENT, EXACT, ABSENT, EXACT, EXACT], "MAYOR", "FAVOR"), 
    ([ABSENT, ABSENT, EXACT, ABSENT, EXACT], "RIVER", "FAVOR"),
    ([EXISTS, ABSENT, ABSENT, ABSENT, ABSENT], "AMAST", "FAVOR"),
    
    ([EXACT, EXACT, EXACT, EXACT, EXACT], "SKILL", "SKILL"),
    ([EXACT, ABSENT, EXACT, ABSENT, EXACT], "SWIRL", "SKILL"),
    ([ABSENT, EXISTS, ABSENT, ABSENT, EXACT], "CIVIL", "SKILL"),
    ([EXACT, ABSENT, EXACT, ABSENT, ABSENT], "SHIMS", "SKILL"),
    ([EXACT, EXISTS, EXISTS, EXACT, ABSENT], "SILLY", "SKILL"),
    ([EXACT, EXISTS, EXACT, ABSENT, ABSENT], "SLICE", "SKILL"),
   ])
  def test_tally_for_target_versus_guess(self, expected_tally, guess, target): 
    self.assertEqual(expected_tally, tally(target, guess))
  
  @parameterized.expand([
    ("FOR"),
    ("FERVER"),
  ])
  def test_for_wrong_word_length(self, guess):
    with self.assertRaises(Exception) as context:
      tally("FAVOR", guess)

  def test_play_deal_with_invalid_first_guess(self):
    with self.assertRaises(Exception) as context:
      play("FAVOR", "DEAL", 0)

  losing_message = "It was FAVOR, better luck next time"
  @parameterized.expand([    
    ("FAVOR", "FAVOR", 0, 1, [EXACT] * 5, WON, "Amazing"),
    ("FAVOR", "WRONG", 0, 1, [ABSENT, EXISTS, EXISTS, ABSENT, ABSENT], IN_PROGRESS, ""),
    ("FAVOR", "FAVOR", 1, 2, [EXACT] * 5, WON, "Splendid"),
    ("FAVOR", "WRONG", 1, 2, [ABSENT, EXISTS, EXISTS, ABSENT, ABSENT], IN_PROGRESS, ""),
    ("FAVOR", "FAVOR", 2, 3, [EXACT] * 5, WON, "Awesome"),
    ("FAVOR", "WRONG", 2, 3, [ABSENT, EXISTS, EXISTS, ABSENT, ABSENT], IN_PROGRESS, ""),
    ("FAVOR", "FAVOR", 3, 4, [EXACT] * 5, WON, "Yay"),
    ("FAVOR", "WRONG", 3, 4, [ABSENT, EXISTS, EXISTS, ABSENT, ABSENT], IN_PROGRESS, ""),
    ("FAVOR", "FAVOR", 4, 5, [EXACT] * 5, WON, "Yay"),
    ("FAVOR", "WRONG", 4, 5, [ABSENT, EXISTS, EXISTS, ABSENT, ABSENT], IN_PROGRESS, ""),
    ("FAVOR", "FAVOR", 5, 6, [EXACT] * 5, WON, "Yay"),
    ("FAVOR", "WRONG", 5, 6, [ABSENT, EXISTS, EXISTS, ABSENT, ABSENT], LOST, losing_message),
    ("FAVOR", "FAVOR", 6, 7, [EXACT] * 5, LOST, losing_message),
    ("FAVOR", "WRONG", 7, 8, [ABSENT, EXISTS, EXISTS, ABSENT, ABSENT], LOST, losing_message)
  ])
  def test_play_with_different_inputs(self, target, guess, attempt_number, new_attempt, response, status, message):
    self.assertEqual(play(target, guess, attempt_number), {"attempts": new_attempt, "response": response, "status": status, "message": message})
  
  @parameterized.expand([
    ("FAVOR", "FAVOR", {"attempts": 1, "response": [EXACT] * 5, "status": WON, "message": "Amazing"}, True, 0),
    ("FAVOR", "RIVER", {"attempts": 1, "response": [ABSENT, ABSENT, EXACT, ABSENT, EXACT], "status": IN_PROGRESS, "message": ""}, True, 0),
    ("FAVOR", "FAVOR", {"attempts": 0, "response": [], "status": WRONG_SPELLING, "message": ""}, False, 0), 
    ("FAVOR", "RIVER", {"attempts": 1, "response": [], "status": WRONG_SPELLING, "message": ""}, False, 1),
  ])
  def test_play_with_correct_spelling(self, target, guess, expected_response, expected_validity, attempt):
    
    def is_spelling_correct(word):
      is_spelling_correct.called_with = word
      return expected_validity
    
    self.assertEqual(play(target, guess, attempt, is_spelling_correct), expected_response)
    self.assertEqual(is_spelling_correct.called_with, guess)
  
  def test_play_with_exception_raises_exception(self):
    
    def is_spelling_correct(word):
      is_spelling_correct.called_with = word
      raise Exception

    with self.assertRaises(Exception): play("FAVOR", "RIVER", 0, is_spelling_correct)

if __name__ == '__main__':
  unittest.main()