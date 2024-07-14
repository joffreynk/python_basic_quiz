  #! python3
  # randomQuizGenerator.py - Creates quizzes with questions and answers in
  # random order, along with the answer key.
import random, os
from pathlib import Path
# The quiz data. Keys are questions and values are their allAnswers.
quizData = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
  'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
  'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
  'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':'Springfield',
  'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':'Topeka',
  'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':'Augusta',
  'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':'Lansing',
  'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':'Jefferson City',
  'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City',
  'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
  'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
  'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
  'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':'Nashville',
  'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':'Montpelier',
  'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

description = 'Full Name:_________________________________ \nClass:________ \nGeography quiz\n\nInstructions:\nPlease attempt all the questions.\nThe use of the computer or map is highly discouraged\n\n\n'

quizPath = Path(Path.cwd()/'quizzes')

if not quizPath.exists():
  os.makedirs(quizPath)

# Generate 35 quiz files.
for quizNum in range(35):
  # TODO: Create the quiz and answer key files.
  file = open('{}/quiz{}.txt'.format(quizPath, quizNum+1), 'w')
  # TODO: Write out the header for the quiz.
  file.write(description)
  # TODO: Shuffle the order of the questions from main data and get the first 12.
  questions = list(quizData.keys())
  random.shuffle(questions)
  random.shuffle(questions)
  s = questions[1:12]
  
  # TODO: Loop through all 12 questions, making a question for each.
  for index, q in enumerate(s):
    allAnswers = list(quizData.values())
    allAnswers.remove(quizData[q])
    random.shuffle(allAnswers)
    random.shuffle(allAnswers)
    c = allAnswers[15:18] # get 3 answers from all all Answers
    c.append(quizData[q]) # add the correct answer to answers list
    random.shuffle(c)
    random.shuffle(c)
    file.write('Q{}. what is the capital city of the {}? \n'.format(index+1, q)) #format the question basd on your case
    file.write('A. {}\t B. {}\t C. {}\t D. {}\n\n'.format(c[1], c[0], c[3], c[2]))
  
  file.close()

