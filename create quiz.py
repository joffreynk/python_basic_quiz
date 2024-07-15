  #! python3
  # randomQuizGenerator.py - Creates quizzes with questions and answers in
  # random order, along with the answer key.
import random, os, json
from pathlib import Path
# The quiz data. Keys are questions and values are their allAnswers.
with open('data.json', 'r') as f:
  quizData = json.loads(f.read())
  f.close()

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
  # TODO: Shuffle the order of the questions from main data and get the first 15.
  questions = list(quizData.keys())
  random.shuffle(questions)
  random.shuffle(questions)
  s = questions[:15]
  
  # TODO: Loop through all 15 questions, making a question for each.
  for index, question in enumerate(s):
    allAnswers = list(quizData.values())
    allAnswers.remove(quizData[question])
    random.shuffle(allAnswers)
    random.shuffle(allAnswers)
    c = allAnswers[15:18] # get 3 answers from all all Answers
    c.append(quizData[question]) # add the correct answer to answers list
    random.shuffle(c)
    random.shuffle(c)
    file.write('Q{}. what is the capital city of the {}? \n'.format(index+1, question)) #format the question basd on your case
    file.write('A. {}\t B. {}\t C. {}\t D. {}'.format(c[1], c[0], c[3], c[2]))
    if index<len(s)-1: file.write('\n\n');
  
  file.close()

