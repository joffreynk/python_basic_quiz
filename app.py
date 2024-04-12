  # ! python3
  # randomQuizGenerator.py - Creates quizzes with questions and answers in
  # random order, along with the answer key.
import random, os, pathlib as p
# The quiz data. Keys are states and values are their capitals.
allStates = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
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

# Generate 35 quiz files.
for quizNum in range(35):
  # TODO: Create the quiz and answer key files.
  file = open('Quiz{}.txt'.format(quizNum+1), 'w')
  # TODO: Write out the header for the quiz.
  file.write('Full Name:_________________________________ \nClass:________ \nGeography quiz\n\nInstructions:\nPlease attempt all the questions.\nThe use of the computer or map is highly discouraged\n\n\n')
  # TODO: Shuffle the order of the states.
  states = list(allStates.keys())
  random.shuffle(states)
  random.shuffle(states)
  s = states[1:12]
  
  # TODO: Loop through all 50 states, making a question for each.
  for q in s:
    capitals = list(allStates.values())
    capitals.remove(allStates[q])
    random.shuffle(capitals)
    random.shuffle(capitals)
    c = capitals[15:18]
    c.append(allStates[q])
    random.shuffle(c)
    file.write('what is the capital city of the {}? \n'.format(q))
    file.write('A. {}\t B. {}\t C. {}\t D. {}\n\n'.format(c[1], c[0], c[3], c[2]))
  
  file.close()

