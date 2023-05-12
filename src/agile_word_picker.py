import requests, random, time

def get_response_for_list():

  url = "https://agilec.cs.uh.edu/words"

  return requests.get(url).text.strip()

def is_valid_response(response):
    return response.startswith("[") and response.endswith("]")

def parse_response(response):
    
  if not is_valid_response(response): raise Exception
  
  words_list = [word.strip() for word in response[1:-1].split(",") if len(word.strip()) == 5]
  
  return words_list if len(response) > 2 else []

def get_random_word_with_seed(seed, words):
  
  get_random_word_with_seed.seed = getattr(get_random_word_with_seed, 'seed', None)
  
  if get_random_word_with_seed.seed != seed:
    
    get_random_word_with_seed.seed = seed
    random.seed(seed)
    
  return random.choice(words)

def get_random_word():

  seed = time.time()
  
  return get_random_word_with_seed(seed, parse_response(get_response_for_list())).upper()