import requests

def get_response_for(word):
  
  url = f"http://agilec.cs.uh.edu/spell?check={word}"
  
  return requests.post(url).text

def parse_response(response):
  return response == "true"

def is_spelling_correct(word):
  return parse_response(get_response_for(word))