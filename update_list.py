# keep an updated list of trivia questions from opentdb with answers
# start: 5:39 pm
# finish: 6:01 pm
# time: 22 minutes
# finished debugging: can't say. was interrupted.
# total time: n/a
import requests
import json

def add_more_questions(data):
  questions_api_url = "https://opentdb.com/api.php?amount=50"
  new_questions = read_json_from_url(questions_api_url)["results"]

  data = read_json_file()
  if not data: data = []

  for q in new_questions:
    if q not in data:
      data.append(q)
  write_json_file(data)

# Makes a request to a JSON API, and returns the data as a JSON
def read_json_from_url(json_url, filename="trivia_questions.json"):
  # Download all the questions along with their answers
  # Optimizing this code should take ten minutes.
  # I'll have it pull open the file each time for now, since that's easier to write
  r = requests.get(json_url)
  return json.loads(r.text)

# Parses a JSON file and returns the parsed text
def read_json_file(filename="trivia_questions.json"):
  try:
    with open(filename, "r") as questions_file:
      return json.load(questions_file)
  except FileNotFoundError:
    pass  # if file doesn't exist, we'll create it
  return None

def write_json_file(data, filename="trivia_questions.json"):
  with open(filename, "w") as questions_file:
    json.dump(data, questions_file, indent=2)

def main():
  # Get the current number of verified questions so it knows how many questions we need
  # (Is the number before " Verified Questions" in the h4 tag at https://opentdb.com/ accurate/up-to-date? What's the best URL to pull the current number of questions from?)
  num_questions = 3706
  list_of_questions = []

  from time import sleep 
  while len(read_json_file()) < num_questions:
    print(len(read_json_file()))
    add_more_questions(list_of_questions)

if __name__ == "__main__":
  main()
