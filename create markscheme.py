import re, json, os
from pathlib import Path as p

with open('data.json', 'r') as f:
  quizData = json.loads(f.read())
  f.close()
quizPath = p(p.cwd()/'quizzes')
answerPath = p(p.cwd()/'markschemes')

if not answerPath.exists():
  os.makedirs(answerPath)

for file in quizPath.glob('*'):
  print(file)
  with open(file) as qf:
    quiz= qf.read().split('\n\n\n');
    qa = quiz[1].split('\n\n');
    with open(answerPath/'{}.txt'.format(file.stem), 'w') as af:
      fileIndex = re.search(r'\d+', file.stem).group()
      af.write('QUiz {} answersheet\n\n'.format(fileIndex))
      for q in qa:
        [q, a] = q.split('\n');
        capital = q.strip().split(' ')[len(q.strip().split(' '))-1];
        capital = capital[:len(capital)-1];
        key = q.strip().split(' ')[0];
        b = []
        for question in quizData.keys():
          if question.endswith(capital):
            b.append(question)
        
        b.sort()
        b.reverse()

        for question in b:
          v = re.search(question, q)
          if v:
            capital = v.group()
            break
        
        question_key = q.strip().split(' ')[0]
        answer = quizData[capital]
        answerReg = re.search('[A-D]. {}'.format(answer), a)
        af.write('{} {}\n'.format(question_key, answerReg.group().split(' ')[0][0]))
      af.close()
    f.close()
