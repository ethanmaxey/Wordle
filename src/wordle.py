from enum import Enum

class Match(Enum):
  EXACT = 1
  EXISTS = 2
  ABSENT = 3

EXACT, EXISTS, ABSENT = Match.EXACT, Match.EXISTS, Match.ABSENT

class GameStatus(Enum):
    WON, LOST, IN_PROGRESS, WRONG_SPELLING = 1, 2, 3, 4
    
WON, LOST, IN_PROGRESS, WRONG_SPELLING = GameStatus.WON, GameStatus.LOST, GameStatus.IN_PROGRESS, GameStatus.WRONG_SPELLING

WORD_SIZE = 5

def calculate_win_or_loss_variables(current_attempt_number , response, target):
  
    messages = {1: "Amazing", 2: "Splendid", 3: "Awesome"}
    
    win_loss_dictionary = {"status": IN_PROGRESS, "message": ""}
  
    if response == [EXACT] * 5 and current_attempt_number <= 6:
    
      win_loss_dictionary["status"] = WON
      win_loss_dictionary["message"] = messages[current_attempt_number] if current_attempt_number <= 3 else "Yay"
  
    elif current_attempt_number >= 6:
      
      win_loss_dictionary["status"] = LOST 
      win_loss_dictionary["message"] = "It was {}, better luck next time".format(target)  
    
    return win_loss_dictionary

def validate_length(guess):
  
  if len(guess) != 5:
      raise Exception(f"Invalid guess = '{guess}' length of {len(guess)}")
    
def tally(target, guess):
  
  validate_length(guess)
  
  return [tally_for_position(i, target, guess) for i in range(WORD_SIZE)]

def tally_for_position(position, target, guess):
  if target[position] == guess[position]:
    return EXACT

  letter_at_position = guess[position]
  
  positional_matches = count_positional_matches(target, guess, letter_at_position)
  
  non_positional_occurrences_in_target = count_number_of_occurrences_until_position(WORD_SIZE - 1, target, letter_at_position) - positional_matches

  number_of_occurrences_in_guess_until_position = count_number_of_occurrences_until_position(position, guess, letter_at_position)

  return EXISTS if non_positional_occurrences_in_target >= number_of_occurrences_in_guess_until_position else ABSENT

def count_positional_matches(target, guess, letter):
  return len([ch for i, ch in enumerate(guess) if target[i] == ch and ch == letter])

def count_number_of_occurrences_until_position(position, word, letter):
  return word[:position + 1].count(letter)

def play(target, guess, attempts_so_far, is_spelling_correct=lambda word: True):
  
  current_attempt_number, response, status, message = attempts_so_far, [], WRONG_SPELLING, ""
  
  if (is_spelling_correct(guess)):
    
    response = tally(target, guess)
    
    current_attempt_number = attempts_so_far + 1
    
    win_loss_dict = calculate_win_or_loss_variables(current_attempt_number, response, target)
    
    status, message = win_loss_dict["status"], win_loss_dict["message"]
        
  return {"attempts": current_attempt_number, "response": response, "status": status, "message": message}