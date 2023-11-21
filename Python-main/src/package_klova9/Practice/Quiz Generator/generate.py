import json
import random

quiz = json.load(open('Python-main\src\package_klova9\Practice\Quiz Generator\questions.json'))

i = random.randint(0, len(quiz) - 1)
print(quiz[i]['question']+quiz[i]['answer'])