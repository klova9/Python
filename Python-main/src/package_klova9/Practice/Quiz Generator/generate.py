import json
import random


with open('Python-main\src\package_klova9\Practice\Quiz Generator\questions.json') as f:
    quiz = json.dump()
print(random.choice(quiz['question']))
